---
description: "Guide to semantic deduplication pipeline for removing duplicate video clips using clustering and similarity comparison"
categories: ["video-curation"]
tags: ["deduplication", "clustering", "semantic-dedup", "pipeline", "video-processing", "similarity"]
personas: ["mle-focused", "data-scientist-focused"]
difficulty: "intermediate"
content_type: "tutorial"
modality: "video-only"

---

(video-pipelines-dedup)=

# Deduplication Pipeline

The deduplication pipeline implements **Semantic Deduplication** to remove duplicate clips from the dataset. It performs the following stages:

1. **Clustering**: Clusters the clips into groups based on their similarity.
2. **Pairwise Comparison**: Compares each clip in a cluster to every other clip in the cluster.
3. **Removal**: Removes clips within clusters that are similar to each other.

---

## Use Cases

- Removing duplicate clips from a dataset that are similar to each other.

---

## Prerequisites

- Completed the {ref}`gs-video` guide.
- Generated clips using the {ref}`video-pipelines-splitting`.

---

## Run the NeMo Curator Video Deduplication Pipeline

The following setup allows you to process video clips either from a local directory or from cloud storage, creating a dataset ready for training your video AI model.

### With Clips Stored Locally

If the data (output of splitting pipeline) is located at `~/nemo_curator_local_workspace/output_dataset`, run the following command:

```bash
video_curator launch \
    --image-name nemo_video_curator --image-tag 1.0.0 \
    --env text_curator \
    --no-mount-s3-creds -- python3 -m nemo_curator.video.pipelines.video.run_pipeline dedup \
    --input-embeddings-path /config/output_dataset/iv2_embd \
    --output-path /config/output_dataset/semantic_dedup \
    --n-clusters 1000 \
    --eps-thresholds 0.01 0.001 \
    --eps-to-extract 0.01 \
    --which-to-keep hard \
    --files-per-partition 1000
```

This command uses `video_curator launch` to run the deduplication pipeline (`python3 -m nemo_curator.video.pipelines.video.run_pipeline dedup`) inside the Docker container.

### With Clips Stored in Cloud Storage

If your data is stored on cloud storage, replace the path with an S3 path and remove the `--no-mount-s3-creds` flag.

```bash
video_curator launch \
    --image-name nemo_video_curator --image-tag 1.0.0 \
    --env text_curator \
    -- python3 -m nemo_curator.video.pipelines.video.run_pipeline dedup \
    --input-embeddings-path s3://video-storage/iv2_embd/ \
    --output-path s3://video-storage/semantic_dedup/ \
    --n-clusters 1000 \
    --eps-thresholds 0.01 0.001 \
    --eps-to-extract 0.01 \
    --which-to-keep hard \
    --files-per-partition 1000
```

## Key Parameters

```{list-table} Parameters
:header-rows: 1
:widths: 30 70

* - Parameter
  - Description
* - `--input-embeddings-path`
  - Specifies the path to the embeddings file.
* - `--output-path`
  - Specifies the path to the output file.
* - `--n-clusters`
  - Specifies the number of clusters to create.
* - `--eps-thresholds`
  - Specifies the epsilon thresholds to use for the clustering. This is a list of two values.
* - `--eps-to-extract`
  - Specifies the epsilon value to use for the extraction.
* - `--which-to-keep`
  - Specifies which clips to keep. Options are `hard`, `soft`, or `random`.
* - `--files-per-partition`
  - Specifies the number of files per partition. Each file is 1 KB, and we want each partition to be ~512 MB to ~2 GB so that's ~250k to ~1M files per partition.
```
