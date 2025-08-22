---
description: "Detailed guide to the video splitting pipeline for breaking down long videos into clips with automated captioning and embedding generation"
categories: ["video-curation"]
tags: ["video-splitting", "gpu-accelerated", "pipeline", "captioning", "embedding", "docker", "nvdec", "nvenc"]
personas: ["mle-focused", "data-scientist-focused"]
difficulty: "intermediate"
content_type: "tutorial"
modality: "video-only"

---

(video-pipelines-splitting)=

# Splitting Pipeline

```{image} ../../about/concepts/video/_images/video-pipeline-diagram.png
:alt: Video Pipeline Diagram
```

The splitting pipeline is the first of two video curation pipelines in NeMo Curator. It performs the following stages:

1. **Video Download**: Downloads the videos from cloud storage or reads them from disk into memory.
2. **Decoding and Splitting**: Decodes the video frames from the raw mp4 bytes and runs a TransNetV2-based splitting algorithm to split the video into clips based on rapid changes in color from frame to frame.
3. **Transcoding**: Encodes each of the clips into individual mp4 files under the same encoding (H264).
4. **Filtering**: Filters out clips based on motion and aesthetics.
5. **Video Embedding**: Creates an embedding for each clip. While not directly used by the curation pipeline, it can be used in other ways like constructing a visual semantic search. This is not to be confused with the video tokenizer. These embeddings are created with the InternVideo2 model.
6. **Captioning**: Generates a text caption of the clip using a vision-language model.

These clips and captions can then be manually inspected before producing a final output dataset.

---

## Use Cases

- Generating clips for generative video model fine-tuning.
- Creating vector embeddings for a semantic search across the dataset.

---

## Prerequisites

Before you can use the splitting pipeline, make sure that you have:

- Completed the {ref}`gs-video` guide.

---

## Run the NeMo Curator Video Splitting Pipeline

The following setup allows you to split videos either from a local directory or from cloud storage, creating short clips with video embeddings and synthetic captions.

### With Videos Stored Locally

If the data is located at `~/nemo_curator_local_workspace/input_videos`, run the following command:

```bash
mkdir -p ~/nemo_curator_local_workspace/output_clips

video_curator launch \
    --image-name nemo_video_curator --image-tag 1.0.0 \
    --no-mount-s3-creds \
    -- python3 -m nemo_curator.video.pipelines.video.run_pipeline split \
    --input-video-path /config/input_videos \
    --output-clip-path /config/output_clips \
    --verbose
```

This command uses `video_curator launch` to run the splitting pipeline (`python3 -m nemo_curator.video.pipelines.video.run_pipeline split`) inside the Docker container.

### With Videos Stored in Cloud Storage

If your data is stored on cloud storage, replace the path with an S3 path and remove the `--no-mount-s3-creds` flag.

```bash
video_curator launch \
    --image-name nemo_video_curator --image-tag 1.0.0 \
    -- python3 -m nemo_curator.video.pipelines.video.run_pipeline split \
    --input-video-path s3://video-storage/raw_videos/ \
    --output-clip-path s3://video-storage/clips/ \
    --verbose
```

The output clip path will have the following structure:

```
~/nemo_curator_local_workspace/output_clips/
    clips/
    iv2_emb/
    metas/
    previews/
    processed_videos/
    v0/
    summary.json
```

```{list-table} Directory Descriptions
:widths: 20 80
:header-rows: 1

* - Directory
  - Description
* - `clips/`
  - `.mp4` files for the transcoded clips.
* - `iv2_emb/`
  - `.pickle` files for the InternVideo2 video embeddings.
* - `metas/`
  - `.json` files containing metadata for each clip.
* - `previews/`
  - `.webp` files for web previews for each of the windows in each video used to generate the captions.
* - `processed_videos/`
  - `.json` files for metadata about each original video that was processed.
* - `v0/`
  - `all_window_captions.json` contains an aggregation of all the captions generated across all the clips.
* - `summary.json`
  - A summary of the splitting pipeline results.
```

