---
description: "Audio processing tutorial using the FLEURS dataset"
categories: ["tutorials"]
tags: ["audio-tutorials", "fleurs-dataset", "asr-inference"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "beginner"
content_type: "tutorial"
modality: "audio-only"
---

# Audio Processing Tutorial

Learn audio processing with NeMo Curator through a working example using the FLEURS multilingual speech dataset.

## Available Tutorial

### FLEURS Dataset Processing

The complete working tutorial demonstrates the full audio processing workflow:

**Location**: `tutorials/audio/fleurs/`

**What it covers**:
- Loading the FLEURS multilingual speech dataset
- ASR inference using NeMo models
- WER calculation and quality assessment
- Duration analysis and filtering
- Exporting processed results

**Files**:
- `pipeline.py` - Complete pipeline implementation
- `run.py` - Command-line interface
- `pipeline.yaml` - Configuration options
- `README.md` - Setup and usage instructions

### Running the Tutorial

```bash
cd tutorials/audio/fleurs/

# Run with default settings (Armenian, dev split)
python run.py --raw_data_dir /data/fleurs_output

# Customize language and model
python run.py \
    --raw_data_dir /data/fleurs_output \
    --lang ko_kr \
    --split train \
    --model_name nvidia/stt_ko_fastconformer_hybrid_large_pc \
    --wer_threshold 50.0
```

## Tutorial Pipeline Overview

The FLEURS tutorial implements this processing flow:

1. **Data Loading**: Download and extract FLEURS dataset files
2. **ASR Inference**: Transcribe audio using NeMo ASR models
3. **Quality Assessment**: Calculate WER between ground truth and predictions
4. **Duration Analysis**: Extract audio file duration
5. **Filtering**: Keep only samples below WER threshold
6. **Export**: Save results in JSONL format

## Key Stages Used

```python
# Load FLEURS dataset
CreateInitialManifestFleursStage(lang="hy_am", split="dev", raw_data_dir="/data")

# ASR inference
InferenceAsrNemoStage(model_name="nvidia/stt_hy_fastconformer_hybrid_large_pc")

# Quality metrics
GetPairwiseWerStage(text_key="text", pred_text_key="pred_text", wer_key="wer")
GetAudioDurationStage(audio_filepath_key="audio_filepath", duration_key="duration")

# Filtering
PreserveByValueStage(input_value_key="wer", target_value=75.0, operator="le")

# Export
AudioToDocumentStage()
JsonlWriter(path="/output/results")
```

## Prerequisites

- NeMo Curator installed
- NVIDIA GPU (recommended for ASR inference)
- Internet connection (for dataset download)
- Python 3.8+

## Expected Output

The tutorial produces:
- Processed audio manifest with transcriptions
- WER scores for quality assessment
- Filtered dataset based on quality thresholds
- JSONL export ready for downstream use

## Customization

You can adapt the tutorial for your own datasets by:
- Replacing `CreateInitialManifestFleursStage` with `JsonlReader` for custom manifests
- Changing the ASR model for different languages
- Adjusting quality thresholds
- Adding custom filtering stages

## Related Topics

- **[Audio Processing Overview](../index.md)** - Complete audio processing capabilities
- **[Custom Manifests](../load-data/custom-manifests.md)** - Creating manifests for your own data
- **[ASR Inference](../process-data/asr-inference/index.md)** - ASR model configuration