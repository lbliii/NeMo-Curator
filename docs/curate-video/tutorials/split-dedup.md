---
description: "End-to-end workflow tutorial covering the video curation process from splitting through semantic deduplication (Ray/Python)"
categories: ["video-curation"]
tags: ["workflow", "pipeline", "video-splitting", "deduplication", "semantic", "ray"]
personas: ["mle-focused", "data-scientist-focused"]
difficulty: "intermediate"
content_type: "tutorial"
modality: "video-only"

---

(video-tutorials-split-dedup)=
# Split and Deduplicate Workflow

Learn how to run the splitting pipeline to generate clips and embeddings, then remove near-duplicate clips using semantic deduplication.

```{contents} Tutorial Steps:
:local:
:depth: 2
```

## Before You Start

- Complete the [Get Started guide](gs-video).
- Review:
  - [Splitting pipeline](video-pipelines-splitting)
  - [Semantic Deduplication pipeline](video-pipelines-dedup)

---

## 1. Generate Clips and Embeddings

Run the splitting example. Set `DATA_DIR`, `OUT_DIR`, and `MODEL_DIR` first.

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

Embeddings are written under `$OUT_DIR/iv2_embd_parquet/` (or `ce1_embd_parquet/` if using Cosmos-Embed1).

---

## 2. Run Semantic Deduplication

Use KMeans clustering followed by Pairwise similarity on the parquet embeddings.

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
        embedding_dim=512,
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

---

## 3. Inspect Results

- KMeans outputs per-cluster partitions under `${OUTPUT_DIR}/kmeans/`.
- Pairwise outputs per-cluster similarity files under `${OUTPUT_DIR}/pairwise/` with columns including `id`, `max_id`, and `cosine_sim_score`.
- Use these to decide keep/remove policies or downstream sampling.

```{note}
Sharding/export for training is not covered here.
```
