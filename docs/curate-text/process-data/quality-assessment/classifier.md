---
description: "Filter text using trained quality classifiers including FastText models and pre-trained language classification"
categories: ["how-to-guides"]
tags: ["classifier-filtering", "fasttext", "ml-models", "quality", "training", "scoring"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "how-to"
modality: "text-only"
---

(text-process-data-filter-classifier)=

# Classifier-Based Filtering

Classifier-based filtering uses machine learning models to differentiate between high-quality and low-quality documents. NVIDIA NeMo Curator implements an approach similar to the one described in [Brown et al., 2020](https://arxiv.org/abs/2005.14165), which trains a binary skip-gram classifier to distinguish between curated high-quality data and lower-quality data.

## Supported Classifier Models

NeMo Curator supports a variety of classifier models for different filtering and classification tasks. The table below summarizes the main supported models, their backend, typical use case, and HuggingFace model link (if public):

```{list-table}
:header-rows: 1
:widths: 20 20 30 30
* - Classifier Name
  - Model Type
  - Typical Use Case / Description
  - HuggingFace Model/Link
* - FastTextQualityFilter
  - fastText (binary classifier)
  - Quality filtering, high/low quality document classification (available as filter, not distributed classifier)
  - https://fasttext.cc/
* - FastTextLangId
  - fastText (language identification)
  - Language identification (available as filter, not distributed classifier)
  - https://fasttext.cc/docs/en/language-identification.html
* - QualityClassifier
  - DeBERTa (transformers, HF)
  - Document quality classification (multi-class, e.g., for curation)
  - https://huggingface.co/nvidia/quality-classifier-deberta
* - DomainClassifier
  - DeBERTa (transformers, HF)
  - Domain classification (English)
  - https://huggingface.co/nvidia/domain-classifier
* - MultilingualDomainClassifier
  - mDeBERTa (transformers, HF)
  - Domain classification (multilingual, 52 languages)
  - https://huggingface.co/nvidia/multilingual-domain-classifier
* - ContentTypeClassifier
  - DeBERTa (transformers, HF)
  - Content type classification (11 speech types)
  - https://huggingface.co/nvidia/content-type-classifier-deberta
* - AegisClassifier
  - LlamaGuard-7b (LLM, PEFT, HF)
  - Safety classification (AI content safety, requires access to LlamaGuard-7b)
  - https://huggingface.co/meta-llama/LlamaGuard-7b
* - InstructionDataGuardClassifier
  - Custom neural net (used with Aegis)
  - Detects instruction data poisoning
  - https://huggingface.co/nvidia/instruction-data-guard
* - FineWebEduClassifier
  - SequenceClassification (transformers, HF)
  - Educational content quality scoring (FineWeb)
  - https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier
* - FineWebMixtralEduClassifier
  - SequenceClassification (transformers, HF)
  - Educational content quality scoring (Mixtral variant)
  - https://huggingface.co/nvidia/nemocurator-fineweb-mixtral-edu-classifier
* - FineWebNemotronEduClassifier
  - SequenceClassification (transformers, HF)
  - Educational content quality scoring (Nemotron-4 variant)
  - https://huggingface.co/nvidia/nemocurator-fineweb-nemotron-4-edu-classifier
```

## How It Works

Classifier-based filtering learns the characteristics of high-quality documents from training data, unlike heuristic filtering which relies on predefined rules and thresholds. This approach is particularly effective when:

- You have a reference dataset of known high-quality documents
- The distinction between high and low quality is complex or subtle
- You want to filter based on domain-specific characteristics

NVIDIA NeMo Curator uses [fastText](https://fasttext.cc/) for implementing classifier-based filtering, which offers excellent performance and scalability for text classification tasks.

:::{note}
fastText is the official name and capitalization used by the fastText library created by Facebook Research.
:::

The classifier-based filtering process involves:

1. Preparing training data by sampling from high-quality and low-quality datasets
2. Training a binary skip-gram classifier using fastText
3. Using the trained model to score documents in your dataset
4. Filtering documents based on the classifier scores, optionally using Pareto-based sampling

---

## Usage

:::{note}
Training fastText classifiers requires using CLI commands. The trained models can then be used with the Python API for filtering datasets.
:::

### 1. Prepare Training Data

First, you need to prepare training data by sampling from high-quality and low-quality datasets using the CLI command.

You can prepare training data using Python scripts:

```python
from nemo_curator.stages.text.io.reader import JsonlReader
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends.xenna.executor import XennaExecutor
import random

# Sample from low-quality dataset (e.g., raw Common Crawl)
def sample_documents(input_path, output_path, num_samples, label):
    pipeline = Pipeline(name="sample_data")
    reader = JsonlReader(file_paths=input_path, fields=["text"])
    pipeline.add_stage(reader)
    
    # Execute pipeline to load data
    executor = XennaExecutor()
    results = pipeline.run(executor)
    
    # Sample and save with labels for fastText format
    with open(output_path, 'w') as f:
        for result in results:
            data = result.to_pandas()
            sampled = data.sample(min(num_samples, len(data)))
            for _, row in sampled.iterrows():
                f.write(f"{label} {row['text'].replace(chr(10), ' ')}\n")

# Create training samples
sample_documents(
    "/path/to/common-crawl/*.jsonl", 
    "./cc_samples.txt", 
    10000, 
    "__label__cc"
)
sample_documents(
    "/path/to/wikipedia/*.jsonl", 
    "./hq_samples.txt", 
    10000, 
    "__label__hq"
)
```

#### Command Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `--input-data-dir` | Directory containing JSONL files to sample from | `/data/common_crawl/` |
| `--output-num-samples` | Number of documents to sample | `10000` |
| `--label` | FastText label prefix for the category | `__label__hq` or `__label__cc` |
| `--output-train-file` | Output file for training samples | `./samples.txt` |

### 2. Train a Classifier

Next, train a fastText classifier using the prepared samples. You can use the fastText library directly:

```python
import fasttext

# Combine training samples into a single file
with open('./fasttext_samples.train', 'w') as outfile:
    with open('./cc_samples.txt', 'r') as infile:
        outfile.write(infile.read())
    with open('./hq_samples.txt', 'r') as infile:
        outfile.write(infile.read())

# Train the fastText model
model = fasttext.train_supervised(
    input='./fasttext_samples.train',
    epoch=25,
    lr=0.1,
    wordNgrams=2,
    dim=100,
    loss='softmax'
)

# Save the trained model
model.save_model('./quality_classifier.bin')

# Evaluate the model
print("Model validation results:")
result = model.test('./fasttext_samples.train')
print(f"Number of examples: {result[0]}")
print(f"Precision: {result[1]:.4f}")
print(f"Recall: {result[2]:.4f}")
```

#### Training Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `epoch` | Number of training epochs | 25 |
| `lr` | Learning rate | 0.1 |
| `wordNgrams` | Max length of word ngram | 2 |
| `dim` | Size of word vectors | 100 |
| `loss` | Loss function (softmax, ns, hs) | softmax |

The training will output validation metrics including precision and recall scores.

### 3. Apply the Classifier for Filtering

Finally, use the trained model to filter your dataset. Note that FastText classifiers work as filters in pipelines, not as distributed classifiers:

::::{tab-set}

:::{tab-item} Python

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.text.io.reader import JsonlReader
from nemo_curator.stages.text.io.writer import JsonlWriter
from nemo_curator.stages.text.modules import ScoreFilter
from nemo_curator.stages.text.filters import FastTextQualityFilter

# Create pipeline with FastText filter
pipeline = Pipeline(name="fasttext_quality_pipeline")

# Add stages
read_stage = JsonlReader("input_data/")
filter_stage = ScoreFilter(
    FastTextQualityFilter(
        model_path="./quality_classifier.bin",
        label="__label__hq",  # High quality label
        alpha=3,              # Pareto distribution alpha parameter
        seed=42               # Random seed for reproducibility
    ),
    text_field="text",
    score_field="quality_score"
)
write_stage = JsonlWriter("high_quality_output/")

pipeline.add_stage(read_stage)
pipeline.add_stage(filter_stage)
pipeline.add_stage(write_stage)

# Execute pipeline (uses XennaExecutor by default)
results = pipeline.run()

# Optional: Use a custom executor configuration
from nemo_curator.backends.xenna.executor import XennaExecutor

custom_executor = XennaExecutor(config={
    "execution_mode": "streaming",
    "cpu_allocation_percentage": 0.9
})
results = pipeline.run(executor=custom_executor)
```

:::

:::{tab-item} Configuration

You can configure FastText filters with different parameters:

```python
from nemo_curator.stages.text.filters import FastTextQualityFilter

# Basic quality filter
basic_filter = FastTextQualityFilter(
    model_path="./quality_classifier.bin",
    label="__label__hq",  # High quality label
    alpha=3,              # Pareto distribution alpha parameter
    seed=42               # Random seed for reproducibility
)

# More selective filter (higher alpha = more selective)
selective_filter = FastTextQualityFilter(
    model_path="./quality_classifier.bin",
    label="__label__hq",
    alpha=5,              # Higher alpha for stricter filtering
    seed=42
)

# Language identification filter
lang_filter = FastTextLangId(
    model_path="./lid.176.bin",  # fastText language ID model
    language="en",               # Target language
    score_threshold=0.8          # Minimum confidence score
)
```

:::

::::

## Pareto-Based Sampling

NeMo Curator's implementation includes support for Pareto-based sampling, as described in Brown et al., 2020. This approach:

1. Scores documents using the trained classifier
2. Ranks documents based on their scores
3. Samples documents according to a Pareto distribution, favoring higher-ranked documents

This method helps maintain diversity in the dataset while still prioritizing higher-quality documents.

## FastTextQualityFilter Parameters

The `FastTextQualityFilter` accepts the following parameters:

- `model_path` (str, required): Path to the trained fastText model file
- `label` (str, default="__label__hq"): The label for high-quality documents
- `alpha` (float, default=3): Alpha parameter for Pareto distribution sampling
- `seed` (int, default=42): Random seed for reproducible sampling

## Configuration

A typical configuration for classifier-based filtering looks like:

```yaml
filters:
  - name: ScoreFilter
    filter:
      name: FastTextQualityFilter
      model_path: /path/to/quality_classifier.bin
      label: __label__hq
      alpha: 3
      seed: 42
    text_field: text
    score_field: quality_score
```

## Best Practices

For effective classifier-based filtering:

1. **Training data selection**: Use truly high-quality sources for positive examples
2. **Validation**: Manually review a sample of filtered results to confirm effectiveness
3. **Threshold tuning**: Adjust the threshold based on your quality requirements
4. **Combination with heuristics**: Consider using heuristic filters as a pre-filter
5. **Domain adaptation**: Train domain-specific classifiers for specialized corpora