---

## Key Parameters

Here are a few key parameters shown in this example:

```{list-table} Parameters
:header-rows: 1

* - Parameter
  - Description
* - `--image-name nemo_video_curator` and `--image-tag 1.0.0`
  - Specifies the Docker image and tag to use.
* - `--no-mount-s3-creds`
  - This flag prevents the S3 credentials from being mounted in the container. It's useful when you don't have S3 credentials and your data is stored locally.
* - `--input-video-path`
  - Specifies the path inside the container or on cloud storage that holds all the .mp4 files to be clipped. If you need to access local data, the directory `~/nemo_curator_local_workspace/` is mounted to `/config/`.
* - `--output-clip-path`
  - Indicates where the output clips and metadata will be stored. It functions similarly to `--input-video-path` in terms of mounts.
```

With `--input-video-path` above, by default it will find all files under that path. In case there are too many files under the same path, you can also provide a specific list of videos in a json file in list format like below:

```json
[
    "s3://input-data/video1.mp4",
    "s3://input-data/video2.mp4",
    "s3://input-data/video3.mp4"
]
```

Then this json can be passed in with `--input-video-list-json-path`; same as paths above, this can be either a path inside the container or on cloud storage.

You can find a list of all parameters in the launcher by running:

```bash
video_curator launch --help
```

In addition, you can find a list of all parameters used in the splitting pipeline by running:

```bash
video_curator launch \
    --image-name nemo_video_curator --image-tag 1.0.0 \
    --curator-path ./ \
    -- python3 -m nemo_curator.video.pipelines.video.run_pipeline split \
    --help
```

---

## Performance Considerations

### Accelerate Pipeline Processing
You can accelerate the splitting pipeline using NVIDIA's [NVDEC video decoder](https://docs.nvidia.com/video-technologies/video-codec-sdk/12.1/nvdec-video-decoder-api-prog-guide/index.html) and [NVENC video encoder](https://docs.nvidia.com/video-technologies/video-codec-sdk/11.1/nvenc-video-encoder-api-prog-guide/index.html) by setting the following parameters.

```{note}
Not all GPUs support NVENC (`h264_nvenc`). Verify your GPU supports NVENC before configuring the following parameters.
```

```{list-table}
:header-rows: 1

* - Parameter
  - Description
  - Default Value
* - `VideoFrameExtractionStage`'s `decoder_mode`
  - Specifies the decoder used for splitting clips. Can be set to `ffmpeg_cpu`, `ffmpeg_gpu`, or `pynvc`. Choose between ffmpeg on CPU or GPU or PyNvVideoCodec for video decoding.
  - `ffmpeg_cpu`
* - `ClipTranscodingStage`'s `encoder`
  - Specifies the encoder used for transcoding clips. Can be set to either `libopenh264` or `h264_nvenc`. If you choose to use `h264_nvenc`, ensure that your GPU supports the hardware encoder.
  - `libopenh264`
* - `ClipTranscodingStage`'s `use_hwaccel`
  - Specifies whether to use a hardware accelerator for decoding phase of transcoding. If used when `--encoder` is set to `h264_nvenc`, the hardware accelerator will be `NVENC`. If unset, the hardware accelerator is automatically chosen by `ffmpeg`.
  - N/A
```

### Reduce Memory Requirements

If you need to run the splitting pipeline on less than 38 GB of VRAM, you can reduce the memory requirements by:

1. Lowering the number of clips captioned at once by setting `QwenCaptionStage`'s `batch_size` argument to a lower value. By default, this parameter is set to `16`.
2. Applying fp8 weights for the Qwen model using `QwenCaptionStage`'s `fp8_enable` argument.

We've observed ~21GB of GPU memory usage when `QwenCaptionStage`'s `batch_size=1` and `fp8_enable=True` are set.