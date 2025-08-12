---
description: "Handle multilingual content and language-specific processing including language identification and stop word management"
categories: ["workflows"]
tags: ["language-management", "multilingual", "fasttext", "stop-words", "language-detection"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "workflow"
modality: "text-only"
---

(text-process-data-languages)=

# Language Management

Handle multilingual content and language-specific processing requirements using NeMo Curator's tools and utilities.

NeMo Curator provides robust tools for managing multilingual text datasets through language detection, stop word management, and specialized handling for non-spaced languages. These tools are essential for creating high-quality monolingual datasets and applying language-specific processing.

## How it Works

Language management in NeMo Curator typically follows this pattern using the Pipeline API:

```python
from ray_curator.pipeline import Pipeline
from ray_curator.backends.xenna.executor import XennaExecutor
from ray_curator.stages.text.io.reader import JsonlReader
from ray_curator.stages.text.modules import ScoreFilter
from ray_curator.stages.text.filters import FastTextLangId

# 1) Build the pipeline
pipeline = Pipeline(name="language_management")

# Read JSONL files into document batches
pipeline.add_stage(
    JsonlReader(file_paths="input_data/*.jsonl", files_per_partition=2)
)

# Identify languages and keep docs above a confidence threshold
pipeline.add_stage(
    ScoreFilter(
        FastTextLangId(model_path="/path/to/lid.176.bin", min_langid_score=0.3),
        score_field="language",
    )
)

# 2) Execute
executor = XennaExecutor()
results = pipeline.run(executor)
```

---

## Language Processing Capabilities

- **Language detection** using FastText and CLD2 (176+ languages)
- **Stop word management** with built-in lists and customizable thresholds
- **Special handling** for non-spaced languages (Chinese, Japanese, Thai, Korean)
- **Language-specific** text processing and quality filtering

## Available Tools

::::{grid} 1 1 1 2
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`globe;1.5em;sd-mr-1` Language Identification
:link: language
:link-type: doc
Identify document languages and separate multilingual datasets
+++
{bdg-secondary}`fasttext`
{bdg-secondary}`176-languages`
{bdg-secondary}`detection`
{bdg-secondary}`classification`
:::

:::{grid-item-card} {octicon}`filter;1.5em;sd-mr-1` Stop Words
:link: stopwords
:link-type: doc
Manage high-frequency words to enhance text extraction and content detection
+++
{bdg-secondary}`preprocessing`
{bdg-secondary}`filtering`
{bdg-secondary}`language-specific`
{bdg-secondary}`nlp`
:::

::::

## Usage

### Quick Start Example

```python
from ray_curator.pipeline import Pipeline
from ray_curator.backends.xenna import XennaExecutor
from ray_curator.stages.text.io.reader import JsonlReader
from ray_curator.stages.text.modules import ScoreFilter
from ray_curator.stages.text.filters import FastTextLangId

pipeline = Pipeline(name="langid_quickstart")

pipeline.add_stage(
    JsonlReader(file_paths="multilingual_data/*.jsonl", files_per_partition=2)
)

pipeline.add_stage(
    ScoreFilter(
        FastTextLangId(model_path="/path/to/lid.176.bin", min_langid_score=0.3),
        score_field="language",
    )
)

executor = XennaExecutor()
results = pipeline.run(executor)

# Optional: extract language code from the stored string "[score, LANG]"
import ast
for batch in results or []:
    df = batch.to_pandas()
    if "language" in df.columns:
        df["lang_code"] = df["language"].apply(lambda x: ast.literal_eval(x)[1] if isinstance(x, str) else x[1])
        # do something with df
```

### Supported Languages

NeMo Curator supports language identification for **176 languages** through FastText, including:

- **Major languages**: English, Spanish, French, German, Chinese, Japanese, Arabic, Russian
- **Regional languages**: Local and regional languages worldwide
- **Special handling**: Non-spaced languages (Chinese, Japanese, Thai, Korean)

## Best Practices

1. **Download the FastText model**: Get `lid.176.bin` from [fasttext.cc](https://fasttext.cc/docs/en/language-identification.html)
2. **Set appropriate thresholds**: Balance precision vs. recall based on your needs
3. **Handle non-spaced languages**: Use special processing for Chinese, Japanese, Thai, Korean
4. **Check on your domain**: Test language detection accuracy on your specific data

```{toctree}
:maxdepth: 4
:titlesonly:
:hidden:

Language Identification <language>
Stop Words <stopwords>
```
