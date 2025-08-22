---
description: "Overview of NeMo Curator's video processing pipeline workflow including splitting, deduplication, and sharding stages"
categories: ["video-curation"]
tags: ["pipeline", "video-processing", "splitting", "deduplication", "sharding", "workflow"]
personas: ["mle-focused", "data-scientist-focused"]
difficulty: "intermediate"
content_type: "concept"
modality: "video-only"

---

(video-pipelines)=
# Video Curation Pipelines

## Pipeline Workflow

These pipelines are typically run in the following order:

1. **Splitting Pipeline**: Breaks down long videos into shorter, manageable clips while preserving scene continuity and content relevance.
2. **Deduplication Pipeline**: Removes duplicate or near-duplicate clips using semantic similarity to ensure dataset diversity and quality.
3. **Sharding Pipeline**: Organizes the processed clips into efficient data shards for optimal training performance and distributed processing.

## Pipeline Library

Explore the available default pipelines.

::::{grid} 1 1 1 2
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`video;1.5em;sd-mr-1` Splitting Pipelines
:link: video-pipelines-splitting
:link-type: ref
Split long videos into clips using NeMo Curator and annotate them using various models.
+++
{bdg-secondary}`video-splitting`
{bdg-secondary}`video-sharding`
{bdg-secondary}`custom-pipelines`
:::

:::{grid-item-card} {octicon}`video;1.5em;sd-mr-1` Deduplication Pipelines
:link: video-pipelines-dedup
:link-type: ref
Remove duplicate clips using NeMo Curator's deduplication pipeline.
+++
{bdg-secondary}`video-splitting`
{bdg-secondary}`video-sharding`
{bdg-secondary}`custom-pipelines`
:::

:::{grid-item-card} {octicon}`video;1.5em;sd-mr-1` Sharding Pipelines
:link: video-pipelines-sharding
:link-type: ref
Package your clips into datasets ready for training with NeMo Curator's sharding pipeline.
+++
{bdg-secondary}`video-splitting`
{bdg-secondary}`video-sharding`
{bdg-secondary}`custom-pipelines`
:::

::::

```{toctree}
:hidden:
:maxdepth: 2

splitting
dedup
sharding
```
