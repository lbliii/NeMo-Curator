---
description: "Release notes and version history for NeMo Curator platform updates and new features"
categories: ["reference"]
tags: ["release-notes", "changelog", "updates"]
personas: ["data-scientist-focused", "mle-focused", "admin-focused", "devops-focused"]
difficulty: "reference"
content_type: "reference"
modality: "universal"
---

(about-release-notes)=

# Release Notes 25.09

This major release represents a fundamental architecture shift from Dask to Ray, expanding NeMo Curator to support multimodal data curation with new [video](../../curate-video/index.md) and [audio](../../curate-audio/index.md) capabilities. This refactor enables unified backend processing, better heterogeneous computing support, and enhanced autoscaling for dynamic workloads.

## Installation Updates

### New Docker Container

- **New Docker container**: Updated Docker infrastructure with CUDA 12.8.1 and Ubuntu 24.04 base
- **UV source installations**: Integrated UV package manager (v0.8.22) for faster dependency management
- **PyPI improvements**: Enhanced PyPI installation with modular extras (`[cuda12x]`, `[all]`, `[image]`, `[audio]`, `[video]`)
- **Docker file to build own image**: Simplified Dockerfile structure for custom container builds with FFmpeg support

For complete installation instructions, see [Installation](../../admin/installation.md).

## Video Modality

NeMo Curator now supports comprehensive [video data curation](../../curate-video/index.md) with distributed processing capabilities:

- **Ray-based distributed architecture**: Scalable video processing with [autoscaling support](../concepts/video/architecture.md)
- **Pipeline stages**: Modular [video processing stages](../../curate-video/process-data/index.md) with configurable resources
- **Execution modes**: Support for both streaming and batch processing modes
- **High-throughput processing**: Optimized for large-scale video corpora with efficient data flow

Get started with [video curation tutorials](../../curate-video/tutorials/index.md).

## Audio Modality

New [audio curation capabilities](../../curate-audio/index.md) for speech data processing:

- **ASR inference**: [Automatic speech recognition](../../curate-audio/process-data/asr-inference/index.md) using NeMo Framework pretrained models
- **Quality assessment**: [Word Error Rate (WER) and Character Error Rate (CER)](../../curate-audio/process-data/quality-assessment/index.md) calculation
- **Speech metrics**: [Duration analysis and speech rate metrics](../../curate-audio/process-data/audio-analysis/index.md) (words/characters per second)
- **Text integration**: Seamless integration with [text curation workflows](../../curate-audio/process-data/text-integration/index.md) via `AudioToDocumentStage`
- **Manifest support**: JSONL manifest format for audio file management

Explore [audio curation tutorials](../../curate-audio/tutorials/index.md).

## Text & Image Refactors

### Text Refactors

- **Ray backend migration**: Complete transition from Dask to Ray for distributed [text processing](../../curate-text/index.md)
- **Task-centric architecture**: New `Task`-based processing model for finer-grained control
- **Pipeline redesign**: Updated `ProcessingStage` and `Pipeline` architecture with resource specification
- **Fuzzy deduplication improvements**: Enhanced [fuzzy deduplication workflow](../../curate-text/process-data/fuzzy-deduplication.md) with Ray integration

### Image Refactors

- **Pipeline-based architecture**: Transitioned from legacy `ImageTextPairDataset` to modern [stage-based processing](../../curate-images/index.md) with `ImageReaderStage`, `ImageEmbeddingStage`, and filter stages
- **DALI-based image loading**: New `ImageReaderStage` uses NVIDIA DALI for high-performance WebDataset tar shard processing with GPU/CPU fallback
- **Modular processing stages**: Separate stages for [embedding generation](../../curate-images/process-data/embeddings.md), [aesthetic filtering](../../curate-images/process-data/aesthetic-filtering.md), and [NSFW filtering](../../curate-images/process-data/nsfw-filtering.md)
- **Task-based data flow**: Images processed as `ImageBatch` tasks containing `ImageObject` instances with metadata, embeddings, and classification scores

Learn more about [image curation](../../curate-images/index.md).

## Core Refactors

### Pipelines

- **New Pipeline API**: Ray-based pipeline execution with `BaseExecutor` interface
- **Multiple backends**: Support for [Xenna, Ray Actor Pool, and Ray Data execution backends](../../reference/infrastructure/execution-backends.md)
- **Resource specification**: Configurable CPU and GPU memory requirements per stage
- **Stage composition**: Improved stage validation and execution orchestration

### Stages

- **ProcessingStage redesign**: Generic `ProcessingStage[X, Y]` base class with type safety
- **Resource requirements**: Built-in resource specification for CPU and GPU memory
- **Backend adapters**: Stage adaptation layer for different Ray orchestration systems
- **Input/output validation**: Enhanced type checking and data validation

## Tutorials

### Refactored

- **Text tutorials**: Updated all [text curation tutorials](https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials/text) to use new Ray-based API
- **Image tutorials**: Migrated [image processing tutorials](https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials/image) to unified backend

## Net-New

- **Audio tutorials**: New [audio curation tutorials](https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials/audio)
- **Video tutorials**: New [video processing tutorials](https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials/video)

For all tutorial content, refer to the [tutorials directory](https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials) in the NeMo Curator GitHub repository.

## Known Limitations (Pending Refactor in Future Release)

### Generation

- **Synthetic data generation**: Synthetic text generation features are being refactored for Ray compatibility
- **Hard negative mining**: Retrieval-based data generation workflows under development

### PII

- **PII processing**: Personal Identifiable Information removal tools are being updated for Ray backend
- **Privacy workflows**: Enhanced privacy-preserving data curation capabilities in development

### Blending & Shuffling

- **Data blending**: Multi-source dataset blending functionality being refactored
- **Dataset shuffling**: Large-scale data shuffling operations under development

## Docs Refactor

- **Local preview capability**: Improved documentation build system with local preview support
- **Modality-specific guides**: Comprehensive documentation for each supported modality ([text](../../curate-text/index.md), [image](../../curate-images/index.md), [audio](../../curate-audio/index.md), [video](../../curate-video/index.md))
- **API reference**: Complete [API documentation](../../apidocs/index.rst) with type annotations and examples
- **Deployment guides**: Updated [installation](../../admin/installation.md) and [deployment documentation](../../admin/deployment/index.md) for all environments

---

## Migration Guide

TBD

## What's Next

The next release will focus on completing the refactor of Generation, PII, and Blending & Shuffling features, along with additional performance optimizations and new modality support.