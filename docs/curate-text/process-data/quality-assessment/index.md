---
description: "Score and remove low-quality content using heuristics and ML classifiers with comprehensive filtering capabilities"
categories: ["workflows"]
tags: ["quality-assessment", "filtering", "heuristic", "classifier", "distributed", "scoring"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "workflow"
modality: "text-only"
---

(text-process-data-filter)=
# Quality Assessment & Filtering

Score and remove low-quality content using heuristics and ML classifiers to prepare your data for model training using NVIDIA NeMo Curator tools and utilities.

Large datasets often contain documents considered to be "low quality." In this context, "low quality" data means data we do not want a downstream model to learn from, and "high quality" data is data that we do want a downstream model to learn from. The metrics that define quality can vary by use case.

## How It Works

NeMo Curator filtering uses several key components:

::::{tab-set}

:::{tab-item} ScoreFilter

The `ScoreFilter` is at the center of filtering in NeMo Curator. It applies a filter to a document and optionally saves the score as metadata:

```python
from ray_curator.pipeline.pipeline import Pipeline
from ray_curator.backends.xenna.executor import XennaExecutor
from ray_curator.stages.text.io.reader.jsonl import JsonlReader
from ray_curator.stages.text.filters.heuristic_filter import WordCountFilter
from ray_curator.stages.text.modules.score_filter import ScoreFilter
from ray_curator.stages.text.io.writer.jsonl import JsonlWriter

pipeline = Pipeline(name="scorefilter_example")
pipeline.add_stage(JsonlReader(file_paths="books_dataset/*.jsonl", files_per_partition=4))
pipeline.add_stage(ScoreFilter(WordCountFilter(min_words=80), text_field="text", score_field="word_count"))
pipeline.add_stage(JsonlWriter(output_dir="long_books/"))

XennaExecutor().run(stages=pipeline._stages)  # or pipeline.run(XennaExecutor())
```

The filter object implements two key methods:

- `score_document`: Computes a quality score for a document
- `keep_document`: Determines if a document should be kept based on its score

:::

:::{tab-item} Filter and Score Modules

For more specific use cases, NeMo Curator provides two specialized modules:

- `Score`: A module that only adds metadata scores to records without filtering
  - Takes a scoring function that evaluates text and returns a score
  - Adds the score to a specified metadata field
  - Useful for analysis or multi-stage filtering pipelines
  
```python
from ray_curator.stages.text.modules.score_filter import Score

# Add a score without filtering (as a pipeline stage)
pipeline.add_stage(Score(WordCountFilter().score_document, text_field="text", score_field="word_count"))
```

- `Filter`: A module that filters based on pre-computed metadata
  - Takes a filter function that evaluates metadata and returns True/False
  - Only uses existing metadata fields (doesn't compute new scores)
  - Efficient for filtering on pre-computed metrics
  
```python
from ray_curator.stages.text.modules.score_filter import Filter

# Filter using a pre-computed column
pipeline.add_stage(Filter(lambda score: score >= 100, filter_field="word_count"))
```

You can combine these modules in pipelines:

```python
# Compose as pipeline stages
pipeline.add_stage(Score(word_counter, score_field="word_count"))
pipeline.add_stage(Score(symbol_counter, score_field="symbol_ratio"))
pipeline.add_stage(Filter(lambda x: x >= 100, filter_field="word_count"))
pipeline.add_stage(Filter(lambda x: x <= 0.3, filter_field="symbol_ratio"))
```

:::

:::{tab-item} Batched Filtering

For improved performance, NeMo Curator supports batch processing using the `@batched` decorator:

```python
from nemo_curator.utils.decorators import batched
import pandas as pd

class BatchedFilter(DocumentFilter):
    @batched
    def keep_document(self, scores: pd.Series):
        # Process multiple documents in one operation
        return scores > 10
```

The batched processing can significantly improve performance on large datasets by:
- Reducing function call overhead
- Enabling vectorized operations
- Optimizing memory usage

:::

::::

---

## Filtering Approaches

::::{grid} 1 1 1 2
:gutter: 2

:::{grid-item-card} {octicon}`filter;1.5em;sd-mr-1` Heuristic Filtering
:link: heuristic
:link-type: doc
Filter text using configurable rules and metrics
+++
{bdg-secondary}`rules`
{bdg-secondary}`metrics`
{bdg-secondary}`fast`
:::

:::{grid-item-card} {octicon}`cpu;1.5em;sd-mr-1` Classifier Filtering
:link: classifier
:link-type: doc
Filter text using trained quality classifiers
+++
{bdg-secondary}`ml-models`
{bdg-secondary}`quality`
{bdg-secondary}`scoring`
:::

:::{grid-item-card} {octicon}`cpu;1.5em;sd-mr-1` Distributed Classification
:link: distributed-classifier
:link-type: doc
GPU-accelerated classification with pre-trained models
+++
{bdg-secondary}`gpu`
{bdg-secondary}`distributed`
{bdg-secondary}`scalable`
:::

:::{grid-item-card} {octicon}`terminal;1.5em;sd-mr-1` Custom Filters
:link: custom
:link-type: doc
Implement and combine your own custom filters
+++
{bdg-secondary}`custom`
{bdg-secondary}`flexible`
{bdg-secondary}`extensible`
:::

::::

## Usage

Use the Curator pipeline to read data, apply filters/classifiers, and write results. Example:

```python
from ray_curator.pipeline import Pipeline
from ray_curator.backends.xenna.executor import XennaExecutor
from ray_curator.stages.text.io.reader.jsonl import JsonlReader
from ray_curator.stages.text.filters.heuristic_filter import WordCountFilter, RepeatingTopNGramsFilter
from ray_curator.stages.text.modules import ScoreFilter
from ray_curator.stages.text.io.writer import JsonlWriter

pipeline = Pipeline(name="quality_filtering")
pipeline.add_stage(
    JsonlReader(file_paths="/path/to/input/*.jsonl", files_per_partition=4)
).add_stage(
    ScoreFilter(WordCountFilter(min_words=80), text_field="text", score_field="word_count")
).add_stage(
    ScoreFilter(RepeatingTopNGramsFilter(n=3, max_repeating_ngram_ratio=0.18), text_field="text")
).add_stage(
    JsonlWriter(output_dir="/path/to/output/high_quality")
)

executor = XennaExecutor()
pipeline.run(executor)
```

```{toctree}
:maxdepth: 4
:titlesonly:
:hidden:

Heuristic Filters <heuristic>
Classifier Filters <classifier>
Distributed Classification <distributed-classifier>
Custom Filters <custom>
```

## Best Practices

When filtering large datasets, consider these performance tips:

1. **Order matters**: Place computationally inexpensive filters early in your pipeline
2. **Batch size tuning**: Adjust batch sizes based on your hardware capabilities
3. **Use vectorization**: Implement batched methods for compute-intensive filters
4. **Disk I/O**: Consider compression and chunking strategies for large datasets
5. **Distributed processing**: For TB-scale datasets, run pipelines with a distributed executor (for example, `XennaExecutor`) and adjust stage resources and batch sizes to match your cluster