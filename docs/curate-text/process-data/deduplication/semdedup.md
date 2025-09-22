---
description: "Remove semantically redundant data using embeddings and clustering to identify meaning-based duplicates in large text datasets"
categories: ["how-to-guides"]
tags: ["semantic-dedup", "embeddings", "clustering", "similarity", "meaning-based", "advanced"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "advanced"
content_type: "how-to"
modality: "text-only"
---

(text-process-data-format-sem-dedup)=
# Semantic Deduplication

Detect and remove semantically redundant data from your large text datasets using NeMo Curator.

Unlike exact or fuzzy deduplication, which focus on textual similarity, semantic deduplication leverages the meaning of content to identify duplicates. This approach can significantly reduce dataset size while maintaining or even improving model performance.

Semantic deduplication is particularly effective for large, uncurated web-scale datasets, where it can remove up to 50% of the data with minimal performance impact. The technique uses embeddings to identify "semantic duplicates" - content pairs that convey similar meaning despite using different words.

:::{note}
**GPU Acceleration**: Semantic deduplication requires GPU acceleration for both embedding generation and clustering operations. This method uses the `cudf` backend and PyTorch models on GPU for optimal performance.
:::

## How It Works

The SemDeDup algorithm consists of the following main steps:

1. **Embedding Generation**: Each document is embedded using a pre-trained model
2. **Clustering**: The embeddings are grouped into k clusters using k-means clustering
3. **Similarity Computation**: Within each cluster, pairwise cosine similarities are computed
4. **Duplicate Identification**: Document pairs with cosine similarity above a threshold are considered semantic duplicates
5. **Duplicate Removal**: From each group of semantic duplicates within a cluster, one representative document is kept (typically the one with the lowest cosine similarity to the cluster centroid) and the rest are removed

:::{note}
 NeMo Curator implements methods based on the paper [SemDeDup: Data-efficient learning at web-scale through semantic deduplication](https://arxiv.org/pdf/2303.09540) by Abbas et al.
:::

## Before You Start

Before running semantic deduplication, ensure that each document in your dataset has a unique identifier. You can use the `AddId` stage from NeMo Curator if needed:

```python
from nemo_curator.stages.text.modules import AddId
from nemo_curator.pipeline import Pipeline

# Create pipeline with ID generation
pipeline = Pipeline(name="add_ids_for_dedup")

# Add ID generation stage
pipeline.add_stage(
    AddId(
        id_field="doc_id",
        id_prefix="corpus"  # Optional prefix for meaningful IDs
    )
)
```

For more details on using `AddId`, refer to the {ref}`text-process-data-add-id` documentation.

## TextSemanticDeduplicationWorkflow Interface

The `TextSemanticDeduplicationWorkflow` class provides a comprehensive end-to-end interface for semantic deduplication in NeMo Curator:

### Key Parameters
- `input_path`: Path(s) to input files containing text data
- `output_path`: Directory to write deduplicated output
- `cache_path`: Directory to cache intermediate results (embeddings, kmeans, pairwise, etc.)
- `perform_removal`: Whether to perform duplicate removal (True) or just identify duplicates (False)
- `text_field`: Name of the text field in input data (default: "text")
- `id_field`: Name of the ID field in the data
- `model_identifier`: HuggingFace model identifier for embeddings
- `n_clusters`: Number of clusters for K-means
- `eps`: Epsilon value for duplicate identification

### Usage Modes

**Mode 1: Two-step process (`perform_removal=False`)**
```python
# Step 1: Identify duplicates only
workflow = TextSemanticDeduplicationWorkflow(
    input_path="input_data/",
    output_path="results/",
    perform_removal=False,  # Only identify duplicates
    eps=0.01
)
results = workflow.run(executor)
# Duplicates are saved to output_path/duplicates/
```

**Mode 2: One-step process (`perform_removal=True`)**
```python
# Returns deduplicated dataset directly
workflow = TextSemanticDeduplicationWorkflow(
    input_path="input_data/",
    output_path="results/",
    perform_removal=True,  # Complete deduplication
    eps=0.01
)
results = workflow.run(executor)
# Clean dataset saved to output_path/deduplicated/
```

---

## Quick Start

```python
from nemo_curator.stages.text.deduplication.semantic import TextSemanticDeduplicationWorkflow
from nemo_curator.backends import RayDataExecutor

# Option 1: Two-step process (more control)
workflow = TextSemanticDeduplicationWorkflow(
    input_path="input_data/*.jsonl",
    output_path="./results",
    cache_path="./sem_cache",
    model_identifier="sentence-transformers/all-MiniLM-L6-v2",
    n_clusters=100,
    eps=0.07,  # Similarity threshold
    id_field="doc_id",
    perform_removal=False  # Only identify duplicates
)

# Run workflow
executor = RayDataExecutor()
results = workflow.run(executor)
# Duplicate IDs saved to ./results/duplicates/

# Option 2: One-step process (simpler)
workflow_simple = TextSemanticDeduplicationWorkflow(
    input_path="input_data/*.jsonl",
    output_path="./results", 
    cache_path="./sem_cache",
    model_identifier="sentence-transformers/all-MiniLM-L6-v2",
    n_clusters=100,
    eps=0.07,
    id_field="doc_id",
    perform_removal=True  # Complete deduplication
)

results = workflow_simple.run(executor)
# Clean dataset saved to ./results/deduplicated/
```

---

## Configuration

Semantic deduplication in NeMo Curator is configured through the `TextSemanticDeduplicationWorkflow` dataclass parameters. Here's how to configure the workflow:

```python
from nemo_curator.stages.text.deduplication.semantic import TextSemanticDeduplicationWorkflow

# Configure workflow with parameters
workflow = TextSemanticDeduplicationWorkflow(
    # Input/Output configuration
    input_path="input_data/",
    output_path="results/",
    cache_path="semdedup_cache",  # Directory for intermediate files
    perform_removal=True,
    
    # Embedding generation parameters
    text_field="text",
    embedding_field="embeddings",
    model_identifier="sentence-transformers/all-MiniLM-L6-v2",
    embedding_max_seq_length=512,
    embedding_pooling="mean_pooling",
    embedding_model_inference_batch_size=256,
    
    # Semantic deduplication parameters
    n_clusters=100,  # Number of clusters for K-means
    id_field="id",
    distance_metric="cosine",
    which_to_keep="hard",
    eps=0.01,  # Similarity threshold
    
    # K-means clustering parameters
    kmeans_max_iter=300,
    kmeans_tol=1e-4,
    kmeans_random_state=42,
    kmeans_init="k-means||",
    pairwise_batch_size=1024,
    
    # I/O parameters
    input_filetype="jsonl",
    output_filetype="parquet",
    verbose=True
)
```

You can customize these parameters to suit your specific needs and dataset characteristics.

:::{note}
**Configuration Parameters**: The above configuration shows the most commonly used parameters. For advanced use cases, additional parameters like `embedding_max_chars` (to control text truncation), `kmeans_oversampling_factor` (for K-means optimization), and I/O parameters are available. See the complete parameter table below for all options.
:::

### Embedding Models

You can choose alternative pre-trained models for embedding generation by modifying the `embedding_model_name_or_path` parameter in the configuration file.

::::{tab-set}

:::{tab-item} Sentence Transformer

Sentence transformers are ideal for text-based semantic similarity tasks. 

```python
workflow = TextSemanticDeduplicationWorkflow(
    model_identifier="sentence-transformers/all-MiniLM-L6-v2",
    # ... other parameters
)
```
:::

:::{tab-item} HuggingFace Model

```python
workflow = TextSemanticDeduplicationWorkflow(
    model_identifier="facebook/opt-125m",
    # ... other parameters
)
```

You can also use your own pre-trained custom models by specifying the path.
:::
::::

When changing the model, ensure that:

1. The model is compatible with the data type you're working with
2. You adjust the `embedding_model_inference_batch_size` parameter for your model's memory requirements
3. The chosen model is appropriate for the language or domain of your dataset

### Deduplication Threshold

The semantic deduplication process is controlled by the similarity threshold parameter:

```python
workflow = TextSemanticDeduplicationWorkflow(
    # ... other parameters
    eps=0.01  # Similarity threshold
)
```

`eps`: The similarity threshold used for identifying duplicates. This value determines how similar documents need to be to be considered duplicates. Lower values are more strict, requiring higher similarity for documents to be considered duplicates.

When choosing an appropriate threshold:

* Lower thresholds (for example, 0.001): More strict, resulting in less deduplication but higher confidence in the identified duplicates
* Higher thresholds (for example, 0.1): Less strict, leading to more aggressive deduplication but potentially removing documents that are only somewhat similar

We recommend experimenting with different threshold values to find the optimal balance between data reduction and maintaining dataset diversity and quality. The impact of this threshold can vary depending on the nature and size of your dataset.

## Usage

::::{tab-set}

:::{tab-item} TextSemanticDeduplicationWorkflow Class
You can use the TextSemanticDeduplicationWorkflow class to perform all steps:

```python
from nemo_curator.stages.text.deduplication.semantic import TextSemanticDeduplicationWorkflow
from nemo_curator.backends import RayDataExecutor

# Initialize workflow with configuration
workflow = TextSemanticDeduplicationWorkflow(
    input_path="input_data/",
    output_path="results/",
    cache_path="cache/",
    text_field="text",
    id_field="doc_id",
    model_identifier="sentence-transformers/all-MiniLM-L6-v2",
    n_clusters=100,
    eps=0.01,
    perform_removal=False,  # Two-step process
    verbose=True
)

# Create executor
executor = RayDataExecutor()

# Two-step semantic deduplication process
# Step 1: Identify duplicates (saves duplicate IDs to output_path/duplicates/)
results = workflow.run(executor)

# Step 2: For manual removal, set perform_removal=True and re-run
workflow.perform_removal = True
final_results = workflow.run(executor)
# Clean dataset saved to output_path/deduplicated/

# Alternative: One-step process
workflow_onestep = TextSemanticDeduplicationWorkflow(
    input_path="input_data/",
    output_path="results/",
    cache_path="cache/",
    id_field="doc_id",
    perform_removal=True  # Complete deduplication
)
results = workflow_onestep.run(executor)
```

This approach allows for easy experimentation with different configurations and models without changing the core code.

```{tip}
**Flexible Interface**: The `TextSemanticDeduplicationWorkflow` class supports both one-step and two-step workflows:
- Use `perform_removal=True` for direct deduplication (saves clean dataset)
- Use `perform_removal=False` for manual control over the removal process (saves duplicate IDs only)

This interface provides comprehensive end-to-end semantic deduplication capabilities.
```
:::

:::{tab-item} Individual Components
Embedding Creation:

```python
from nemo_curator.stages.text.embedders import EmbeddingCreatorStage
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends import RayDataExecutor

# Create pipeline for embedding generation
pipeline = Pipeline(name="embedding_generation")

# Add embedding stage
embedding_stage = EmbeddingCreatorStage(
    model_identifier="sentence-transformers/all-MiniLM-L6-v2",
    text_field="text",
    embedding_field="embeddings",
    model_inference_batch_size=256
)
pipeline.add_stage(embedding_stage)

# Run pipeline
executor = RayDataExecutor()
results = pipeline.run(executor)
```

Semantic Deduplication Workflow:

```python
from nemo_curator.stages.deduplication.semantic.workflow import SemanticDeduplicationWorkflow

# Perform semantic deduplication on pre-generated embeddings
workflow = SemanticDeduplicationWorkflow(
    input_path="path/to/embeddings/",  # Directory with embedding parquet files
    output_path="path/to/output/",
    n_clusters=100,
    id_field="doc_id",
    embedding_field="embeddings",
    which_to_keep="hard",
    pairwise_batch_size=1024,
    eps=0.01,  # Similarity threshold for duplicate identification
    verbose=True
)

# Run the workflow
results = workflow.run(pairwise_executor=executor)

# Results contain timing information and duplicate counts
print(f"Total duplicates identified: {results['total_duplicates_identified']}")
print(f"Execution time: {results['total_execution_time']:.2f} seconds")

# Duplicate IDs are saved to output_path/duplicates/
```

:::

::::

--- 

### Comparison with Other Deduplication Methods

```{list-table} Deduplication Method Behavior Comparison
:header-rows: 1
:widths: 25 25 25 25

* - Method
  - Return Value Options
  - perform_removal Parameter
  - Workflow
* - ExactDuplicates
  - Duplicates or Clean Dataset
  - ✅ Available
  - One-step or two-step
* - FuzzyDuplicates
  - Duplicates or Clean Dataset  
  - ✅ Available
  - One-step or two-step
* - TextSemanticDeduplicationWorkflow
  - Duplicates or Clean Dataset
  - ✅ Available
  - One-step or two-step
```

### Key Parameters

```{list-table} Key Configuration Parameters
:header-rows: 1
:widths: 25 15 20 40

* - Parameter
  - Type
  - Default
  - Description
* - `model_identifier`
  - str
  - "sentence-transformers/all-MiniLM-L6-v2"
  - Pre-trained model for embedding generation
* - `embedding_model_inference_batch_size`
  - int
  - 256
  - Number of samples per embedding batch
* - `n_clusters`
  - int
  - 100
  - Number of clusters for k-means clustering
* - `kmeans_max_iter`
  - int
  - 300
  - Maximum iterations for clustering
* - `eps`
  - float
  - 0.01
  - Threshold for deduplication (higher = more aggressive)
* - `which_to_keep`
  - str
  - "hard"
  - Strategy for keeping duplicates ("hard"/"easy"/"random")
* - `pairwise_batch_size`
  - int
  - 1024
  - Batch size for similarity computation
* - `distance_metric`
  - str
  - "cosine"
  - Distance metric for similarity ("cosine" or "l2")
* - `embedding_pooling`
  - str
  - "mean_pooling"
  - Pooling strategy ("mean_pooling" or "last_token")
* - `perform_removal`
  - bool
  - true
  - Whether to perform duplicate removal
* - `text_field`
  - str
  - "text"
  - Name of the text field in input data
* - `id_field`
  - str
  - "id"
  - Name of the ID field in the data
```

## Output Format

The semantic deduplication process produces the following directory structure in your configured `cache_path`:

```s
cache_path/
├── embeddings/                           # Embedding outputs
│   └── *.parquet                         # Parquet files containing document embeddings
├── semantic_dedup/                       # Semantic deduplication cache
│   ├── kmeans_results/                   # K-means clustering outputs
│   │   ├── kmeans_centroids.npy         # Cluster centroids
│   │   └── embs_by_nearest_center/      # Embeddings organized by cluster
│   │       └── nearest_cent={0..n-1}/   # Subdirectories for each cluster
│   │           └── *.parquet            # Cluster member embeddings
│   └── pairwise_results/                # Pairwise similarity results
│       └── *.parquet                    # Similarity scores by cluster
└── output_path/
    ├── duplicates/                       # Duplicate identification results
    │   └── *.parquet                    # Document IDs to remove
    └── deduplicated/                     # Final clean dataset (if perform_removal=True)
        └── *.parquet                    # Deduplicated documents
```

### File Formats

1. **Document Embeddings** (`embeddings/*.parquet`):
   - Contains document IDs and their vector embeddings
   - Format: Parquet files with columns: `[id_column, embedding_column]`

2. **Cluster Assignments** (`clustering_results/`):
   - `kmeans_centroids.npy`: NumPy array of cluster centers
   - `embs_by_nearest_center/`: Parquet files containing cluster members
   - Format: Parquet files with columns: `[id_column, embedding_column, cluster_id]`

3. **Deduplicated Results** (`output_path/duplicates/*.parquet`):
   - Final output containing document IDs to remove after deduplication
   - Format: Parquet file with columns: `["id"]`
   - **Important**: Contains only the IDs of documents to remove, not the full document content
   - When `perform_removal=True`, clean dataset is saved to `output_path/deduplicated/`

Typically, semantic deduplication reduces dataset size by 20–50% while maintaining or improving model performance.

## Performance Considerations

Semantic deduplication is computationally intensive, especially for large datasets. However, the benefits in terms of reduced training time and improved model performance often outweigh the upfront cost:

- Use GPU acceleration for faster embedding generation and clustering
- Adjust the number of clusters (`n_clusters`) based on your dataset size and available resources
- The `eps_to_extract` parameter controls the trade-off between dataset size reduction and potential information loss
- Using batched cosine similarity significantly reduces memory requirements for large datasets

### GPU Requirements

**Hardware Prerequisites:**
- NVIDIA GPU with CUDA support
- Sufficient GPU memory (recommended: >8GB for medium datasets)
- RAPIDS libraries (cuDF, cuML) for GPU-accelerated operations

**Backend Requirements:**
- **Required**: `cudf` backend for GPU acceleration
- **Not supported**: CPU-only processing (use hash-based deduplication instead)

**Performance Characteristics:**
- **Embedding Generation**: GPU-accelerated using PyTorch models
- **Clustering**: GPU-accelerated k-means clustering
- **Similarity Computation**: Batched GPU operations for cosine similarity

```{list-table} Performance Scaling
:header-rows: 1
:widths: 25 25 25 25

* - Dataset Size
  - GPU Memory Required
  - Processing Time
  - Recommended GPUs
* - <100K docs
  - 4-8 GB
  - 1-2 hours
  - RTX 3080, A100
* - 100K-1M docs
  - 8-16 GB
  - 2-8 hours
  - RTX 4090, A100
* - >1M docs
  - >16 GB
  - 8+ hours
  - A100, H100
```

For very large datasets, consider distributed processing across multiple GPUs or use incremental processing approaches.

For more details on the algorithm and its performance implications, refer to the original paper: [SemDeDup: Data-efficient learning at web-scale through semantic deduplication](https://arxiv.org/pdf/2303.09540) by Abbas et al.
