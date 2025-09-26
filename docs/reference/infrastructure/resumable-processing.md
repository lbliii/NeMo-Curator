---
description: "Implementation guide for resumable processing to handle interrupted large-scale data operations in NeMo Curator"
categories: ["reference"]
tags: ["batch-processing", "large-scale", "optimization", "python-api", "configuration", "monitoring"]
personas: ["mle-focused", "admin-focused"]
difficulty: "intermediate"
content_type: "reference"
modality: "universal"
---

(reference-infra-resumable-processing)=

# Resumable Processing

This guide explains strategies to make large-scale data operations resumable.

## Why Resumable Processing Matters

Large datasets can trigger interruptions due to:
- System timeouts
- Hardware failures
- Network issues
- Resource constraints
- Scheduled maintenance

NeMo Curator provides built-in functionality for resuming operations from where they left off.

## Practical Patterns for Resumable Processing

### 1. Identify remaining files by comparing directories

Use file listing utilities and deterministic output naming to skip already processed inputs:

```python
from nemo_curator.utils.file_utils import get_file_paths

input_files = set(get_file_paths("input_directory/", recursive=True, extensions=[".jsonl"]))
output_files = set(get_file_paths("output_directory/", recursive=True, extensions=[".jsonl"]))

# Example: outputs mirror input filenames in the output directory
def corresponding_output_path(input_path: str) -> str:
    # Implement your mapping from input path to output path
    ...

remaining_inputs = [f for f in input_files if corresponding_output_path(f) not in output_files]

# Process remaining inputs using Pipeline API
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.text.io.reader import JsonlReader
from nemo_curator.stages.text.io.writer import JsonlWriter

for chunk in chunk_list(remaining_inputs, chunk_size=64):
    pipeline = Pipeline(name=f"resumable_chunk_{hash(tuple(chunk))}")
    
    # Read chunk files
    reader = JsonlReader(file_paths=chunk, fields=["text", "id"])
    pipeline.add_stage(reader)
    
    # Add your processing stages
    pipeline.add_stage(my_processor)
    
    # Write results
    writer = JsonlWriter(path="output_directory/", write_to_filename=True)
    pipeline.add_stage(writer)
    
    # Execute pipeline
    pipeline.run()
```

### 2. Batch processing of remaining files

Chunk remaining files to control memory and checkpoint progress frequently:

```python
def chunk_list(items: list[str], chunk_size: int) -> list[list[str]]:
    return [items[i:i+chunk_size] for i in range(0, len(items), chunk_size)]

for file_batch in chunk_list(remaining_inputs, chunk_size=64):
    pipeline = Pipeline(name=f"batch_{hash(tuple(file_batch))}")
    
    reader = JsonlReader(file_paths=file_batch, fields=["text", "id"])
    pipeline.add_stage(reader)
    pipeline.add_stage(my_processor)
    
    writer = JsonlWriter(path="output_directory/", write_to_filename=True)
    pipeline.add_stage(writer)
    
    pipeline.run()
```

## How Resumable Processing Works

The resumption approach works by:

1. Examining filenames in the input directory
2. Comparing them with filenames in the output directory
3. Identifying files that exist in the input but not in the output directory
4. Processing only those unprocessed files

This approach works best when you:
- Use `add_filename=True` when reading files
- Use `write_to_filename=True` when writing files
- Keep consistent filename patterns between input and output

## Best Practices for Resumable Processing

1. **Preserve filenames**: Use `add_filename=True` when reading files and `write_to_filename=True` when writing.

2. **Batch appropriately**: Choose batch sizes that balance memory usage and processing efficiency.

3. **Write checkpoints**: For complex pipelines, write intermediate results to disk.

4. **Test resume behavior**: Verify that your process resumes after simulated interruptions.

5. **Track disk space**: Ensure enough storage for input and output files.

6. **Log progress**: Maintain logs of processed files to help diagnose issues.
