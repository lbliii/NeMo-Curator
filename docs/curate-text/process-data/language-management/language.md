---
description: "Identify document languages accurately using FastText models supporting 176 languages for multilingual text processing"
categories: ["how-to-guides"]
tags: ["language-identification", "fasttext", "multilingual", "176-languages", "detection", "classification"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "how-to"
modality: "text-only"
---

(text-process-data-languages-id)=
# Language Identification and Unicode Fixing

Large unlabeled text corpora often contain a variety of languages. NVIDIA NeMo Curator provides tools to accurately identify the language of each document, which is essential for language-specific curation tasks and building high-quality monolingual datasets.

## How it Works

NeMo Curator's language identification system works through a three-step process:

1. **Text Preprocessing**: The system normalizes input text by stripping whitespace and converting newlines to spaces to prepare it for FastText analysis.

2. **FastText Language Detection**: The pre-trained FastText language identification model (`lid.176.bin`) analyzes the preprocessed text and returns:
   - A confidence score (0.0 to 1.0) indicating certainty of the prediction
   - A language code (for example, "EN", "ES", "FR") in FastText's two-letter uppercase format

3. **Filtering and Scoring**: The pipeline filters documents based on a configurable confidence threshold (`min_langid_score`) and stores both the confidence score and language code as metadata.

### Language Detection Process

The `FastTextLangId` filter implements this workflow by:

- Loading the FastText language identification model on worker initialization
- Processing text through `model.predict()` with `k=1` to get the top language prediction
- Extracting the language code from FastText labels (for example, `__label__en` becomes "EN")
- Comparing confidence scores against the threshold to determine document retention
- Returning results as `[confidence_score, language_code]` for downstream processing

This approach supports **176 languages** with high accuracy, making it suitable for large-scale multilingual dataset curation where language-specific processing and monolingual dataset creation are critical.

## Before You Start

- Language identification requires NeMo Curator with distributed backend support. For installation instructions, see the {ref}`admin-installation` guide.

---

## Usage

The following example demonstrates how to create a language identification pipeline using Curator with distributed processing.

::::{tab-set}

:::{tab-item} Python

```python
"""Language identification using Curator."""

from ray_curator.backends.xenna import XennaExecutor
from ray_curator.pipeline import Pipeline
from ray_curator.stages.text.filters import FastTextLangId
from ray_curator.stages.text.io.reader import JsonlReader
from ray_curator.stages.text.modules import ScoreFilter

def create_language_identification_pipeline(data_dir: str) -> Pipeline:
    """Create a pipeline for language identification."""
    
    # Define pipeline
    pipeline = Pipeline(
        name="language_identification", 
        description="Identify document languages using FastText"
    )
    
    # Add stages
    # 1. Reader stage - creates tasks from JSONL files
    pipeline.add_stage(
        JsonlReader(
            file_paths=data_dir,
            files_per_partition=2,  # Each task processes 2 files
            reader="pandas"
        )
    )
    
    # 2. Language identification with filtering
    # IMPORTANT: Download lid.176.bin or lid.176.ftz from https://fasttext.cc/docs/en/language-identification.html
    fasttext_model_path = "/path/to/lid.176.bin"  # or lid.176.ftz (compressed)
    pipeline.add_stage(
        ScoreFilter(
            FastTextLangId(model_path=fasttext_model_path, min_langid_score=0.3), 
            score_field="language"
        )
    )
    
    return pipeline

def main():
    # Create pipeline
    pipeline = create_language_identification_pipeline("./data")
    
    # Print pipeline description
    print(pipeline.describe())
    
    # Create executor and run
    executor = XennaExecutor()
    results = pipeline.run(executor)
    
    # Process results
    print(f"Pipeline completed! Processed {len(results)} batches")
    
    total_documents = sum(task.num_items for task in results) if results else 0
    print(f"Total documents processed: {total_documents}")
    
    # Access language scores
    for i, batch in enumerate(results):
        if batch.num_items > 0:
            df = batch.to_pandas()
            print(f"Batch {i} columns: {list(df.columns)}")
            # Language scores are now in the 'language' field

if __name__ == "__main__":
    main()
```

:::
::::

## Configuration

Configure Curator language identification programmatically using the Python API as shown in the previous section.

:::{note}
YAML pipeline configuration support for Curator will be available in a future release. Use the programmatic Python API for now.
:::

## Understanding Results

The language identification process adds a score field to each document batch:

1. **`language` field**: Contains the FastText language identification results as a string representation of a list with two elements (for backend compatibility):
   - Element 0: The confidence score (between 0 and 1)
   - Element 1: The language code in FastText format (for example, "EN" for English, "ES" for Spanish)

2. **Task-based processing**: Curator processes documents in batches (tasks), and results are available through the task's pandas DataFrame:

```python
# Access results from pipeline execution
for batch in results:
    df = batch.to_pandas()
    # Language scores are in the 'language' column
    print(df[['text', 'language']].head())
```

:::{note}
FastText language codes are typically two-letter uppercase codes that may differ slightly from standard ISO 639-1 codes. The model supports 176 languages with high accuracy.
:::

### Processing Language Results

You can extract and work with language identification results:

```python
import ast

# Extract language codes from results
for batch in results:
    df = batch.to_pandas()
    if 'language' in df.columns:
        # Parse the "[score, language_code]" string safely
        df['lang_score'] = df['language'].apply(lambda x: ast.literal_eval(x)[0] if isinstance(x, str) else x[0])
        df['lang_code'] = df['language'].apply(lambda x: ast.literal_eval(x)[1] if isinstance(x, str) else x[1])

        # Filter by confidence threshold
        high_confidence = df[df['lang_score'] > 0.7]
        print(f"High confidence documents: {len(high_confidence)}")
```

A higher confidence score indicates greater certainty in the language identification. The `ScoreFilter` automatically filters documents below your specified `min_langid_score` threshold.

## Performance Considerations

- Language identification with Curator is computationally intensive but scales with Ray's distributed processing
- Curator handles distributed execution across cluster nodes using the XennaExecutor backend
- The FastText model file (`lid.176.bin` or compressed `lid.176.ftz`) must be accessible to all worker nodes
- Processing speed depends on document length, cluster size, available computational resources, and the `files_per_partition` setting
- Memory usage scales with cluster configuration and task batch sizes
- Curator provides efficient resource allocation and auto scaling for large-scale processing
- **Task-based processing**: The pipeline groups documents into tasks based on the `JsonlReader` configuration, enabling parallel processing across the cluster

## Best Practices

:::{important}
**Model Download Required**: Download the FastText language identification model from the [official FastText repository](https://fasttext.cc/docs/en/language-identification.html) before using this filter. Available formats:
- `lid.176.bin` (full model, ~130MB)
- `lid.176.ftz` (compressed model, smaller file size)
:::

### Curator-Specific Recommendations

- **Task partitioning**: Adjust `files_per_partition` in `JsonlReader` based on your data size and cluster capacity. Smaller values create more tasks for better parallel processing
- **Pipeline design**: Use `ScoreFilter` for combined scoring and filtering, or separate `Score` and `Filter` stages for more control
- **Model accessibility**: Ensure the FastText model file is accessible to all worker nodes in your Ray cluster
- **Resource allocation**: Configure appropriate resources for the `FastTextLangId` stage based on your model size and processing requirements

### Confidence Threshold Guidelines

- **Default threshold (0.3)**: Balanced approach suitable for most use cases
- **Higher threshold (0.7+)**: More precision but may discard borderline documents
- **Lower threshold (0.1-0.2)**: Higher recall but may include misclassified documents

### Production Workflow Tips

- Analyze the language distribution in your dataset using the pipeline results to understand composition
- Consider a two-pass approach: first filter with a lower threshold, then manually review edge cases
- In production, verify language identification accuracy on a sample of your domain data
- Track task completion and resource usage through Ray's monitoring capabilities
- Save pipeline results to Parquet format for efficient downstream processing
