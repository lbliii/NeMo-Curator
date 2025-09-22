---
description: "Text processing workflows including quality filtering, fuzzy deduplication, content cleaning, and pipeline design"
categories: ["concepts-architecture"]
tags: ["data-processing", "quality-filtering", "deduplication", "pipeline", "pii-removal", "distributed"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "concept"
modality: "text-only"
---

(about-concepts-text-data-processing)=
# Text Processing Concepts

This guide covers the most common text processing workflows in NVIDIA NeMo Curator, based on real-world usage patterns from production data curation pipelines.

## Most Common Workflows

The majority of NeMo Curator users follow these core workflows, typically in this order:

### 1. Quality Filtering

Most users start with basic quality filtering using heuristic filters to remove low-quality content:

**Essential Quality Filters:**

- `WordCountFilter` - Remove too short/long documents
- `NonAlphaNumericFilter` - Remove symbol-heavy content  
- `RepeatedLinesFilter` - Remove repetitive content
- `PunctuationFilter` - Ensure proper sentence structure
- `BoilerPlateStringFilter` - Remove template/boilerplate text

### 2. Fuzzy Deduplication 

For production datasets, fuzzy deduplication is essential to remove near-duplicate content across sources:

**Key Components:**

- `FuzzyDeduplicationWorkflow` - End-to-end fuzzy deduplication pipeline
- Ray distributed computing framework for scalability
- Connected components clustering for duplicate identification

### 3. Content Cleaning 

Basic text normalization and cleaning operations:

**Common Cleaning Steps:**

- `UnicodeReformatter` - Normalize Unicode characters
- `PiiModifier` - Remove or redact personal information
- `NewlineNormalizer` - Standardize line breaks
- Basic HTML/markup removal

### 4. Exact Deduplication 

Remove identical documents, especially useful for smaller datasets:

**Implementation:**
- `ExactDuplicates` - Hash-based exact matching
- MD5 or SHA-256 hashing for document identification

## Core Processing Architecture

NeMo Curator uses these fundamental building blocks that users combine into pipelines:

```{list-table}
:header-rows: 1

* - Component
  - Purpose  
  - Usage Pattern
* - **`Pipeline`**
  - Orchestrate processing stages
  - Every workflow starts here
* - **`ScoreFilter`**
  - Apply filters with optional scoring
  - Chain multiple quality filters
* - **`Modify`**
  - Transform document content
  - Clean and normalize text
* - **Reader/Writer Stages**
  - Load and save text data
  - Input/output for pipelines
* - **Processing Stages**
  - Transform DocumentBatch tasks
  - Core processing components
```

## Implementation Examples

### Complete Quality Filtering Pipeline

This is the most common starting workflow, used in 90% of production pipelines:

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends.xenna.executor import XennaExecutor
from nemo_curator.stages.text.io.reader import JsonlReader
from nemo_curator.stages.text.io.writer import JsonlWriter
from nemo_curator.stages.text.modules import ScoreFilter
from nemo_curator.stages.text.filters import (
    WordCountFilter,
    NonAlphaNumericFilter,
    RepeatedLinesFilter,
    PunctuationFilter,
    BoilerPlateStringFilter
)

# Create processing pipeline
pipeline = Pipeline(name="quality_filtering")

# Load dataset - the starting point for all workflows
reader = JsonlReader(file_paths="data/*.jsonl")
pipeline.add_stage(reader)

# Standard quality filtering pipeline (most common)
# Remove too short/long documents (essential)
word_count_filter = ScoreFilter(
    score_fn=WordCountFilter(min_words=50, max_words=10000),
    text_field="text",
    score_field="word_count"
)
pipeline.add_stage(word_count_filter)

# Remove symbol-heavy content
alpha_numeric_filter = ScoreFilter(
    score_fn=NonAlphaNumericFilter(max_non_alpha_numeric_to_text_ratio=0.25),
    text_field="text"
)
pipeline.add_stage(alpha_numeric_filter)

# Remove repetitive content
repeated_lines_filter = ScoreFilter(
    score_fn=RepeatedLinesFilter(max_repeated_line_fraction=0.7),
    text_field="text"
)
pipeline.add_stage(repeated_lines_filter)

# Ensure proper sentence structure
punctuation_filter = ScoreFilter(
    score_fn=PunctuationFilter(max_num_sentences_without_endmark_ratio=0.85),
    text_field="text"
)
pipeline.add_stage(punctuation_filter)

# Remove template/boilerplate text
boilerplate_filter = ScoreFilter(
    score_fn=BoilerPlateStringFilter(),
    text_field="text"
)
pipeline.add_stage(boilerplate_filter)

# Add writer stage
writer = JsonlWriter(path="filtered_data/")
pipeline.add_stage(writer)

# Execute pipeline
executor = XennaExecutor()
results = pipeline.run(executor)
```

### Content Cleaning Pipeline

Basic text normalization:

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends.xenna.executor import XennaExecutor
from nemo_curator.stages.text.io.reader import JsonlReader
from nemo_curator.stages.text.io.writer import JsonlWriter
from nemo_curator.stages.text.modules import Modify
from nemo_curator.stages.text.modifiers import UnicodeReformatter, PiiModifier

# Create cleaning pipeline
pipeline = Pipeline(name="content_cleaning")

# Read input data
reader = JsonlReader(file_paths="input_data/*.jsonl")
pipeline.add_stage(reader)

# Essential cleaning steps
# Normalize unicode characters (very common)
unicode_modifier = Modify(
    modifier=UnicodeReformatter(),
    text_field="text"
)
pipeline.add_stage(unicode_modifier)

# Remove/redact PII (important for production)
pii_modifier = Modify(
    modifier=PiiModifier(
        supported_entities=["PERSON", "EMAIL", "PHONE_NUMBER"],
        anonymize_action="replace"
    ),
    text_field="text"
)
pipeline.add_stage(pii_modifier)

# Write cleaned data
writer = JsonlWriter(path="cleaned_data/")
pipeline.add_stage(writer)

# Execute pipeline
executor = XennaExecutor()
results = pipeline.run(executor)
```

### Large-Scale Fuzzy Deduplication

Critical for production datasets (requires Ray + GPU):

```python
import ray
from nemo_curator.stages.deduplication.fuzzy.workflow import FuzzyDeduplicationWorkflow

# Initialize Ray cluster with GPU support (required for fuzzy deduplication)
ray.init(num_gpus=4)

# Configure fuzzy deduplication workflow (production settings)
fuzzy_workflow = FuzzyDeduplicationWorkflow(
    input_path="/path/to/input/data",
    cache_path="./cache",
    output_path="./output",
    text_field="text",
    perform_removal=False,  # Currently only identification supported
    # LSH parameters for ~80% similarity threshold
    num_bands=20,           # Number of LSH bands
    minhashes_per_band=13,  # Hashes per band
    char_ngrams=24,         # Character n-gram size
    seed=42
)

# Run fuzzy deduplication workflow
fuzzy_workflow.run()

# Cleanup Ray when done
ray.shutdown()
```

### Exact Deduplication (All dataset sizes)

Quick deduplication for any dataset size (requires Ray + GPU):

```python
import ray
from nemo_curator.stages.deduplication.exact.workflow import ExactDeduplicationWorkflow

# Initialize Ray cluster with GPU support (required for exact deduplication)
ray.init(num_gpus=4)

# Configure exact deduplication workflow
exact_workflow = ExactDeduplicationWorkflow(
    input_path="/path/to/input/data",
    output_path="/path/to/output",
    text_field="text",
    perform_removal=False,  # Currently only identification supported
    assign_id=True,         # Automatically assign unique IDs
    input_filetype="parquet"
)

# Run exact deduplication workflow
exact_workflow.run()

# Cleanup Ray when done
ray.shutdown()
```

### Complete End-to-End Pipeline

Most users combine these steps into a comprehensive workflow:

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends.xenna.executor import XennaExecutor

# Complete production pipeline (most common pattern)
def build_production_pipeline():
    pipeline = Pipeline(name="production_processing")
    
    # 1. Content cleaning first
    unicode_modifier = Modify(
        modifier=UnicodeReformatter(),
        text_field="text"
    )
    pipeline.add_stage(unicode_modifier)
    
    pii_modifier = Modify(
        modifier=PiiModifier(supported_entities=["PERSON"], anonymize_action="replace"),
        text_field="text"
    )
    pipeline.add_stage(pii_modifier)
    
    # 2. Quality filtering
    word_filter = ScoreFilter(
        score_fn=WordCountFilter(min_words=50, max_words=10000),
        text_field="text"
    )
    pipeline.add_stage(word_filter)
    
    alpha_filter = ScoreFilter(
        score_fn=NonAlphaNumericFilter(max_non_alpha_numeric_to_text_ratio=0.25),
        text_field="text"
    )
    pipeline.add_stage(alpha_filter)
    
    repeated_filter = ScoreFilter(
        score_fn=RepeatedLinesFilter(max_repeated_line_fraction=0.7),
        text_field="text"
    )
    pipeline.add_stage(repeated_filter)
    
    boilerplate_filter = ScoreFilter(
        score_fn=BoilerPlateStringFilter(),
        text_field="text"
    )
    pipeline.add_stage(boilerplate_filter)
    
    return pipeline

# Apply the complete pipeline
complete_pipeline = build_production_pipeline()
executor = XennaExecutor()
processed_results = complete_pipeline.run(executor)

# Then apply deduplication separately for large datasets
# For large datasets - use fuzzy deduplication
import ray
ray.init(num_gpus=4)
fuzzy_workflow = FuzzyDeduplicationWorkflow(
    input_path="/path/to/processed/data",
    cache_path="./cache",
    output_path="./output",
    text_field="text"
)
fuzzy_workflow.run()
ray.shutdown()

# For smaller datasets - use exact deduplication
exact_workflow = ExactDeduplicationWorkflow(
    input_path="/path/to/processed/data",
    output_path="./output",
    text_field="text",
    assign_id=True
)
exact_workflow.run()
ray.shutdown()
```

## Advanced Usage Patterns

### GPU-Accelerated Processing

For faster processing when GPUs are available (some operations require GPU):

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends.ray.executor import RayExecutor
from nemo_curator.stages.text.io.reader import JsonlReader

# Create pipeline with GPU-accelerated executor
pipeline = Pipeline(name="gpu_processing")

# Read data with GPU backend support
reader = JsonlReader(
    file_paths="data/*.jsonl",
    read_kwargs={"engine": "pyarrow", "dtype_backend": "pyarrow"}
)
pipeline.add_stage(reader)

# Add processing stages (same as before)
# ... add your processing stages ...

# Execute with Ray GPU executor for acceleration
executor = RayExecutor(
    num_gpus=4,
    rmm_pool_size="4GB",
    enable_spilling=True
)
processed_results = pipeline.run(executor)
```

**GPU acceleration benefits**:
- **Required** for fuzzy deduplication operations
- Faster processing for classification and embedding operations
- More efficient memory usage with RMM for large datasets
- Significant speedup for MinHash and LSH operations (16x faster for fuzzy deduplication)

### Multi-Node Distributed Processing

For production-scale data processing across multiple machines:

```python
import ray
from nemo_curator.stages.deduplication.fuzzy.workflow import FuzzyDeduplicationWorkflow
from nemo_curator.stages.text.deduplication.semantic import TextSemanticDeduplicationWorkflow
from nemo_curator.backends.xenna import XennaExecutor

# Initialize Ray cluster for distributed processing
ray.init(address="ray://scheduler-node:10001")

# Apply fuzzy deduplication at scale (most common large-scale operation)
fuzzy_workflow = FuzzyDeduplicationWorkflow(
    input_path="/path/to/large_data",
    cache_path="./cache",
    output_path="./output",
    text_field="text",
    # Tuned for high-precision deduplication
    num_bands=25,
    minhashes_per_band=10,
    char_ngrams=24
)
fuzzy_workflow.run()

# For semantic deduplication with text embedding generation
text_sem_workflow = TextSemanticDeduplicationWorkflow(
    input_path="/path/to/text_data",
    output_path="./sem_output",
    cache_path="./sem_cache", 
    text_field="text",
    model_identifier="sentence-transformers/all-MiniLM-L6-v2",
    n_clusters=1000,  # More clusters for large datasets
    perform_removal=False
)
text_sem_workflow.run(XennaExecutor())

# Results are written to output directories
# Process removal IDs separately if needed
ray.shutdown()
```

### Domain-Specific Processing

Common patterns for specialized content:

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends.xenna.executor import XennaExecutor

# Web crawl data processing (very common)
def build_web_pipeline():
    pipeline = Pipeline(name="web_processing")
    
    # Web pages are longer
    word_filter = ScoreFilter(
        score_fn=WordCountFilter(min_words=100),
        text_field="text"
    )
    pipeline.add_stage(word_filter)
    
    # More lenient for web content
    alpha_filter = ScoreFilter(
        score_fn=NonAlphaNumericFilter(max_non_alpha_numeric_to_text_ratio=0.3),
        text_field="text"
    )
    pipeline.add_stage(alpha_filter)
    
    # Remove navigation/footers
    boilerplate_filter = ScoreFilter(
        score_fn=BoilerPlateStringFilter(),
        text_field="text"
    )
    pipeline.add_stage(boilerplate_filter)
    
    # Limit URL-heavy content
    url_filter = ScoreFilter(
        score_fn=UrlsFilter(max_url_to_text_ratio=0.2),
        text_field="text"
    )
    pipeline.add_stage(url_filter)
    
    return pipeline

# Code dataset processing
def build_code_pipeline():
    pipeline = Pipeline(name="code_processing")
    
    # Code has symbols
    alpha_filter = ScoreFilter(
        score_fn=AlphaFilter(min_alpha_ratio=0.25),
        text_field="text"
    )
    pipeline.add_stage(alpha_filter)
    
    # Reasonable file sizes
    token_filter = ScoreFilter(
        score_fn=TokenCountFilter(min_tokens=20),
        text_field="text"
    )
    pipeline.add_stage(token_filter)
    
    return pipeline

# Academic/research content
def build_academic_pipeline():
    pipeline = Pipeline(name="academic_processing")
    
    # Academic papers are longer
    word_filter = ScoreFilter(
        score_fn=WordCountFilter(min_words=500),
        text_field="text"
    )
    pipeline.add_stage(word_filter)
    
    # Domain-specific quality
    quality_filter = ScoreFilter(
        score_fn=FastTextQualityFilter(model="academic"),
        text_field="text"
    )
    pipeline.add_stage(quality_filter)
    
    return pipeline
```

### Configuration-Driven Processing

For reproducible production pipelines:

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends.xenna.executor import XennaExecutor

# Most production users define pipelines in configuration
def build_config_pipeline(config_file):
    """Build pipeline from YAML configuration"""
    # Load and parse configuration
    pipeline = Pipeline(name="config_driven")
    
    # Add reader stage
    reader = JsonlReader(file_paths="input_data/*.jsonl")
    pipeline.add_stage(reader)
    
    # Load and parse configuration to add filter stages
    filter_stages = build_filter_stages_from_config(config_file)
    for stage in filter_stages:
        pipeline.add_stage(stage)
    
    # Add writer stage
    writer = JsonlWriter(path="output_data/")
    pipeline.add_stage(writer)
    
    return pipeline

# Use configuration for consistent processing
config_pipeline = build_config_pipeline("production_filters.yaml")
executor = XennaExecutor()
processed_results = config_pipeline.run(executor)
```

## Performance Best Practices

### Scale-Based Approach Selection

```{list-table}
:header-rows: 1

* - Dataset Size
  - Recommended Approach
  - Key Considerations
* - **Small (<1GB)**
  - Single node, exact deduplication
  - CPU cluster suitable, GPU optional for speed
* - **Medium (1-100GB)**
  - Single node, fuzzy deduplication
  - GPU required for fuzzy deduplication operations  
* - **Large (>100GB)**
  - Multi-node cluster, optimized fuzzy dedup
  - Distributed processing with GPU acceleration
```

### Hardware-Based Recommendations

```{list-table}
:header-rows: 1

* - Available Hardware
  - Recommended Setup
  - Performance Benefits
* - **GPU Available**
  - `get_client(cluster_type="gpu")`
  - Required for fuzzy deduplication, faster classification and embeddings
* - **CPU Only**
  - `get_client()` (default)
  - Good performance for filtering and exact deduplication
* - **Multi-Node Cluster**
  - `get_client(scheduler_address="...")`
  - Scales to massive datasets, distributes compute across nodes
```

### Production Optimization Guidelines

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends.xenna.executor import XennaExecutor

# Create optimized production pipeline
pipeline = Pipeline(name="optimized_production")

# Add reader stage
reader = JsonlReader(file_paths="data/*.jsonl")
pipeline.add_stage(reader)

# 1. Order operations by computational cost (most important optimization)
# Cheapest operations first (filter out bad data early)
word_filter = ScoreFilter(
    score_fn=WordCountFilter(min_words=10),  # Very fast
    text_field="text"
)
pipeline.add_stage(word_filter)

alpha_filter = ScoreFilter(
    score_fn=NonAlphaNumericFilter(),  # Fast
    text_field="text"
)
pipeline.add_stage(alpha_filter)

repeated_filter = ScoreFilter(
    score_fn=RepeatedLinesFilter(),  # Medium cost
    text_field="text"
)
pipeline.add_stage(repeated_filter)

# More expensive operations on remaining data
quality_filter = ScoreFilter(
    score_fn=FastTextQualityFilter(),  # Benefits from GPU acceleration
    text_field="text"
)
pipeline.add_stage(quality_filter)

# 3. Batch processing for memory efficiency
writer = JsonlWriter(
    path="output/",
    write_kwargs={"files_per_partition": 1}  # Control output partitioning
)
pipeline.add_stage(writer)

# Execute pipeline
executor = XennaExecutor()
processed_results = pipeline.run(executor)
```

### Advanced Client Configuration

For specialized use cases, configure the client with specific parameters:

```python
# GPU acceleration for operations that support or require it
gpu_executor = RayExecutor(
    num_gpus=4,
    rmm_pool_size="8GB",
    enable_spilling=True,
    set_torch_to_use_rmm=True
)

# Multi-node production cluster
distributed_executor = RayExecutor(
    scheduler_address="tcp://scheduler-node:8786"
)

# Custom CPU cluster configuration
cpu_executor = XennaExecutor(
    n_workers=16,
    threads_per_worker=2,
    memory_limit="8GB"
)
```

## Command Line Usage

Most production users prefer command-line tools for automation. All NeMo Curator scripts automatically set up distributed processing:

```bash
# Most common: Basic quality filtering (uses get_client internally)
filter_documents \
  --input-data-dir=input/ \
  --filter-config-file=heuristic_filters.yaml \
  --output-retained-document-dir=output/ \
  --device=cpu \
  --num-workers=8

# GPU acceleration for faster processing
filter_documents \
  --input-data-dir=input/ \
  --filter-config-file=heuristic_filters.yaml \
  --output-retained-document-dir=output/ \
  --device=gpu

# Large-scale: Fuzzy deduplication (4-step process)
# Step 1: Compute minhashes
gpu_compute_minhashes \
  --input-data-dir=input/ \
  --output-minhash-dir=minhashes/ \
  --cache-dir=cache/ \
  --device=gpu

# Step 2: LSH bucketing  
minhash_buckets \
  --input-minhash-dir=minhashes/ \
  --output-bucket-dir=buckets/ \
  --cache-dir=cache/

# Step 3: Find duplicate pairs
buckets_to_edges \
  --input-bucket-dir=buckets/ \
  --output-dir=edges/ \
  --cache-dir=cache/

# Step 4: Remove duplicates
gpu_connected_component \
  --input-edges-dir=edges/ \
  --output-dir=deduplicated/ \
  --cache-dir=cache/

# Multi-node processing using scheduler
filter_documents \
  --input-data-dir=input/ \
  --filter-config-file=heuristic_filters.yaml \
  --output-retained-document-dir=output/ \
  --scheduler-address=tcp://scheduler-node:8786
```

### Common Command Line Options

All NeMo Curator scripts support these distributed processing options:

- `--device`: Choose `cpu` or `gpu` for processing (default: `cpu`)
- `--num-workers`: Number of workers for local processing (default: CPU count)
- `--scheduler-address`: Connect to existing distributed cluster
- `--scheduler-file`: Path to Dask scheduler file
- `--threads-per-worker`: Threads per worker (default: `1`)

These options automatically configure `get_client()` with the appropriate parameters.
