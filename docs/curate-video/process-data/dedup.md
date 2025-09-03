---
description: "Remove near-duplicate clips using semantic clustering and pairwise similarity"
categories: ["video-curation"]
tags: ["deduplication", "semantic", "pairwise", "kmeans", "video"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "howto"
modality: "video-only"
---

(video-process-dedup)=

# Duplicate Removal

Use clip-level embeddings to identify and remove near-duplicate video clips so your dataset remains compact, diverse, and efficient to train on.

## How it Works

Duplicate removal operates on clip-level embeddings produced during processing:

1. **Inputs**
   - Parquet batches from `ClipWriterStage` under `iv2_embd_parquet/` or `ce1_embd_parquet/`
   - Columns: `id`, `embedding`

2. **Outputs**
   - Cluster: `KMeansStage` partitions embeddings and writes centroid distances (for example, `cosine_dist_to_cent`).
   - Pairwise: `PairwiseStage` computes within-cluster similarity on GPU and, for each clip, emits `max_id` and `cosine_sim_score`. Ranking controls whether to prefer outliers ("hard") or representatives ("easy").
   - Identify: `IdentifyDuplicatesStage` filters pairs with `cosine_sim_score >= 1.0 - eps` and writes Parquet files of duplicate `id`s for removal during export.

## Quickstart

Use the generic semantic duplicate-removal stages with clip embeddings written to parquet.

```python
from nemo_curator.stages.deduplication.semantic.kmeans import KMeansStage
from nemo_curator.stages.deduplication.semantic.pairwise import PairwiseStage
from nemo_curator.stages.deduplication.semantic.ranking import RankingStrategy
from nemo_curator.stages.deduplication.semantic.identify_duplicates import IdentifyDuplicatesStage

# Example: cluster embeddings, compute pairwise within clusters, then write duplicate IDs
kmeans = KMeansStage(
    n_clusters=1000,
    id_field="id",
    embedding_field="embedding",
    input_path="/path/to/embeddings/",   # parquet files with id + embedding
    output_path="/path/to/kmeans_out/",
    input_filetype="parquet",
)

pairwise = PairwiseStage(
    id_field="id",
    embedding_field="embedding",
    input_path="/path/to/kmeans_out/",
    output_path="/path/to/pairwise_out/",
    ranking_strategy=RankingStrategy.metadata_based(
        metadata_cols=["cosine_dist_to_cent", "id"],
        ascending=[True, True],
    ),
)

identify = IdentifyDuplicatesStage(
    output_path="/path/to/duplicates/",  # writes parquet of duplicate ids
    eps=0.1,  # keep pairs with cosine_sim_score >= 0.9
)
```

Input format: Parquet with columns `id` and `embedding` (produced by the video pipeline’s embedding stages and writer). Duplicate removal operates at the clip level using these embeddings. The `IdentifyDuplicatesStage` writes Parquet files containing duplicate `id`s; perform removal by filtering out rows whose `id` appears in those files during export.

```{seealso}
Embeddings are written by the [`ClipWriterStage`](video-save-export) under `iv2_embd_parquet/` or `ce1_embd_parquet/`. For a runnable workflow, refer to the [Split and Remove Duplicates Workflow](video-tutorials-split-dedup).
```

## Parameters

::::{tab-set}

:::{tab-item} KMeansStage

```{list-table} KMeansStage (semantic clustering)
:header-rows: 1

* - Parameter
  - Description
* - `n_clusters`
  - Number of clusters for K‑means (for example, 1,000+ for multi‑million clip sets).
* - `id_field`
  - Column name containing clip IDs (for example, `"id"`).
* - `embedding_field`
  - Column with vector data (for example, `"embedding"`).
* - `input_path`
  - Path to Parquet embeddings directory from the writer.
* - `output_path`
  - Directory for K‑means outputs (sharded by cluster).
* - `input_filetype`
  - Use `"parquet"` for video embeddings.
* - `embedding_dim`
  - Embedding dimension (InternVideo2: 512; Cosmos‑Embed1 varies by variant).
```

:::

:::{tab-item} PairwiseStage

```{list-table} PairwiseStage (within‑cluster similarity)
:header-rows: 1

* - Parameter
  - Description
* - `which_to_keep`
  - `"hard"` keeps outliers far from centroid; `"easy"` keeps nearest to centroid; `"random"` ignores distance.
* - `sim_metric`
  - `"cosine"` (default) or `"l2"` affects centroid distances and ranking.
* - `ranking_strategy`
  - Optional explicit ranking (overrides switches). Use `RankingStrategy.metadata_based([...])`.
* - `pairwise_batch_size`
  - Batch size for GPU pairwise computation (default `1024`). Increase with available memory.
* - `embedding_dim`
  - Embedding dimension for memory estimates and batching.
* - `read_kwargs` / `write_kwargs`
  - Storage options for Parquet I/O, including cloud credentials.
```

:::

:::{tab-item} IdentifyDuplicatesStage

```{list-table} IdentifyDuplicatesStage (filter pairs)
:header-rows: 1

* - Parameter
  - Description
* - `eps`
  - Similarity tolerance. Keeps pairs with `cosine_sim_score >= 1.0 - eps` (for example, `0.1` → similarity ≥ 0.9).
* - `output_path`
  - Directory for Parquet files with duplicate `id`s.
* - `read_kwargs` / `write_kwargs`
  - Storage options for reading pairwise outputs and writing final duplicate IDs.
```

:::

::::

## Tuning Guidelines

- Start with `n_clusters` in the low thousands; increase for large datasets to bound per‑cluster size.
- Set `embedding_dim` to match your model (InternVideo2: 512). Incorrect dimensions can cause memory issues.
- Use `which_to_keep="hard"` to favor diversity (outliers). Use `"easy"` to keep more representative clips.
- Increase `pairwise_batch_size` when GPU memory allows to improve throughput.

## Troubleshooting

- "No data found for cluster": Confirm K‑means output path and storage credentials.
- Out‑of‑memory during pairwise: Lower `pairwise_batch_size` and verify `embedding_dim`.
- Empty duplicate outputs: Reduce `eps` (for example, `0.2` → similarity ≥ 0.8) or check that embeddings use the same model across clips.

<!-- end -->
