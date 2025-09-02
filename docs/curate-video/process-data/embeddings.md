---
description: "Generate clip-level embeddings using Cosmos-Embed1 or InternVideo2"
categories: ["video-curation"]
tags: ["embeddings", "cosmos-embed1", "internvideo2", "video"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "howto"
modality: "video-only"
---

<!-- markdownlint-disable MD041 -->

(video-process-embeddings)=

# Embeddings {#video-process-embeddings}

Create frame sequences and compute clip-level embeddings for search, QA, and duplicate removal.

## How It Works

Embedding in NeMo Curator is a two-stage process per model:

1. Frame creation stage prepares model-specific frame tensors from earlier extracted frames.
2. Embedding stage runs the model, produces a clip-level vector, and frees intermediate frames to reduce memory.

### Data Flow and Keys

- Input frames: `clip.extracted_frames[sequence-<target_fps>]` (from the frame extraction stages). Refer to [Frame Extraction](video-process-frame-extraction).
- Model-specific frames:
  - Cosmos-Embed1: `clip.cosmos_embed1_frames`
  - InternVideo2: `clip.intern_video_2_frames`
- Embeddings:
  - Cosmos-Embed1: `clip.cosmos_embed1_embedding`
  - InternVideo2: `clip.intern_video_2_embedding`
- Optional text verification result (when you pass `texts_to_verify`):
  - `clip.cosmos_embed1_text_match` or `clip.intern_video_2_text_match` → tuple of the best-matching text and probability

If the source `target_fps` does not yield enough frames for a model’s required frame count, the frame creation stage automatically re-extracts frames at higher rates (doubling up to 20 FPS) using the clip buffer.

```{note}
Embeddings can be written out by downstream writers. For example, `ClipWriterStage` compacts clip embeddings to buffers for Parquet output, then clears large in-memory fields.
```

## Cosmos-Embed1

```python
from nemo_curator.stages.video.embedding.cosmos_embed1 import (
    CosmosEmbed1FrameCreationStage,
    CosmosEmbed1EmbeddingStage,
)

frames = CosmosEmbed1FrameCreationStage(
    model_dir="/models",
    variant="224p",  # or 336p, 448p
    target_fps=2.0,
    verbose=True,
)
embed = CosmosEmbed1EmbeddingStage(
    model_dir="/models",
    variant="224p",
    gpu_memory_gb=20.0,
    verbose=True,
)
```

### Cosmos-Embed1 Parameters

#### Frame Creation (`CosmosEmbed1FrameCreationStage`)

```{list-table} Cosmos-Embed1 frame creation parameters
:header-rows: 1
:widths: 22 12 12 54

* - Parameter
  - Type
  - Default
  - Description
* - `model_dir`
  - str
  - `"models/cosmos_embed1"`
  - Directory for model utilities and configs used to format input frames.
* - `variant`
  - {"224p", "336p", "448p"}
  - `"336p"`
  - Resolution preset that controls the model’s expected input size.
* - `target_fps`
  - float
  - 2.0
  - Source sampling rate used to select frames; may re-extract at higher FPS if needed.
* - `num_cpus`
  - int
  - 3
  - CPU cores used when on-the-fly re-extraction is required.
* - `verbose`
  - bool
  - `False`
  - Log per-clip decisions and re-extraction messages.
```

#### Embedding (`CosmosEmbed1EmbeddingStage`)

```{list-table} Cosmos-Embed1 embedding parameters
:header-rows: 1
:widths: 22 12 12 54

* - Parameter
  - Type
  - Default
  - Description
* - `model_dir`
  - str
  - `"models/cosmos_embed1"`
  - Directory for model weights; downloaded on each node if missing.
* - `variant`
  - {"224p", "336p", "448p"}
  - `"336p"`
  - Resolution preset used by the model weights.
* - `gpu_memory_gb`
  - int
  - 20
  - Approximate GPU memory reservation per worker.
* - `texts_to_verify`
  - list[str] | None
  - `None`
  - Optional text prompts to score against the clip embedding.
* - `verbose`
  - bool
  - `False`
  - Log setup and per-clip outcomes.
```

### Cosmos-Embed1 Procedure

1. Add `CosmosEmbed1FrameCreationStage` to transform extracted frames into model-ready tensors.
2. Add `CosmosEmbed1EmbeddingStage` to generate `clip.cosmos_embed1_embedding` and optional `clip.cosmos_embed1_text_match`.

### Cosmos-Embed1 Outputs

- `clip.cosmos_embed1_frames` → temporary tensors used by the embedding stage
- `clip.cosmos_embed1_embedding` → final clip-level vector (NumPy array)
- Optional: `clip.cosmos_embed1_text_match`

## InternVideo2

```python
from nemo_curator.stages.video.embedding.internvideo2 import (
    InternVideo2FrameCreationStage,
    InternVideo2EmbeddingStage,
)

frames = InternVideo2FrameCreationStage(
    model_dir="/models",
    target_fps=2.0,
    verbose=True,
)
embed = InternVideo2EmbeddingStage(
    model_dir="/models",
    gpu_memory_gb=20.0,
    verbose=True,
)
```

### InternVideo2 Parameters

#### Frame Creation (`InternVideo2FrameCreationStage`)

```{list-table} InternVideo2 frame creation parameters
:header-rows: 1
:widths: 22 12 12 54

* - Parameter
  - Type
  - Default
  - Description
* - `model_dir`
  - str
  - `"InternVideo2"`
  - Directory for model utilities used to format input frames.
* - `target_fps`
  - float
  - 2.0
  - Source sampling rate used to select frames; may re-extract at higher FPS if needed.
* - `verbose`
  - bool
  - `False`
  - Log re-extraction and per-clip messages.
```

#### Embedding (`InternVideo2EmbeddingStage`)

```{list-table} InternVideo2 embedding parameters
:header-rows: 1
:widths: 22 12 12 54

* - Parameter
  - Type
  - Default
  - Description
* - `model_dir`
  - str
  - `"InternVideo2"`
  - Directory for model weights; downloaded on each node if missing.
* - `gpu_memory_gb`
  - float
  - 10.0
  - Approximate GPU memory reservation per worker.
* - `num_gpus_per_worker`
  - float
  - 1.0
  - GPUs reserved per worker for embedding.
* - `texts_to_verify`
  - list[str] | None
  - `None`
  - Optional text prompts to score against the clip embedding.
* - `verbose`
  - bool
  - `False`
  - Log setup and per-clip outcomes.
```

### InternVideo2 Procedure

1. Add `InternVideo2FrameCreationStage` to transform extracted frames into model-ready tensors.
2. Add `InternVideo2EmbeddingStage` to generate `clip.intern_video_2_embedding` and optional `clip.intern_video_2_text_match`.

### InternVideo2 Outputs

- `clip.intern_video_2_frames` → temporary tensors used by the embedding stage
- `clip.intern_video_2_embedding` → final clip-level vector (NumPy array)
- Optional: `clip.intern_video_2_text_match`

<!-- end -->
