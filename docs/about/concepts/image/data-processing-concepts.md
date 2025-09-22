---
description: "Core concepts for processing image data including embedding generation, classification, filtering, and deduplication"
categories: ["concepts-architecture"]
tags: ["data-processing", "embedding", "classification", "filtering", "deduplication", "gpu-accelerated", "pipeline"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "concept"
modality: "image-only"
---

(about-concepts-image-data-processing)=

# Data Processing Concepts (Image)

This page covers the core concepts for processing image data in NeMo Curator.

## Embedding Generation

Image embeddings are vector representations of images, used for downstream tasks like classification, filtering, and deduplication.

- **ImageEmbeddingStage:** Uses CLIP ViT-L/14 model for high-quality embedding generation. Supports GPU acceleration, batching, and automatic CPU fallback.
- **Custom Embedding Stages:** You can subclass `ProcessingStage` to use your own model or preprocessing logic.
- **CLIP Integration:** Built-in CLIP model provides robust embeddings for aesthetic and NSFW classification.
- **Pipeline Integration:** Embedding generation integrates seamlessly into NeMo Curator's pipeline architecture.

**Example:**

```python
from nemo_curator.stages.image.embedders.clip_embedder import ImageEmbeddingStage

# Add to pipeline
pipeline.add_stage(ImageEmbeddingStage(
    model_dir="/path/to/models",
    model_inference_batch_size=32,
    num_gpus_per_worker=0.25,
    remove_image_data=False,
))
```

## Classification

Classification stages score and filter images based on their embeddings.

- **ImageAestheticFilterStage:** Predicts aesthetic scores (0–1) and filters images below a threshold.
- **ImageNSFWFilterStage:** Predicts NSFW probability (0–1) and filters images above a threshold.
- **Pipeline Integration:** Classification stages run efficiently after embedding generation in the same pipeline.

**Example:**

```python
from nemo_curator.stages.image.filters.aesthetic_filter import ImageAestheticFilterStage
from nemo_curator.stages.image.filters.nsfw_filter import ImageNSFWFilterStage

# Add to pipeline
pipeline.add_stage(ImageAestheticFilterStage(
    model_dir="/path/to/models",
    score_threshold=0.5,
    model_inference_batch_size=32,
))

pipeline.add_stage(ImageNSFWFilterStage(
    model_dir="/path/to/models", 
    score_threshold=0.5,
    model_inference_batch_size=32,
))
```

## Filtering

Filtering integrates with the classification stages, which automatically remove images that don't meet the configured thresholds.

- **Aesthetic Filtering:** Images with scores below `score_threshold` are automatically filtered out
- **NSFW Filtering:** Images with scores above `score_threshold` are automatically filtered out  
- **Pipeline Flow:** Filtering happens seamlessly as part of the stage processing

The filtering happens automatically within the stages - images that don't meet criteria are removed from the `ImageBatch` before passing to the next stage.

## Deduplication

Image deduplication removes duplicate images that have been pre-identified through external processes.

- **ImageDuplicatesRemovalStage:** Filters out images based on a list of duplicate IDs stored in Parquet files
- **ID-based Removal:** Uses image identifiers to remove duplicates rather than computing similarity
- **Pipeline Integration:** Runs after embedding and classification stages to remove identified duplicates

**Example:**

```python
from nemo_curator.stages.image.deduplication.removal import ImageDuplicatesRemovalStage

# Add to pipeline
pipeline.add_stage(ImageDuplicatesRemovalStage(
    removal_parquets_dir="/path/to/duplicate_ids",
    duplicate_id_field="id",
))
```

## Pipeline Flow

A typical image curation pipeline using NeMo Curator's stage-based architecture:

1. **Partition** tar files (`FilePartitioningStage`)
2. **Load** images from WebDataset (`ImageReaderStage`)
3. **Generate embeddings** (`ImageEmbeddingStage`)
4. **Filter by aesthetics** (`ImageAestheticFilterStage`)
5. **Filter NSFW content** (`ImageNSFWFilterStage`)
6. **Remove duplicates** (`ImageDuplicatesRemovalStage`) - optional

**Example:**

```python
from nemo_curator.stages.file_partitioning import FilePartitioningStage
from nemo_curator.stages.image.io.image_reader import ImageReaderStage
from nemo_curator.stages.image.embedders.clip_embedder import ImageEmbeddingStage
from nemo_curator.stages.image.filters.aesthetic_filter import ImageAestheticFilterStage
from nemo_curator.stages.image.filters.nsfw_filter import ImageNSFWFilterStage
from nemo_curator.stages.image.deduplication.removal import ImageDuplicatesRemovalStage

# Build pipeline
pipeline.add_stage(FilePartitioningStage(file_paths="/path/to/tars"))
pipeline.add_stage(ImageReaderStage())
pipeline.add_stage(ImageEmbeddingStage(model_dir="/path/to/models"))
pipeline.add_stage(ImageAestheticFilterStage(model_dir="/path/to/models", score_threshold=0.5))
pipeline.add_stage(ImageNSFWFilterStage(model_dir="/path/to/models", score_threshold=0.5))
# Optional: Remove duplicates if you have pre-identified duplicate IDs
# pipeline.add_stage(ImageDuplicatesRemovalStage(removal_parquets_dir="/path/to/duplicate_ids"))
```

This modular pipeline approach allows you to customize, reorder, or skip stages based on your workflow needs.
