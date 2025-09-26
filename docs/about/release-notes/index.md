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

This major release represents a fundamental architecture shift from Dask to Ray, expanding NeMo Curator to support multimodal data curation with new video and audio capabilities. This refactor enables unified backend processing, better heterogeneous computing support, and enhanced autoscaling for dynamic workloads.

## Installation Updates

### New Docker Container
- **Net-new Docker container**: Updated Docker infrastructure with CUDA 12.8.1 and Ubuntu 24.04 base
- **UV source installations**: Integrated UV package manager (v0.8.22) for faster dependency management
- **PyPI improvements**: Enhanced PyPI installation with modular extras (`[cuda12x]`, `[all]`, `[image]`, `[audio]`, `[video]`)
- **Docker file to build own image**: Simplified Dockerfile structure for custom container builds with FFmpeg support

## Video Modality

NeMo Curator now supports comprehensive video data curation with distributed processing capabilities:

- **Ray-based distributed architecture**: Scalable video processing with autoscaling support
- **Pipeline stages**: Modular video processing stages with configurable resources
- **Execution modes**: Support for both streaming and batch processing modes
- **High-throughput processing**: Optimized for large-scale video corpora with efficient data flow

## Audio Modality

New audio curation capabilities for speech data processing:

- **ASR inference**: Automatic speech recognition using NeMo Framework pretrained models
- **Quality assessment**: Word Error Rate (WER) and Character Error Rate (CER) calculation
- **Speech metrics**: Duration analysis and speech rate metrics (words/characters per second)
- **Text integration**: Seamless integration with text curation workflows via `AudioToDocumentStage`
- **Manifest support**: JSONL manifest format for audio file management

## Text & Image Refactors

### Text Refactors
- **Ray backend migration**: Complete transition from Dask to Ray for distributed text processing
- **Task-centric architecture**: New `Task`-based processing model for finer-grained control
- **Pipeline redesign**: Updated `ProcessingStage` and `Pipeline` architecture with resource specification
- **Fuzzy deduplication improvements**: Enhanced `FuzzyDeduplicationWorkflow` with Ray integration

### Image Refactors  
- **Pipeline-based architecture**: Transitioned from legacy `ImageTextPairDataset` to modern stage-based processing with `ImageReaderStage`, `ImageEmbeddingStage`, and filter stages
- **DALI-based image loading**: New `ImageReaderStage` uses NVIDIA DALI for high-performance WebDataset tar shard processing with GPU/CPU fallback
- **Modular processing stages**: Separate stages for embedding generation (`ImageEmbeddingStage`), aesthetic filtering (`ImageAestheticFilterStage`), and NSFW filtering (`ImageNSFWFilterStage`)
- **Task-based data flow**: Images processed as `ImageBatch` tasks containing `ImageObject` instances with metadata, embeddings, and classification scores

## Core Refactors

### Pipelines
- **New Pipeline API**: Ray-based pipeline execution with `BaseExecutor` interface
- **Multiple backends**: Support for Xenna, Ray Actor Pool, and Ray Data execution backends
- **Resource specification**: Configurable CPU and GPU memory requirements per stage
- **Stage composition**: Improved stage validation and execution orchestration

### Stages
- **ProcessingStage redesign**: Generic `ProcessingStage[X, Y]` base class with type safety
- **Resource requirements**: Built-in resource specification for CPU and GPU memory
- **Backend adapters**: Stage adaptation layer for different Ray orchestration systems
- **Input/output validation**: Enhanced type checking and data validation

## Tutorial Refactors

### Refactored Tutorials
- **Text tutorials**: Updated all text curation tutorials to use new Ray-based API
- **Image tutorials**: Migrated image processing tutorials to unified backend
- **Audio tutorials**: New comprehensive audio curation tutorial suite
- **Video tutorials**: Complete video processing tutorial documentation

### New Tutorial Categories
- **Multimodal workflows**: Cross-modality data curation examples
- **Pipeline customization**: Advanced configuration and customization guides
- **Performance optimization**: Best practices for large-scale processing

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

### Enhanced Documentation
- **Local preview capability**: Improved documentation build system with local preview support
- **Modality-specific guides**: Comprehensive documentation for each supported modality
- **API reference**: Complete API documentation with type annotations and examples
- **Deployment guides**: Updated installation and deployment documentation for all environments

### New Documentation Features
- **Interactive examples**: Enhanced code examples with executable snippets
- **Performance benchmarks**: Detailed performance metrics and scaling guidelines
- **Troubleshooting guides**: Comprehensive troubleshooting and FAQ sections

---

## Migration Guide

For users upgrading from previous versions, see our [Migration Guide](../migration-guide.md) for detailed instructions on updating your existing pipelines to the new Ray-based architecture.

## What's Next

The next release will focus on completing the refactor of Generation, PII, and Blending & Shuffling features, along with additional performance optimizations and new modality support.

