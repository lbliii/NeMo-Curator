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

To process local audio files with NeMo Curator, you need to:

1. **Create a Manifest**: Generate a JSONL manifest file that lists your audio files and transcriptions
2. **Load with JsonlReader**: Use the built-in reader to load your manifest into the pipeline
3. **Process**: Apply audio processing stages like ASR inference and quality assessment

## Supported Audio Formats

NeMo Curator supports audio formats compatible with the soundfile library:

| Format | Extension | Description | Recommended Use |
|--------|-----------|-------------|-----------------|
| WAV | `.wav` | Uncompressed, high quality | ASR training, high-quality datasets |
| FLAC | `.flac` | Lossless compression | Archival, high-quality with compression |
| MP3 | `.mp3` | Lossy compression | Web content, podcasts |
| OGG | `.ogg` | Open-source compression | General purpose |

:::{note}
MP3 (`.mp3`) support depends on your system's libsndfile build. For the most reliable behavior across environments, prefer WAV (`.wav`) or FLAC (`.flac`) formats.
:::

## Creating Manifests for Local Files

### Basic Manifest Creation

Create a JSONL manifest that references your local audio files:

```python
import json
import os
from pathlib import Path

def create_local_manifest(audio_dir: str, output_manifest: str):
    """Create manifest from local audio directory."""
    
    audio_path = Path(audio_dir)
    manifest_entries = []
    
    # Find all WAV files
    for audio_file in audio_path.rglob("*.wav"):
        # Look for corresponding transcript file
        transcript_file = audio_file.with_suffix(".txt")
        
        if transcript_file.exists():
            # Read transcription
            with open(transcript_file, 'r', encoding='utf-8') as f:
                transcription = f.read().strip()
            
            # Create manifest entry
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

# Usage
create_local_manifest(
    audio_dir="/path/to/your/audio/files",
    output_manifest="local_audio_manifest.jsonl"
)
```

### Directory Organization Examples

**Paired Audio-Text Files**:
```
/data/my_speech/
├── sample_001.wav
├── sample_001.txt
├── sample_002.wav
├── sample_002.txt
└── ...
```

**Separated Directories**:
```
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

## Loading in Pipelines

### Complete Local File Processing

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.text.io.reader import JsonlReader
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.stages.audio.metrics.get_wer import GetPairwiseWerStage
from nemo_curator.stages.audio.common import GetAudioDurationStage, PreserveByValueStage
from nemo_curator.stages.audio.io.convert import AudioToDocumentStage
from nemo_curator.stages.text.io.writer import JsonlWriter

def create_local_audio_pipeline(manifest_path: str, output_dir: str) -> Pipeline:
    """Create pipeline for processing local audio files."""
    
    pipeline = Pipeline(name="local_audio_processing")
    
    # Load local manifest
    pipeline.add_stage(JsonlReader(
        file_paths=manifest_path,
        fields=["audio_filepath", "text"]
    ))
    
    # ASR processing
    pipeline.add_stage(InferenceAsrNemoStage(
        model_name="nvidia/stt_en_fastconformer_hybrid_large_pc"
    ))
    
    # Quality assessment
    pipeline.add_stage(GetPairwiseWerStage())
    pipeline.add_stage(GetAudioDurationStage(
        audio_filepath_key="audio_filepath",
        duration_key="duration"
    ))
    
    # Filter by quality
    pipeline.add_stage(PreserveByValueStage(
        input_value_key="wer",
        target_value=50.0,
        operator="le"
    ))
    
    # Export results
    pipeline.add_stage(AudioToDocumentStage())
    pipeline.add_stage(JsonlWriter(path=output_dir))
    
    return pipeline

# Usage
pipeline = create_local_audio_pipeline(
    manifest_path="local_audio_manifest.jsonl",
    output_dir="/output/processed_local_audio"
)
```

### Audio-Only Processing (No Ground Truth)

If you don't have transcriptions and only want ASR inference:

```python
def create_transcription_pipeline(manifest_path: str, output_dir: str) -> Pipeline:
    """Pipeline for transcription-only processing (no ground truth)."""
    
    pipeline = Pipeline(name="transcription_only")
    
    # Load manifest with just audio files
    pipeline.add_stage(JsonlReader(
        file_paths=manifest_path,
        fields=["audio_filepath"]
    ))
    
    # ASR inference
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

# Create audio-only manifest
audio_only_entries = [
    {"audio_filepath": "/path/to/audio1.wav"},
    {"audio_filepath": "/path/to/audio2.wav"},
]

with open("audio_only_manifest.jsonl", "w") as f:
    for entry in audio_only_entries:
        f.write(json.dumps(entry) + "\n")
```

