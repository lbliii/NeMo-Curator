---
description: "Detailed guide to the video splitting pipeline for breaking down long videos into clips with optional captioning and embeddings"
categories: ["video-curation"]
tags: ["video-splitting", "gpu-accelerated", "pipeline", "captioning", "embedding", "ray", "nvdec", "nvenc"]
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

The splitting pipeline reads videos, splits them into clips, and optionally transcodes, filters, embeds, generates captions, and writes results. It performs the following stages:

1. **Video Read**: Reads input videos from local or cloud storage.
2. **Decoding and Splitting**: Extracts frames and splits clips by fixed stride or TransNetV2.
3. **Transcoding**: Encodes each clip (for example, H.264).
4. **Filtering**: Filters clips based on motion and/or aesthetics.
5. **Embeddings (optional)**: Generates clip embeddings (InternVideo2 or Cosmos-Embed1).
6. **Captioning and Previews (optional)**: Generates captions and preview images.
7. **Write Outputs**: Writes media, embeddings, and metadata.

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

## Run the Splitting Pipeline (Python)

Run the example script to split videos and write outputs. Set `DATA_DIR`, `MODEL_DIR`, and `OUT_DIR` first.

```bash
python -m ray_curator.examples.video.video_split_clip_example \
  --video-dir "$DATA_DIR" \
  --model-dir "$MODEL_DIR" \
  --output-clip-path "$OUT_DIR" \
  --splitting-algorithm fixed_stride \
  --fixed-stride-split-duration 10.0 \
  --embedding-algorithm internvideo2 \
  --transcode-encoder libopenh264 \
  --verbose
```

To read from S3, configure `~/.aws/credentials` and use `s3://` for `--video-dir` and `--output-clip-path`.

The output directory contains:

```
$OUT_DIR/
  clips/
  filtered_clips/
  metas/
    v0/
  iv2_embd/
  iv2_embd_parquet/
  ce1_embd/
  ce1_embd_parquet/
  previews/
  processed_videos/
  processed_clip_chunks/
```

```{list-table} Directory Descriptions
:widths: 20 80
:header-rows: 1

* - Directory
  - Description
* - `clips/`
  - Transcoded clip media (`.mp4`).
* - `filtered_clips/`
  - Media for clips filtered out by motion/aesthetic rules.
* - `metas/v0/`
  - Clip metadata (`.json`) including dimensions, motion scores, captions, and windows.
* - `iv2_embd/`, `ce1_embd/`
  - Per-clip embeddings serialized as `.pickle`.
* - `iv2_embd_parquet/`, `ce1_embd_parquet/`
  - Embeddings written as Parquet files (batches/chunks) with columns `id` and `embedding`.
* - `previews/`
  - Preview images (`.webp`) for caption windows when enabled.
* - `processed_videos/`, `processed_clip_chunks/`
  - Video-level metadata and per-chunk clip statistics.
```

---

## Common Options

Here are a few key parameters shown in this example:

```{list-table} Selected Flags
:header-rows: 1

* - Flag
  - Description
* - `--splitting-algorithm`
  - Choose `fixed_stride` or `transnetv2`.
* - `--fixed-stride-split-duration`
  - Duration (seconds) per clip for fixed stride splitting.
* - `--transnetv2-frame-decoder-mode`
  - `pynvc`, `ffmpeg_gpu`, or `ffmpeg_cpu`.
* - `--transcode-encoder`
  - `libopenh264` or `h264_nvenc`.
* - `--transcode-use-hwaccel`
  - Enable hardware-accelerated decode during transcoding.
* - `--embedding-algorithm`
  - `internvideo2` or Cosmos-Embed1 variants (`cosmos-embed1-224p`, `-336p`, `-448p`).
* - `--generate-captions`, `--generate-previews`
  - Enable captioning and preview generation.
* - `--aesthetic-threshold`
  - Filter low-aesthetic clips when set.
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

For full options, run:

```bash
python -m ray_curator.examples.video.video_split_clip_example --help
```

---

## Performance Considerations

### Accelerate Pipeline Processing
Accelerate the pipeline with NVIDIA's NVDEC/NVENC by selecting the appropriate decoder and encoder options.

```{note}
Not all GPUs support NVENC (`h264_nvenc`). Verify your GPU supports NVENC before configuring the following parameters.
```

```{list-table}
:header-rows: 1

* - Parameter
  - Description
  - Default Value
* - `--transnetv2-frame-decoder-mode`
  - Choose between `ffmpeg_cpu`, `ffmpeg_gpu`, or `pynvc` for frame decoding in TransNetV2 splitting.
  - `pynvc`
* - `ClipTranscodingStage`'s `encoder`
  - Specifies the encoder used for transcoding clips. Can be set to either `libopenh264` or `h264_nvenc`. If you choose to use `h264_nvenc`, ensure that your GPU supports the hardware encoder.
  - `libopenh264`
* - `--transcode-use-hwaccel`
  - Enable hardware acceleration during transcoding. With `--transcode-encoder h264_nvenc`, the pipeline uses NVENC.
  - N/A
```

### Reduce Memory Requirements

To reduce VRAM usage below 38 GB:

1. Set `--captioning-batch-size 1`.
2. Enable `--captioning-use-fp8-weights`.

We have observed around 21 GB when both are set.