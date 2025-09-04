---
description: "Perform automatic speech recognition using NeMo Framework models with GPU acceleration and batch processing"
categories: ["audio-processing"]
tags: ["asr-inference", "nemo-models", "speech-recognition", "gpu-accelerated", "batch-processing"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "how-to"
modality: "audio-only"
---

# ASR Inference

Perform automatic speech recognition (ASR) on audio files using NeMo Framework's pretrained models. The ASR inference stage transcribes audio into text, enabling downstream quality assessment and text processing workflows.

## How it Works

The `InferenceAsrNemoStage` processes `AudioBatch` objects by:

1. **Model Loading**: Downloads and initializes NeMo ASR models on GPU or CPU
2. **Batch Processing**: Groups audio files for efficient inference
3. **Transcription**: Generates text predictions for each audio file
4. **Output Creation**: Returns `AudioBatch` with original data plus predicted transcriptions

## Basic Usage

### Simple ASR Inference

```python
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.stages.resources import Resources

# Create ASR inference stage
asr_stage = InferenceAsrNemoStage(
    model_name="nvidia/stt_en_fastconformer_hybrid_large_pc",
    filepath_key="audio_filepath",
    pred_text_key="pred_text"
)

# Configure for GPU processing
asr_stage = asr_stage.with_(
    resources=Resources(gpus=1.0),
    batch_size=16
)
```

### Multilingual ASR

```python
# Use language-specific models
language_models = {
    "en_us": "nvidia/stt_en_fastconformer_hybrid_large_pc",
    "es_419": "nvidia/stt_es_fastconformer_hybrid_large_pc", 
    "hy_am": "nvidia/stt_hy_fastconformer_hybrid_large_pc",
}

# Create stage for Armenian
armenian_asr = InferenceAsrNemoStage(
    model_name=language_models["hy_am"]
)
```

## Configuration Options

### Model Selection

NeMo Framework provides pretrained ASR models for multiple languages and domains:

```python
# Domain-specific models
models = {
    "general": "nvidia/stt_en_fastconformer_hybrid_large_pc",
    "telephony": "nvidia/stt_en_fastconformer_telephony_large",
    "streaming": "nvidia/stt_en_fastconformer_streaming_large",
}
```

### Resource Configuration

```python
from nemo_curator.stages.resources import Resources

# GPU configuration
asr_stage = asr_stage.with_(
    resources=Resources(
        gpus=1.0,           # Number of GPUs
        cpus=4.0,           # CPU cores
        memory="16GB"       # Memory allocation
    )
)
```

### Batch Processing

```python
# Optimize batch size based on GPU memory
asr_stage = asr_stage.with_(
    batch_size=32  # Larger batches for better GPU utilization
)
```

## Input Requirements

### AudioBatch Format

Input `AudioBatch` objects must contain:

```python
audio_batch = AudioBatch(
    data=[
        {
            "audio_filepath": "/path/to/audio1.wav",
            # Optional: existing metadata
            "duration": 5.2,
            "language": "en"
        },
        {
            "audio_filepath": "/path/to/audio2.wav",
            "duration": 3.8,
            "language": "en"
        }
    ],
    filepath_key="audio_filepath"
)
```

### Audio File Requirements

- **Supported Formats**: WAV, MP3, FLAC, OGG (any format supported by NeMo Framework)
- **Sample Rates**: 16 kHz recommended (models handle resampling automatically)
- **Channels**: Mono or stereo (converted to mono during processing)
- **Duration**: No strict limits, but very long files may require chunking

## Output Structure

The ASR stage adds predicted transcriptions to each audio sample:

```python
# Output AudioBatch structure
{
    "audio_filepath": "/path/to/audio1.wav",
    "pred_text": "this is the predicted transcription",
    "duration": 5.2,  # Preserved from input
    "language": "en"  # Preserved from input
}
```

## Error Handling

### Model Loading Errors

```python
try:
    asr_stage.setup()
except RuntimeError as e:
    print(f"Failed to load ASR model: {e}")
    # Fallback to CPU or different model
```

### Processing Errors

The stage handles common audio processing errors:

- **Corrupted audio files**: Skipped with warning logs
- **Unsupported formats**: Graceful failure with error metadata
- **GPU memory issues**: Automatic batch size reduction
- **Network timeouts**: Model download retry logic

## Performance Optimization

### GPU Memory Management

```python
# For large models or limited GPU memory
asr_stage = InferenceAsrNemoStage(
    model_name="nvidia/stt_en_fastconformer_hybrid_large_pc"
).with_(
    batch_size=8,  # Reduce batch size
    resources=Resources(gpus=0.5)  # Share GPU resources
)
```

### Distributed Processing

```python
from nemo_curator.backends.xenna import XennaExecutor

# Configure for multi-GPU processing
executor = XennaExecutor(
    num_workers=4,
    resources_per_worker=Resources(gpus=1.0)
)
```

## Integration Examples

### Complete Audio-to-Text Pipeline

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.audio.io.convert import AudioToDocumentStage

pipeline = Pipeline(name="audio_to_text")

# ASR inference
pipeline.add_stage(asr_stage)

# Convert to text format
pipeline.add_stage(AudioToDocumentStage())

# Continue with text processing...
```

## Related Topics

- **[NeMo ASR Models](nemo-models.md)** - Available models and selection guide
- **[Batch Processing](batch-processing.md)** - Optimization strategies for large datasets
- **[Quality Assessment](../quality-assessment/index.md)** - Evaluate transcription accuracy
- **[Text Integration](../text-integration/index.md)** - Convert to text processing workflows

```{toctree}
:maxdepth: 2
:titlesonly:
:hidden:

NeMo ASR Models <nemo-models.md>
Batch Processing <batch-processing.md>
```