## File Validation

The `AudioBatch` automatically validates file existence:

```python
from nemo_curator.tasks import AudioBatch

# Test file validation
test_batch = AudioBatch(
    data=[
        {"audio_filepath": "/path/to/existing/file.wav", "text": "test"},
        {"audio_filepath": "/path/to/missing/file.wav", "text": "test"}
    ],
    filepath_key="audio_filepath"
)

# Validation will log warnings for missing files
is_valid = test_batch.validate()
print(f"Batch validation: {is_valid}")
```

## Best Practices

### File Path Management

Use absolute paths for reliability:

```python
import os

# Convert to absolute path
audio_file = "/relative/path/to/audio.wav"
absolute_path = os.path.abspath(audio_file)
```

### Batch Size Considerations

For large local datasets, consider processing in smaller batches:

```python
# Process in smaller chunks for memory efficiency
def create_batched_manifest(audio_files: list, batch_size: int = 100):
    """Create multiple smaller manifest files."""
    
    for i in range(0, len(audio_files), batch_size):
        batch = audio_files[i:i + batch_size]
        batch_manifest = f"local_batch_{i//batch_size:04d}.jsonl"
        
        with open(batch_manifest, "w") as f:
            for entry in batch:
                f.write(json.dumps(entry) + "\n")
```

## Error Handling

Handle common issues with local files:

```python
import os
import json

def create_robust_manifest(audio_dir: str, output_manifest: str):
    """Create manifest with error handling."""
    
    valid_entries = []
    error_count = 0
    
    for audio_file in Path(audio_dir).rglob("*.wav"):
        try:
            # Check if file is accessible
            if not os.access(audio_file, os.R_OK):
                print(f"Warning: Cannot read {audio_file}")
                error_count += 1
                continue
            
            # Look for transcription
            transcript_file = audio_file.with_suffix(".txt")
            if transcript_file.exists():
                with open(transcript_file, 'r', encoding='utf-8') as f:
                    transcription = f.read().strip()
                
                if transcription:  # Skip empty transcriptions
                    entry = {
                        "audio_filepath": str(audio_file.absolute()),
                        "text": transcription
                    }
                    valid_entries.append(entry)
                else:
                    error_count += 1
            else:
                error_count += 1
                
        except Exception as e:
            print(f"Error processing {audio_file}: {e}")
            error_count += 1
    
    # Write valid entries
    with open(output_manifest, 'w', encoding='utf-8') as f:
        for entry in valid_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    print(f"Created manifest: {len(valid_entries)} valid, {error_count} errors")
```

## Complete Example

```python
#!/usr/bin/env python3
"""Complete example: Process local audio files with NeMo Curator."""

import json
import os
from pathlib import Path
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.text.io.reader import JsonlReader
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.stages.audio.common import GetAudioDurationStage
from nemo_curator.stages.audio.io.convert import AudioToDocumentStage
from nemo_curator.stages.text.io.writer import JsonlWriter
from nemo_curator.backends.xenna import XennaExecutor

def process_local_audio_collection(audio_dir: str, output_dir: str):
    """Complete workflow for local audio processing."""
    
    # Step 1: Create manifest
    manifest_path = os.path.join(output_dir, "local_manifest.jsonl")
    create_local_manifest(audio_dir, manifest_path)
    
    # Step 2: Create pipeline
    pipeline = Pipeline(name="local_audio_complete")
    
    pipeline.add_stage(JsonlReader(
        file_paths=manifest_path,
        fields=["audio_filepath", "text"]
    ))
    
    pipeline.add_stage(InferenceAsrNemoStage(
        model_name="nvidia/stt_en_fastconformer_hybrid_large_pc"
    ))
    
    pipeline.add_stage(GetAudioDurationStage(
        audio_filepath_key="audio_filepath",
        duration_key="duration"
    ))
    
    pipeline.add_stage(AudioToDocumentStage())
    pipeline.add_stage(JsonlWriter(
        path=os.path.join(output_dir, "transcription_results")
    ))
    
    # Step 3: Execute
    executor = XennaExecutor()
    pipeline.run(executor)
    
    print(f"Processing complete. Results in {output_dir}")

if __name__ == "__main__":
    process_local_audio_collection(
        audio_dir="/path/to/your/audio/files",
        output_dir="/path/to/output"
    )
```

## Related Topics

- **[Custom Manifests](custom-manifests.md)** - Detailed manifest format specification
- **[FLEURS Dataset](fleurs-dataset.md)** - Example of automated dataset loading
- **[Audio Processing Overview](../../index.md)** - Complete audio processing workflow