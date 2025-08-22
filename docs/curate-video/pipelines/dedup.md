---
description: "Guide to semantic deduplication using KMeans clustering and pairwise similarity over clip embeddings"
categories: ["video-curation"]
tags: ["deduplication", "clustering", "semantic-dedup", "pipeline", "video-processing", "similarity", "ray"]
personas: ["mle-focused", "data-scientist-focused"]
difficulty: "intermediate"
content_type: "tutorial"
modality: "video-only"

---

(video-pipelines-dedup)=

# Deduplication Pipeline

The semantic deduplication pipeline removes near-duplicate clips based on embeddings generated in the splitting pipeline. It performs the following stages:

1. **KMeans clustering (RAFT)**: Assigns clip embeddings to centroids and writes partitioned outputs by cluster.
2. **Pairwise similarity (per cluster)**: Computes pairwise cosine similarity within each cluster in batches and writes removal candidates with scores.
3. **Ranking/keep policy**: Ranks by distance to centroid (keep easy vs keep hard) or random; selects which items to keep.

---

## Use Cases

- Removing duplicate clips from a dataset that are similar to each other.

---

## Prerequisites

- Completed the {ref}`gs-video` guide.
- Generated clips using the {ref}`video-pipelines-splitting`.

---

## Run the Semantic Deduplication Pipeline (Python)

Inputs: Parquet embeddings produced by the splitting pipeline, for example `$OUT_DIR/iv2_embd_parquet/` with columns `id` and `embedding`.

```python
from ray_curator.pipeline import Pipeline
from ray_curator.backends.xenna import XennaExecutor
from ray_curator.stages.deduplication.semantic.kmeans import KMeansStage
from ray_curator.stages.deduplication.semantic.pairwise import PairwiseStage

INPUT_PARQUET = f"{OUT_DIR}/iv2_embd_parquet"  # or s3://...
OUTPUT_DIR = f"{OUT_DIR}/semantic_dedup"

pipe = Pipeline(name="video_semantic_dedup", description="KMeans + pairwise dedup")

pipe.add_stage(
    KMeansStage(
        n_clusters=1000,
        id_field="id",
        embedding_field="embedding",
        input_path=INPUT_PARQUET,
        output_path=f"{OUTPUT_DIR}/kmeans",
        input_filetype="parquet",
        embedding_dim=512,  # set if known to optimize grouping
        read_kwargs={"storage_options": None},
        write_kwargs={"storage_options": None},
    )
)

pipe.add_stage(
    PairwiseStage(
        id_field="id",
        embedding_field="embedding",
        input_path=f"{OUTPUT_DIR}/kmeans",
        output_path=f"{OUTPUT_DIR}/pairwise",
        which_to_keep="hard",   # or "easy" or "random"
        sim_metric="cosine",    # or "l2"
        pairwise_batch_size=1024,
        read_kwargs={"storage_options": None},
        write_kwargs={"storage_options": None},
    )
)

pipe.run(XennaExecutor())
```

## Key Parameters

```{list-table} Parameters
:header-rows: 1
:widths: 30 70

* - Parameter
  - Description
* - `n_clusters`
  - Number of clusters to create.
* - `which_to_keep`
  - Keep policy: `hard` (outliers) or `easy` (closest to centroid), or `random`.
* - `sim_metric`
  - Distance metric: `cosine` or `l2` (affects ranking strategy).
* - `pairwise_batch_size`
  - Batch size for pairwise similarity.
* - `read_kwargs` / `write_kwargs`
  - Pass `storage_options` for S3-compatible storage as needed.
```
