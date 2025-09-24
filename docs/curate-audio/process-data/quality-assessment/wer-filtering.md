---
description: "Filter audio samples based on Word Error Rate thresholds to ensure high-quality transcription accuracy"
categories: ["audio-processing"]
tags: ["wer-filtering", "quality-filtering", "transcription-accuracy", "threshold-based", "speech-quality"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "beginner"
content_type: "how-to"
modality: "audio-only"
---

# WER Filtering

Filter audio samples based on Word Error Rate (WER) thresholds to ensure high-quality transcription accuracy in your speech datasets. WER filtering is the primary quality control mechanism for ASR-based audio curation.

## Understanding WER

### What is Word Error Rate?

Word Error Rate measures transcription accuracy by calculating the percentage of words that differ between ground truth and ASR predictions:

```text
WER = (Substitutions + Deletions + Insertions) / Total_Reference_Words × 100
```

### WER Quality Levels

| WER Range | Quality Level | Recommended Use |
|-----------|---------------|-----------------|
| 0-10% | Excellent | Production ASR training, high-quality datasets |
| 10-25% | Good | General ASR training, most applications |
| 25-50% | Moderate | Supplementary training data, domain adaptation |
| 50-75% | Poor | Review required, potential filtering |
| 75%+ | Very Poor | Strong candidate for removal |

## Basic WER Filtering

### Calculate WER

```python
from nemo_curator.stages.audio.metrics.get_wer import GetPairwiseWerStage

# Calculate WER for audio samples
wer_stage = GetPairwiseWerStage(
    text_key="text",           # Ground truth transcription
    pred_text_key="pred_text", # ASR model prediction
    wer_key="wer"             # Output field for WER value
)

# Add to pipeline
pipeline.add_stage(wer_stage)
```

### Apply WER Threshold

```python
from nemo_curator.stages.audio.common import PreserveByValueStage

# Keep samples with WER ≤ 30% (good quality)
wer_filter = PreserveByValueStage(
    input_value_key="wer",
    target_value=30.0,
    operator="le"  # less than or equal
)

pipeline.add_stage(wer_filter)
```

## Advanced WER Filtering

### Multi-Tier Filtering

```python
def create_multi_tier_wer_pipeline() -> Pipeline:
    """Create pipeline with multiple WER quality tiers."""
    from nemo_curator.stages.function_decorators import processing_stage
    
    pipeline = Pipeline(name="multi_tier_wer")
    
    # Calculate WER
    pipeline.add_stage(GetPairwiseWerStage())
    
    # Tier 1: Excellent quality (WER ≤ 10%)
    @processing_stage(name="tier1_filter")
    def excellent_quality_filter(audio_batch: AudioBatch) -> AudioBatch:
        excellent_data = [
            item for item in audio_batch.data 
            if item.get("wer", 100) <= 10.0
        ]
        
        # Mark as tier 1
        for item in excellent_data:
            item["quality_tier"] = "excellent"
        
        return AudioBatch(data=excellent_data, filepath_key=audio_batch.filepath_key)
    
    # Tier 2: Good quality (10% < WER ≤ 25%)  
    @processing_stage(name="tier2_filter")
    def good_quality_filter(audio_batch: AudioBatch) -> AudioBatch:
        good_data = [
            item for item in audio_batch.data
            if 10.0 < item.get("wer", 100) <= 25.0
        ]
        
        for item in good_data:
            item["quality_tier"] = "good"
        
        return AudioBatch(data=good_data, filepath_key=audio_batch.filepath_key)
    
    # Add both tier filters to the pipeline
    pipeline.add_stage(excellent_quality_filter)
    pipeline.add_stage(good_quality_filter)
    
    return pipeline
```

### Statistical WER Filtering

For statistical analysis-based threshold selection, you can analyze your dataset's WER distribution and then apply the calculated threshold using NeMo Curator's `PreserveByValueStage`:

```python
# Apply calculated statistical threshold
statistical_filter = PreserveByValueStage(
    input_value_key="wer",
    target_value=calculated_threshold,  # From your statistical analysis
    operator="le"
)
```

## Domain-Specific WER Filtering

### Conversational Speech

```python
# More lenient thresholds for conversational speech
conversational_wer_config = {
    "excellent_threshold": 15.0,  # vs. 10.0 for read speech
    "good_threshold": 35.0,       # vs. 25.0 for read speech  
    "acceptable_threshold": 60.0   # vs. 50.0 for read speech
}

conversational_filter = PreserveByValueStage(
    input_value_key="wer",
    target_value=conversational_wer_config["good_threshold"],
    operator="le"
)
```

### Broadcast and News

```python
# Stricter thresholds for high-quality broadcast speech
broadcast_wer_config = {
    "excellent_threshold": 5.0,   # Very strict
    "good_threshold": 15.0,       # Stricter than general
    "acceptable_threshold": 25.0   # Maximum for broadcast quality
}

broadcast_filter = PreserveByValueStage(
    input_value_key="wer", 
    target_value=broadcast_wer_config["good_threshold"],
    operator="le"
)
```
