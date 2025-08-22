---
description: "Collection of tutorials for video curation workflows including beginner guides and advanced pipeline customization techniques"
categories: ["video-curation"]
tags: ["tutorial", "video-processing", "pipeline", "customization", "workflow", "beginner"]
personas: ["mle-focused", "data-scientist-focused"]
difficulty: "beginner"
content_type: "tutorial"
modality: "video-only"

---

(video-tutorials)=
# Video Curation Tutorials

Use the tutorials in this section to gain a deeper understanding of how NeMo Curator enables video curation tasks.

```{tip}
Tutorials are organized by complexity and typically build on one another.
```

---

::::{grid} 1 1 1 1
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`mortar-board;1.5em;sd-mr-1` Beginner Tutorial
:link: video-tutorials-beginner
:link-type: ref
Learn how to build and run your first video pipeline using NeMo Curator's video curator component. This tutorial covers basic pipeline construction, model downloading, and pipeline execution.
+++
{bdg-secondary}`video-splitting`
{bdg-secondary}`video-sharding`
{bdg-secondary}`custom-pipelines`
:::

:::{grid-item-card} {octicon}`mortar-board;1.5em;sd-mr-1` Split, Deduplicate, and Shard Videos
:link: video-tutorials-split-dedup-shard-workflow
:link-type: ref
Learn how to remove duplicate clips by running the semantic deduplication pipeline.
+++
{bdg-secondary}`semantic-deduplication`
:::

:::{grid-item-card} {octicon}`mortar-board;1.5em;sd-mr-1` Pipeline Customization Series
:link: video-tutorials-pipeline-cust-series
:link-type: ref
Learn how to customize video pipelines in this multi-part tutorial series.
+++
{bdg-secondary}`video-splitting`
{bdg-secondary}`video-sharding`
{bdg-secondary}`custom-pipelines`
:::

::::

```{toctree}
:hidden:
:maxdepth: 4

Beginner Tutorial <beginner>
Split, Dedup, and Shard Videos <split-dedup-shard-workflow>
Pipeline Customization <pipeline-customization/index>
```
