---
description: "Load audio files from local directories by creating custom manifests"
categories: ["data-loading"]
tags: ["local-files", "custom-manifests", "audio-discovery"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "beginner"
content_type: "how-to"
modality: "audio-only"
---

(audio-load-data-local)=

# Load Local Audio Files

Load audio files from local directories by creating custom manifests that reference your audio files. This guide covers supported formats and basic approaches for organizing local audio data for NeMo Curator processing.

## Overview

To process local audio files with NeMo Curator, you can use built-in stages that automatically discover and process audio files:

1. **Discover Files**: Use `FilePartitioningStage` to automatically find audio files in directories
2. **Process Directly**: Apply audio processing stages like ASR inference that automatically create proper data structures
3. **Optional**: Create custom manifests for advanced use cases with existing transcriptions

## Supported Audio Formats

NeMo Curator supports audio formats compatible with the `soundfile` library:

| Format | Extension | Description | Recommended Use |
|--------|-----------|-------------|-----------------|
| WAV | `.wav` | Uncompressed, high quality | ASR training, high-quality datasets |
| FLAC | `.flac` | Lossless compression | Archival, high-quality with compression |
| MP3 | `.mp3` | Compressed format | Web content, podcasts |
| OGG | `.ogg` | Open-source compression | General purpose |

:::{note}
MP3 (`.mp3`) support depends on your system's `libsndfile` build. For the most reliable behavior across environments, prefer WAV (`.wav`) or FLAC (`.flac`) formats.
:::

## Processing Local Files with Built-in Stages

### Automatic File Discovery

Use the built-in `FilePartitioningStage` to automatically discover audio files in directories:

```python
from nemo_curator.stages.file_partitioning import FilePartitioningStage
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.pipeline import Pipeline
from nemo_curator.backends.xenna import XennaExecutor

def process_local_audio_directory(audio_dir: str, output_dir: str):
    """Process local audio directory with built-in stages."""
    
    pipeline = Pipeline(name="local_audio_processing")
    
    # Automatically discover audio files
    pipeline.add_stage(FilePartitioningStage(
        file_paths=audio_dir,
        file_extensions=[".wav", ".flac", ".mp3", ".ogg"],
        files_per_partition=50  # Process in batches of 50 files
    ))
    
    # ASR processing - automatically converts FileGroupTask to AudioBatch
    pipeline.add_stage(InferenceAsrNemoStage(
        model_name="nvidia/stt_en_fastconformer_hybrid_large_pc"
    ))
    
    # Execute pipeline
    executor = XennaExecutor()
    results = pipeline.run(executor)
    
    return results

# Usage
results = process_local_audio_directory(
    audio_dir="/path/to/your/audio/files",
    output_dir="/path/to/output"
)
```

### Directory Organization Examples

**Paired Audio-Text Files**:

```text
/data/my_speech/
├── sample_001.wav
├── sample_001.txt
├── sample_002.wav
├── sample_002.txt
└── ...
```

**Separated Directories**:

```text
/data/my_speech/
├── audio/
│   ├── sample_001.wav
│   ├── sample_002.wav
│   └── ...
└── transcripts/
    ├── sample_001.txt
    ├── sample_002.txt
    └── ...
```

### Complete Audio Processing Pipeline

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.file_partitioning import FilePartitioningStage
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.stages.audio.metrics.get_wer import GetPairwiseWerStage
from nemo_curator.stages.audio.common import GetAudioDurationStage, PreserveByValueStage
from nemo_curator.stages.audio.io.convert import AudioToDocumentStage
from nemo_curator.stages.text.io.writer import JsonlWriter
from nemo_curator.backends.xenna import XennaExecutor

def create_local_audio_pipeline(audio_dir: str, output_dir: str) -> Pipeline:
    """Create pipeline for processing local audio files."""
    
    pipeline = Pipeline(name="local_audio_processing")
    
    # Automatically discover audio files
    pipeline.add_stage(FilePartitioningStage(
        file_paths=audio_dir,
        file_extensions=[".wav", ".flac", ".mp3", ".ogg"],
        files_per_partition=50
    ))
    
    # ASR processing - automatically creates AudioBatch from FileGroupTask
    pipeline.add_stage(InferenceAsrNemoStage(
        model_name="nvidia/stt_en_fastconformer_hybrid_large_pc"
    ))
    
    # Audio analysis
    pipeline.add_stage(GetAudioDurationStage(
        audio_filepath_key="audio_filepath",
        duration_key="duration"
    ))
    
    # Filter by duration (example: keep files between 1-30 seconds)
    pipeline.add_stage(PreserveByValueStage(
        input_value_key="duration",
        target_value=30.0,
        operator="le"
    ))
    pipeline.add_stage(PreserveByValueStage(
        input_value_key="duration",
        target_value=1.0,
        operator="ge"
    ))
    
    # Export results
    pipeline.add_stage(AudioToDocumentStage())
    pipeline.add_stage(JsonlWriter(path=output_dir))
    
    return pipeline

# Usage
pipeline = create_local_audio_pipeline(
    audio_dir="/path/to/your/audio/files",
    output_dir="/output/processed_local_audio"
)

executor = XennaExecutor()
results = pipeline.run(executor)
```

### Transcription Processing

For transcription processing (no ground truth needed):

```python
def create_transcription_pipeline(audio_dir: str, output_dir: str) -> Pipeline:
    """Pipeline for transcription-only processing."""
    
    pipeline = Pipeline(name="transcription_only")
    
    # Discover audio files automatically
    pipeline.add_stage(FilePartitioningStage(
        file_paths=audio_dir,
        file_extensions=[".wav", ".flac", ".mp3", ".ogg"],
        files_per_partition=100
    ))
    
    # ASR inference - creates AudioBatch with transcriptions
    pipeline.add_stage(InferenceAsrNemoStage(
        model_name="nvidia/stt_en_fastconformer_hybrid_large_pc"
    ))
    
    # Duration analysis
    pipeline.add_stage(GetAudioDurationStage(
        audio_filepath_key="audio_filepath",
        duration_key="duration"
    ))
    
    # Export transcriptions
    pipeline.add_stage(AudioToDocumentStage())
    pipeline.add_stage(JsonlWriter(path=output_dir))
    
    return pipeline

# Usage
pipeline = create_transcription_pipeline(
    audio_dir="/path/to/your/audio/files",
    output_dir="/path/to/output"
)

executor = XennaExecutor()
results = pipeline.run(executor)
```

## File Validation

The built-in stages automatically handle file validation:

- `FilePartitioningStage` includes files that exist during discovery
- `AudioBatch` validates file existence and logs warnings for missing files
- `InferenceAsrNemoStage` handles file access errors properly

```python
from nemo_curator.tasks import AudioBatch

# AudioBatch automatically validates file existence
test_batch = AudioBatch(
    data=[
        {"audio_filepath": "/path/to/existing/file.wav", "text": "test"},
        {"audio_filepath": "/path/to/missing/file.wav", "text": "test"}
    ],
    filepath_key="audio_filepath"
)

# Validation logs warnings for missing files
is_valid = test_batch.validate()
print(f"Batch validation: {is_valid}")
```

## Best Practices

### File Discovery Options

The `FilePartitioningStage` supports flexible file discovery:

```python
# Recursive directory scanning
FilePartitioningStage(
    file_paths="/path/to/audio/root",
    file_extensions=[".wav", ".flac"],  # Filter by audio formats
    files_per_partition=50  # Batch size for processing
)

# Multiple directories
FilePartitioningStage(
    file_paths=["/path/to/dir1", "/path/to/dir2"],
    file_extensions=[".wav"],
    files_per_partition=100
)

# Single file
FilePartitioningStage(
    file_paths="/path/to/single/file.wav",
    files_per_partition=1
)
```

### Batch Size Considerations

Optimize batch sizes based on your system resources:

```python
# Small batches for limited memory
files_per_partition=25  # Process 25 files at a time

# Larger batches for high-memory systems
files_per_partition=200  # Process 200 files at a time

# Single file processing for very large files
files_per_partition=1
```

## Error Handling

The built-in stages provide robust error handling:

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.file_partitioning import FilePartitioningStage
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.backends.xenna import XennaExecutor

def create_robust_pipeline(audio_dir: str, output_dir: str):
    """Create pipeline with built-in error handling."""
    
    pipeline = Pipeline(name="robust_audio_processing")
    
    # FilePartitioningStage automatically filters out non-existent files
    pipeline.add_stage(FilePartitioningStage(
        file_paths=audio_dir,
        file_extensions=[".wav", ".flac", ".mp3", ".ogg"],
        files_per_partition=50
    ))
    
    # InferenceAsrNemoStage handles file access errors gracefully
    pipeline.add_stage(InferenceAsrNemoStage(
        model_name="nvidia/stt_en_fastconformer_hybrid_large_pc"
    ))
    
    try:
        executor = XennaExecutor()
        results = pipeline.run(executor)
        print(f"Processing completed successfully")
        return results
    except Exception as e:
        print(f"Pipeline error: {e}")
        return None

```python
# Built-in error handling features:
# - FilePartitioningStage skips inaccessible files
# - AudioBatch.validate() checks file existence
# - InferenceAsrNemoStage logs warnings for failed files
# - Pipeline execution continues with valid files
```

## Complete Example

```python
#!/usr/bin/env python3
"""Complete example: Process local audio files with NeMo Curator built-in stages."""

import os
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.file_partitioning import FilePartitioningStage
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.stages.audio.common import GetAudioDurationStage, PreserveByValueStage
from nemo_curator.stages.audio.io.convert import AudioToDocumentStage
from nemo_curator.stages.text.io.writer import JsonlWriter
from nemo_curator.backends.xenna import XennaExecutor

def process_local_audio_collection(audio_dir: str, output_dir: str):
    """Complete workflow for local audio processing using built-in stages."""
    
    # Create pipeline with automatic file discovery
    pipeline = Pipeline(name="local_audio_complete")
    
    # Step 1: Automatically discover audio files
    pipeline.add_stage(FilePartitioningStage(
        file_paths=audio_dir,
        file_extensions=[".wav", ".flac", ".mp3", ".ogg"],
        files_per_partition=50
    ))
    
    # Step 2: ASR inference (automatically creates AudioBatch)
    pipeline.add_stage(InferenceAsrNemoStage(
        model_name="nvidia/stt_en_fastconformer_hybrid_large_pc"
    ))
    
    # Step 3: Audio analysis
    pipeline.add_stage(GetAudioDurationStage(
        audio_filepath_key="audio_filepath",
        duration_key="duration"
    ))
    
    # Step 4: Quality filtering (optional)
    pipeline.add_stage(PreserveByValueStage(
        input_value_key="duration",
        target_value=30.0,  # Keep files <= 30 seconds
        operator="le"
    ))
    
    # Step 5: Export results
    pipeline.add_stage(AudioToDocumentStage())
    pipeline.add_stage(JsonlWriter(
        path=os.path.join(output_dir, "transcription_results")
    ))
    
    # Step 6: Execute
    executor = XennaExecutor()
    results = pipeline.run(executor)
    
    print(f"Processing complete. Results in {output_dir}")
    return results

if __name__ == "__main__":
    process_local_audio_collection(
        audio_dir="/path/to/your/audio/files",
        output_dir="/path/to/output"
    )
```

## Advanced: Custom Manifest Creation

For advanced use cases where you have existing transcriptions, you can create custom manifests:

```python
import json
from pathlib import Path

def create_custom_manifest(audio_dir: str, output_manifest: str):
    """Create custom manifest when you have existing transcriptions."""
    
    audio_path = Path(audio_dir)
    manifest_entries = []
    
    # Find audio files with corresponding text files
    for audio_file in audio_path.rglob("*.wav"):
        transcript_file = audio_file.with_suffix(".txt")
        
        if transcript_file.exists():
            with open(transcript_file, 'r', encoding='utf-8') as f:
                transcription = f.read().strip()
            
            entry = {
                "audio_filepath": str(audio_file.absolute()),
                "text": transcription
            }
            manifest_entries.append(entry)
    
    # Write JSONL manifest
    with open(output_manifest, 'w', encoding='utf-8') as f:
        for entry in manifest_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    print(f"Created manifest with {len(manifest_entries)} entries")

# Then use JsonlReader to load the custom manifest:
from nemo_curator.stages.text.io.reader import JsonlReader

pipeline.add_stage(JsonlReader(
    file_paths="custom_manifest.jsonl",
    fields=["audio_filepath", "text"]
))
```

## Related Topics

- **[Custom Manifests](custom-manifests.md)** - Detailed manifest format specification
- **[FLEURS Dataset](fleurs-dataset.md)** - Example of automated dataset loading
- **[Audio Processing Overview](../../index.md)** - Complete audio processing workflow