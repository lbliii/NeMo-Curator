---
description: "Guide to sharding pipeline for organizing processed video clips into training-ready datasets with text embeddings"
categories: ["video-curation"]
tags: ["sharding", "embedding", "dataset", "training", "t5-encoder", "webdataset", "pipeline"]
personas: ["mle-focused", "data-scientist-focused"]
difficulty: "intermediate"
content_type: "tutorial"
modality: "video-only"

---

(video-pipelines-sharding)=

# Sharding Pipeline

```{image} ../../about/concepts/video/_images/video-pipeline-diagram.png
:alt: Video Pipeline Diagram
```

The splitting pipeline is the second of two video curation pipelines in NeMo Curator. It performs the following stages:

1. **Text Embedding**: Creates a text embedding for each caption using a T5 encoder.
2. **Dataset Creation**: Shards the dataset into a format that can be consumed during training of a video foundation model.

This pipeline produces a dataset that can then be used for training a video AI model.

---

## Use Cases

- Generating a complete dataset for generative video model fine-tuning.

---

## Prerequisites

Before you can use the sharding pipeline, make sure that you have:

- Completed the {ref}`gs-video` guide.
- Generated clips using the {ref}`video-pipelines-splitting`.

---

## Run the NeMo Curator Video Sharding Pipeline

The following setup allows you to process video clips either from a local directory or from cloud storage, creating a dataset ready for training your video AI model.

### With Clips Stored Locally

If the data is located at `~/nemo_curator_local_workspace/output_clips`, run the following command:

```bash
mkdir -p ~/nemo_curator_local_workspace/output_dataset

video_curator launch \
    --image-name nemo_video_curator --image-tag 1.0.0 \
    --no-mount-s3-creds \
    -- python3 -m nemo_curator.video.pipelines.video.run_pipeline shard \
    --input-clip-path /config/output_clips \
    --output-dataset-path /config/output_dataset \
    --annotation-version v0
```

This command uses `video_curator launch` to run the sharding pipeline (`python3 -m nemo_curator.video.pipelines.video.run_pipeline shard`) inside the Docker container.

### With Clips Stored in Cloud Storage

If your data is stored on cloud storage, replace the path with an S3 path and remove the `--no-mount-s3-creds` flag.

```bash
video_curator launch \
    --image-name nemo_video_curator --image-tag 1.0.0 \
    -- python3 -m nemo_curator.video.pipelines.video.run_pipeline shard \
    --input-clip-path s3://video-storage/clips/ \
    --output-dataset-path s3://video-storage/webdataset/ \
    --annotation-version v0
```

The output dataset path will have the following structure:

```
~/nemo_curator_local_workspace/output_dataset/
    v0/
        resolution_720/
            aspect_ratio_16_9/
                frames_121_255/
                    metas/
                        part_000000/
                            000000.tar
                    t5_xxl/
                        part_000000/
                            000000.tar
                    video/
                        part_000000/
                            000000.tar
                frames_1024_inf/
                    metas/
                        part_000000/
                            000000.tar
                    t5_xxl/
                        part_000000/
                            000000.tar
                    video/
                        part_000000/
                            000000.tar
```

```{note}
The exact folder names will vary based on the resolutions and aspect ratios supplied in the original videos. By default, we will drop clips that have lower resolution than 720p.
```

```{list-table} Directory Descriptions
:widths: 20 80
:header-rows: 1

* - Directory
  - Description
* - resolution_720/aspect_ratio_16_9/
  - All files at 720p resolution with a 16:9 aspect ratio. Other folders will be created and populated with videos at different resolutions and aspect ratios. The exact bins can be found at `nemo_curator.video.data_utils.dimensions.ResolutionAspectRatioFramesBinsSpec`.
* - frames_121_255/
  - The clips sliced with frames 121 to 255.
* - metas/
  - A tarred version of .json files containing metadata for each clip.
* - t5_xxl/
  - A tarred version of .pickle files for the text embedding of each caption.
* - video/
  - A tarred version of .mp4 files for each clip.
```

---

## Key Parameters

Here are a few key parameters shown in this example:

```{list-table} Parameters
:widths: 30 70
:header-rows: 1

* - Parameter
  - Description
* - `--image-name nemo_video_curator` and `--image-tag 1.0.0`
  - Specifies the Docker image and tag to use.
* - `--no-mount-s3-creds`
  - This flag prevents the S3 credentials from being mounted in the container. It's useful when you don't have S3 credentials and your data is stored locally.
* - `--input-clip-path`
  - Specifies the path inside the container or on cloud storage that holds all the clips, captions, and other metadata to be combined into a single dataset. If you need to access local data, the directory `~/nemo_curator_local_workspace/` is mounted to `/config/`.
* - `--output-dataset-path`
  - Indicates where the output dataset will be stored. It functions similarly to `--input-clip-path` in terms of mounts.
* - `--annotation-version`
  - Defines the annotation version to use for the clip metadata. This helps in scenarios where another process updates the clip metadata (e.g., captions) to a newer version (e.g., v1) after the splitting pipeline produced version v0.
```