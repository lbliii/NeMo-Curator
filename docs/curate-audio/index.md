---
description: "Basic audio processing capabilities for ASR inference, quality assessment, and filtering using NeMo models"
categories: ["workflows"]
tags: ["audio-processing", "asr", "speech-recognition", "quality-filtering", "transcription"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "beginner"
content_type: "workflow"
modality: "audio-only"
---

(audio-overview)=
# About Audio Processing

NeMo Curator provides basic audio processing capabilities for speech datasets. The toolkit includes stages for ASR inference using NeMo models, quality assessment through WER calculation, and filtering based on transcription accuracy.

## Available Functionality

NeMo Curator provides these core audio processing capabilities:

- **ASR Inference**: Transcribe audio using pretrained NeMo ASR models
- **Quality Assessment**: Calculate WER between ground truth and ASR predictions  
- **Duration Analysis**: Extract audio file duration and filter by length
- **Format Handling**: Built-in support for WAV, FLAC, MP3, and other common formats
- **Data Export**: Convert results to text processing format for further curation

## Available Stages

NeMo Curator provides these audio processing stages:

- **`InferenceAsrNemoStage`**: ASR inference using NeMo Framework models
- **`GetPairwiseWerStage`**: Calculate WER between ground truth and predictions  
- **`GetAudioDurationStage`**: Extract audio file duration using soundfile
- **`PreserveByValueStage`**: Filter data based on numeric thresholds
- **`AudioToDocumentStage`**: Convert AudioBatch to DocumentBatch for export
- **`CreateInitialManifestFleursStage`**: Load FLEURS multilingual dataset

## Getting Started

### Load Data

Load audio data into NeMo Curator for processing:

- **[FLEURS Dataset](load-data/fleurs-dataset.md)** - Automated multilingual speech dataset loading
- **[Custom Manifests](load-data/custom-manifests.md)** - Create JSONL manifests for your audio files  
- **[Local Files](load-data/local-files.md)** - Process audio files from local directories

### Process Data

Apply audio processing stages to your data:

- **[ASR Inference](process-data/asr-inference/index.md)** - Transcribe audio using NeMo ASR models
- **[Quality Assessment](process-data/quality-assessment/index.md)** - Calculate WER and filter by quality
- **[Audio Analysis](process-data/audio-analysis/index.md)** - Extract duration and basic metadata
- **[Text Integration](process-data/text-integration/index.md)** - Convert to DocumentBatch for export

## Working Example

The FLEURS tutorial demonstrates the complete audio processing workflow:

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.audio.datasets.fleurs.create_initial_manifest import CreateInitialManifestFleursStage
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.stages.audio.metrics.get_wer import GetPairwiseWerStage
from nemo_curator.stages.audio.common import GetAudioDurationStage, PreserveByValueStage
from nemo_curator.stages.audio.io.convert import AudioToDocumentStage
from nemo_curator.stages.text.io.writer import JsonlWriter

# Create audio processing pipeline
pipeline = Pipeline(name="audio_processing")

# Load FLEURS dataset
pipeline.add_stage(CreateInitialManifestFleursStage(
    lang="hy_am", 
    split="dev", 
    raw_data_dir="/data/fleurs"
))

# ASR inference
pipeline.add_stage(InferenceAsrNemoStage(
    model_name="nvidia/stt_hy_fastconformer_hybrid_large_pc"
))

# Quality assessment
pipeline.add_stage(GetPairwiseWerStage())
pipeline.add_stage(GetAudioDurationStage(
    audio_filepath_key="audio_filepath", 
    duration_key="duration"
))

# Filter by WER threshold
pipeline.add_stage(PreserveByValueStage(
    input_value_key="wer", 
    target_value=75.0, 
    operator="le"
))

# Export results
pipeline.add_stage(AudioToDocumentStage())
pipeline.add_stage(JsonlWriter(path="/output/results"))
```

## Tutorials

- **[FLEURS Tutorial](tutorials/fleurs/)** - Complete working example using the FLEURS dataset
