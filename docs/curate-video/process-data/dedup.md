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

## How it Works

<!-- insert content here -->

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

Input format: parquet with columns `id` and `embedding` (produced by the video pipeline’s embedding stages and writer). Duplicate removal operates at the clip level using these embeddings. The `IdentifyDuplicatesStage` writes parquet files containing duplicate `id`s; perform removal by filtering out rows whose `id` appears in those files during export.

<!-- end -->
