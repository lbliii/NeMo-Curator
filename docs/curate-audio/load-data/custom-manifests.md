---
description: "Create and load custom audio manifests with file paths, transcriptions, and metadata for specialized speech datasets"
categories: ["data-loading"]
tags: ["custom-manifests", "jsonl", "tsv", "audio-metadata", "speech-datasets"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "how-to"
modality: "audio-only"
---

(audio-load-data-custom-manifests)=
# Create and Load Custom Audio Manifests

Create and load custom audio manifests for your own speech datasets. This guide covers manifest formats, metadata requirements, and best practices for organizing audio data with NeMo Curator.

## Manifest Formats

NeMo Curator supports multiple manifest formats for audio data loading:

::::{tab-set}

:::{tab-item} JSONL (Recommended)

The standard format for audio manifests compatible with NeMo Framework:

```json
{"audio_filepath": "/data/audio/sample_001.wav", "text": "hello world", "duration": 2.1, "language": "en"}
{"audio_filepath": "/data/audio/sample_002.wav", "text": "good morning", "duration": 1.8, "language": "en"}
{"audio_filepath": "/data/audio/sample_003.wav", "text": "how are you", "duration": 2.3, "language": "en"}
```

:::

:::{tab-item} TSV

Tab-separated format useful for spreadsheet compatibility:

```bash
audio_filepath	text	duration	language
/data/audio/sample_001.wav	hello world	2.1	en
/data/audio/sample_002.wav	good morning	1.8	en
/data/audio/sample_003.wav	how are you	2.3	en
```

:::
::::

## Fields

::::{tab-set}

:::{tab-item} Minimum Requirements

Every audio manifest must include:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `audio_filepath` | string | Absolute or relative path to audio file | `/data/audio/sample.wav` |
| `text` | string | Ground truth transcription | `"hello world"` |

:::

:::{tab-item} Recommended Fields

Additional fields that enhance processing:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `duration` | float | Audio duration in seconds | `2.1` |
| `language` | string | Language identifier | `"en_us"` |
| `speaker_id` | string | Speaker identifier | `"speaker_001"` |
| `sample_rate` | int | Audio sample rate in Hz | `16000` |

:::
::::

## Creating Custom Manifests

::::{tab-set}

:::{tab-item} From Directory Structure

Create manifests from organized audio directories:

```python
import os
import json
import soundfile as sf
from pathlib import Path

def create_manifest_from_directory(audio_dir: str, output_manifest: str, 
                                 transcription_dir: str = None):
    """Create audio manifest from directory structure."""
    
    audio_path = Path(audio_dir)
    manifest_data = []
    
    for audio_file in audio_path.glob("**/*.wav"):
        # Get transcription file (same name, .txt extension)
        if transcription_dir:
            transcript_file = Path(transcription_dir) / (audio_file.stem + ".txt")
        else:
            transcript_file = audio_file.with_suffix(".txt")
        
        if transcript_file.exists():
            # Read transcription
            with open(transcript_file, 'r', encoding='utf-8') as f:
                text = f.read().strip()
            
            # Get audio duration
            try:
                data, samplerate = sf.read(str(audio_file))
                duration = len(data) / samplerate
            except:
                duration = -1.0  # Mark as invalid
            
            # Create manifest entry
            entry = {
                "audio_filepath": str(audio_file.absolute()),
                "text": text,
                "duration": duration,
                "sample_rate": samplerate if duration > 0 else None
            }
            manifest_data.append(entry)
    
    # Write manifest
    with open(output_manifest, 'w', encoding='utf-8') as f:
        for entry in manifest_data:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    print(f"Created manifest with {len(manifest_data)} entries")

# Usage
create_manifest_from_directory(
    audio_dir="/data/my_speech_dataset/audio",
    transcription_dir="/data/my_speech_dataset/transcripts", 
    output_manifest="/data/my_speech_dataset/manifest.jsonl"
)
```

:::

:::{tab-item} From Existing Datasets

Convert existing speech datasets to NeMo Curator format:

```python
import pandas as pd

def convert_librispeech_manifest(librispeech_csv: str, output_manifest: str):
    """Convert LibriSpeech-style CSV to NeMo Curator manifest."""
    
    df = pd.read_csv(librispeech_csv)
    
    manifest_entries = []
    for _, row in df.iterrows():
        entry = {
            "audio_filepath": row["file_path"],
            "text": row["transcription"].lower(),  # Normalize case
            "duration": row["duration"], 
            "speaker_id": row["speaker_id"],
            "chapter_id": row["chapter_id"]
        }
        manifest_entries.append(entry)
    
    # Write JSONL manifest
    with open(output_manifest, 'w') as f:
        for entry in manifest_entries:
            f.write(json.dumps(entry) + '\n')

# Usage
convert_librispeech_manifest(
    "librispeech_train.csv",
    "librispeech_train_manifest.jsonl"
)
```

:::

::::

## Loading Custom Manifests


::::{tab-set}

:::{tab-item} Direct Loading

Load existing manifests into NeMo Curator pipelines:

```python
from nemo_curator.stages.text.io.reader import JsonlReader
from nemo_curator.stages.audio.io.convert import DocumentToAudioStage

# Load JSONL manifest
reader = JsonlReader(path="/data/my_dataset/manifest.jsonl")

# Convert to AudioBatch format
audio_converter = DocumentToAudioStage(
    filepath_key="audio_filepath",
    text_key="text"
)
```

:::

:::{tab-item} Validation During Loading

```python
from nemo_curator.tasks import AudioBatch

def load_and_validate_manifest(manifest_path: str) -> list[AudioBatch]:
    """Load manifest with validation."""
    
    audio_batches = []
    invalid_count = 0
    
    with open(manifest_path, 'r') as f:
        batch_data = []
        
        for line_num, line in enumerate(f, 1):
            try:
                entry = json.loads(line)
                
                # Validate required fields
                if "audio_filepath" not in entry or "text" not in entry:
                    print(f"Line {line_num}: Missing required fields")
                    invalid_count += 1
                    continue
                
                # Validate file exists
                if not os.path.exists(entry["audio_filepath"]):
                    print(f"Line {line_num}: Audio file not found: {entry['audio_filepath']}")
                    invalid_count += 1
                    continue
                
                batch_data.append(entry)
                
                # Create batches of 100 entries
                if len(batch_data) >= 100:
                    audio_batches.append(AudioBatch(
                        data=batch_data,
                        filepath_key="audio_filepath"
                    ))
                    batch_data = []
                    
            except json.JSONDecodeError:
                print(f"Line {line_num}: Invalid JSON")
                invalid_count += 1
                continue
        
        # Handle remaining entries
        if batch_data:
            audio_batches.append(AudioBatch(
                data=batch_data,
                filepath_key="audio_filepath"
            ))
    
    print(f"Loaded {len(audio_batches)} batches, {invalid_count} invalid entries")
    return audio_batches
```

:::

::::

## Manifest Organization

::::{tab-set}

:::{tab-item} Multi-language Datasets

Organize manifests for multilingual speech data:

```
/data/multilingual_speech/
├── manifests/
│   ├── en_us_train.jsonl
│   ├── en_us_dev.jsonl
│   ├── es_419_train.jsonl
│   ├── es_419_dev.jsonl
│   └── ...
├── audio/
│   ├── en_us/
│   ├── es_419/
│   └── ...
└── metadata/
    ├── speaker_info.json
    └── language_stats.json
```

:::

:::{tab-item} Domain-specific Organization

```
/data/domain_speech/
├── telephony/
│   ├── manifest.jsonl
│   └── audio/
├── broadcast/
│   ├── manifest.jsonl  
│   └── audio/
└── conversational/
    ├── manifest.jsonl
    └── audio/
```

:::

::::

## Best Practices

::::{tab-set}

:::{tab-item} File Path Management

```python
# Use absolute paths for reliability
entry = {
    "audio_filepath": os.path.abspath("/data/audio/sample.wav"),
    "text": "transcription text"
}

# Or use relative paths with consistent base directory
entry = {
    "audio_filepath": "audio/sample.wav",  # Relative to manifest location
    "text": "transcription text"
}
```

:::

:::{tab-item} Text Normalization

```python
def normalize_transcription(text: str) -> str:
    """Normalize transcription text for consistency."""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra whitespace
    text = " ".join(text.split())
    
    # Optional: Remove punctuation for ASR training
    import string
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    return text

# Apply during manifest creation
entry["text"] = normalize_transcription(raw_transcription)
```

:::

:::{tab-item} Metadata Validation

```python
def validate_audio_entry(entry: dict) -> bool:
    """Validate audio manifest entry."""
    
    required_fields = ["audio_filepath", "text"]
    
    # Check required fields
    for field in required_fields:
        if field not in entry:
            return False
    
    # Validate audio file
    audio_path = entry["audio_filepath"]
    if not os.path.exists(audio_path):
        return False
    
    # Validate audio format
    try:
        sf.info(audio_path)
    except:
        return False
    
    # Validate transcription
    if not entry["text"].strip():
        return False
    
    return True
```

:::

::::

## Integration Examples

### Loading into Pipeline

```python
from nemo_curator.pipeline import Pipeline

def create_custom_audio_pipeline(manifest_path: str) -> Pipeline:
    """Create pipeline for custom audio manifest."""
    
    pipeline = Pipeline(name="custom_audio_processing")
    
    # Load custom manifest
    pipeline.add_stage(CustomManifestLoader(manifest_path))
    
    # Process with standard stages
    pipeline.add_stage(InferenceAsrNemoStage(
        model_name="nvidia/stt_en_fastconformer_hybrid_large_pc"
    ))
    
    pipeline.add_stage(GetPairwiseWerStage())
    
    # Filter based on custom criteria
    pipeline.add_stage(PreserveByValueStage("wer", 40.0, "le"))
    
    return pipeline
```
