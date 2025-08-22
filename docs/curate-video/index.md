---
description: "Comprehensive guide to Ray-based video curation with NeMo Curator including splitting and deduplication pipelines for large-scale processing"
categories: ["video-curation"]
tags: ["video-processing", "gpu-accelerated", "pipeline", "distributed", "ray", "splitting", "deduplication", "autoscaling"]
personas: ["mle-focused", "data-scientist-focused"]
difficulty: "intermediate"
content_type: "concept"
modality: "video-only"
---

(video-overview)=
# About Video Curation

Video curation is the process of taking long-form video content and dividing it into short, semantically consistent clips that can be filtered for your use case.
Depending on the use case, this can involve processing 100+ PB of videos.
To efficiently process this quantity of videos, NeMo Curator provides highly optimized curation pipelines.

## Use Cases

* Generating clips for video world model training
* Generating clips for generative video model fine-tuning
* Creating a rich video database for video retrieval applications

## Architecture

```{image} ../about/concepts/video/_images/video-pipeline-diagram.png
:alt: High-level outline of NeMo Curator's video curation architecture
```

This diagram provides a high-level outline of NeMo Curator's video curation architecture.
NeMo Curator offers a collection of pipelines that read/write video data and metadata from/to S3-compatible storage (or locally if the data is small enough).

These pipelines use Ray for multi-node, multi-GPU scaling, allowing us to stream the data through the pipeline efficiently. All computational stages are GPU-accelerated using state-of-the-art NVIDIA libraries to ensure maximum throughput.

Furthermore, the pipelines are optimized so that each stage has the appropriate number of workers to prevent bottlenecks. For example, in the splitting pipeline, the captioning stage is computationally intensive and has a lower throughput than other stages. To compensate, NeMo Curator's autoscaling system automatically creates more workers for the captioning stage, increasing its throughput and reducing bottlenecks.

---

## Introduction

Master the fundamentals of NeMo Curator and set up your video processing environment.

::::{grid} 1 1 1 2
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`database;1.5em;sd-mr-1` Concepts
:link: about-concepts-video
:link-type: ref
Learn about the architecture, stages, pipelines, and data flow for video curation
+++
{bdg-secondary}`stages`
{bdg-secondary}`pipelines`
{bdg-secondary}`ray`
:::

:::{grid-item-card} {octicon}`rocket;1.5em;sd-mr-1` Get Started
:link: gs-video
:link-type: ref
Install NeMo Curator, configure storage, prepare data, and run your first video pipeline.
:::

::::

---

## Pipelines

::::{grid} 1 1 1 2
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`video;1.5em;sd-mr-1` Splitting Pipelines
:link: video-pipelines-splitting
:link-type: ref
Split long videos into clips using NeMo Curator and annotate them using various models.
+++
{bdg-secondary}`video-splitting`
{bdg-secondary}`captioning`
{bdg-secondary}`embeddings`
:::

:::{grid-item-card} {octicon}`video;1.5em;sd-mr-1` Deduplication Pipelines
:link: video-pipelines-dedup
:link-type: ref
Remove duplicate clips using NeMo Curator's deduplication pipeline.
+++
{bdg-secondary}`video-deduplication`
{bdg-secondary}`semantic-dedup`
:::

::::

---

## Tutorials

::::{grid} 1 1 1 2
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`mortar-board;1.5em;sd-mr-1` Beginner Tutorial
:link: video-tutorials-beginner
:link-type: ref
Learn how to customize NeMo Curator's pipelines for your specific needs.
+++
{bdg-secondary}`video-splitting`
{bdg-secondary}`embeddings`
{bdg-secondary}`captioning`
:::

:::{grid-item-card} {octicon}`mortar-board;1.5em;sd-mr-1` Pipeline Customization Tutorials
:link: video-tutorials-pipeline-cust-series
:link-type: ref
Learn how to customize NeMo Curator's pipelines for your specific needs.
+++
{bdg-secondary}`custom-pipelines`
{bdg-secondary}`stages`
{bdg-secondary}`ray`
:::

::::
