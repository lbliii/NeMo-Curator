---
description: "Filter audio samples by duration ranges, speech rate metrics, and temporal characteristics for optimal dataset quality"
categories: ["audio-processing"]
tags: ["duration-filtering", "speech-rate", "temporal-filtering", "audio-length", "quality-control"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "beginner"
content_type: "how-to"
modality: "audio-only"
---

# Duration Filtering

Filter audio samples by duration ranges, speech rate metrics, and temporal characteristics to create optimal datasets for ASR training and speech processing applications.

## Duration-Based Quality Control

### Why Duration Matters

**Training Efficiency**: Duration filtering can improve ASR training by removing samples that may be problematic for training

**Processing Performance**: Duration affects computational requirements:
- Memory usage scales with audio length
- Batch processing efficiency varies with duration variance
- GPU utilization optimized for consistent lengths

## Basic Duration Filtering

### Simple Duration Range

```python
from nemo_curator.stages.audio.common import GetAudioDurationStage, PreserveByValueStage

# Calculate duration for each audio file
duration_stage = GetAudioDurationStage(
    audio_filepath_key="audio_filepath",
    duration_key="duration"
)

# Filter for optimal duration range (1-15 seconds)
min_duration_filter = PreserveByValueStage(
    input_value_key="duration",
    target_value=1.0,
    operator="ge"  # greater than or equal
)

max_duration_filter = PreserveByValueStage(
    input_value_key="duration", 
    target_value=15.0,
    operator="le"  # less than or equal
)

# Add to pipeline
pipeline.add_stage(duration_stage)
pipeline.add_stage(min_duration_filter) 
pipeline.add_stage(max_duration_filter)
```

### Use Case-Specific Ranges

```python
# Duration ranges for different applications
duration_configs = {
    "asr_training": {
        "min_duration": 1.0,
        "max_duration": 20.0,
        "optimal_range": (2.0, 10.0)
    },
    
    "voice_cloning": {
        "min_duration": 3.0,
        "max_duration": 10.0, 
        "optimal_range": (4.0, 8.0)
    },
    
    "speech_synthesis": {
        "min_duration": 2.0,
        "max_duration": 15.0,
        "optimal_range": (3.0, 12.0)
    },
    
    "keyword_spotting": {
        "min_duration": 0.5,
        "max_duration": 3.0,
        "optimal_range": (1.0, 2.0)
    }
}

def create_use_case_duration_filter(use_case: str) -> list[PreserveByValueStage]:
    """Create duration filters for specific use case."""
    
    config = duration_configs.get(use_case, duration_configs["asr_training"])
    
    return [
        PreserveByValueStage(
            input_value_key="duration",
            target_value=config["min_duration"],
            operator="ge"
        ),
        PreserveByValueStage(
            input_value_key="duration",
            target_value=config["max_duration"],
            operator="le"
        )
    ]
```

## Speech Rate Analysis

### Calculate Speech Rate Metrics

The built-in speech rate calculation functions can be used within custom processing stages to analyze speaking speed and add metrics to your pipeline data.

### Speech Rate Filtering

If you have pre-calculated speech rate metrics in your data, you can filter based on them:

```python
from nemo_curator.stages.audio.common import PreserveByValueStage
from nemo_curator.pipeline import Pipeline

# Example: Filter by speech rate if you have word_rate field in your data
pipeline = Pipeline(name="speech_rate_filtering")

# Filter by speech rate (1.5-5 words per second)
pipeline.add_stage(
    PreserveByValueStage(
        input_value_key="word_rate",  # Assumes this field exists in your data
        target_value=1.5,
        operator="ge"
    )
)

pipeline.add_stage(
    PreserveByValueStage(
        input_value_key="word_rate",
        target_value=5.0,
        operator="le"
    )
)
```

:::{note}
This example assumes you have already calculated and stored speech rate metrics in your audio data. The built-in stages do not automatically calculate speech rates - you would need to create a custom stage for that functionality.
:::


## Speech Rate Filtering

### Normal Speech Rate Range

```python
from nemo_curator.stages.audio.common import PreserveByValueStage

# Filter by word rate (assumes word_rate field exists in your data)
word_rate_min_filter = PreserveByValueStage(
    input_value_key="word_rate",
    target_value=1.5,
    operator="ge"
)

word_rate_max_filter = PreserveByValueStage(
    input_value_key="word_rate",
    target_value=5.0,
    operator="le"
)

# Filter by character rate (assumes char_rate field exists in your data)
char_rate_min_filter = PreserveByValueStage(
    input_value_key="char_rate",
    target_value=8.0,
    operator="ge"
)

char_rate_max_filter = PreserveByValueStage(
    input_value_key="char_rate",
    target_value=30.0,
    operator="le"
)
```

:::{note}
These examples assume you have pre-calculated speech rate metrics in your audio data. Use the `get_wordrate()` and `get_charrate()` utility functions to calculate these values in a custom processing stage.
:::


## Combined Duration and Quality Filtering

### Integrated Quality-Duration Pipeline

```python
def create_integrated_quality_duration_pipeline() -> Pipeline:
    """Combine duration, speech rate, and WER filtering."""
    
    pipeline = Pipeline(name="integrated_quality_duration")
    
    # Step 1: Calculate all metrics
    pipeline.add_stage(GetAudioDurationStage(
        audio_filepath_key="audio_filepath",
        duration_key="duration"
    ))
    # Example: compute speech-rate metrics using utilities in a custom stage
    from nemo_curator.stages.function_decorators import processing_stage
    from nemo_curator.stages.audio.metrics.get_wer import get_wordrate, get_charrate

    @processing_stage(name="speech_rate_analysis")
    def compute_speech_rate(audio_batch: AudioBatch) -> AudioBatch:
        for item in audio_batch.data:
            duration = float(item.get("duration", 0) or 0)
            text = item.get("text", "") or ""
            if duration > 0 and text:
                item["word_rate"] = get_wordrate(text, duration)
                item["char_rate"] = get_charrate(text, duration)
        return audio_batch

    pipeline.add_stage(compute_speech_rate)
    pipeline.add_stage(GetPairwiseWerStage())
    
    # Step 2: Apply comprehensive filtering
    @processing_stage(name="comprehensive_quality_filter")
    def comprehensive_filter(audio_batch: AudioBatch) -> AudioBatch:
        filtered_data = []
        
        for item in audio_batch.data:
            duration = item.get("duration", 0)
            wer = item.get("wer", 100)
            word_rate = item.get("word_rate", 0)
            
            # Multi-criteria filtering
            duration_ok = 1.0 <= duration <= 20.0
            wer_ok = wer <= 35.0
            speech_rate_ok = 1.5 <= word_rate <= 5.0
            
            # Adaptive criteria based on other metrics
            if wer <= 15.0:  # Excellent WER - relax duration requirements
                duration_ok = 0.5 <= duration <= 30.0
            
            if duration >= 10.0:  # Long audio - relax WER requirements slightly
                wer_ok = wer <= 40.0
            
            # Apply combined filter
            if duration_ok and wer_ok and speech_rate_ok:
                item["comprehensive_filter_passed"] = True
                item["filter_criteria"] = {
                    "duration_range": [1.0, 20.0],
                    "wer_threshold": 35.0,
                    "speech_rate_range": [1.5, 5.0]
                }
                filtered_data.append(item)
        
        return AudioBatch(data=filtered_data, filepath_key=audio_batch.filepath_key)
    
    pipeline.add_stage(comprehensive_filter)
    
    return pipeline
```


## Best Practices

### Duration Filtering Strategy

1. **Analyze First**: Understand your dataset's duration distribution
2. **Use Case Alignment**: Align duration ranges with intended use
3. **Progressive Filtering**: Apply duration filters before computationally expensive stages
4. **Quality Correlation**: Consider correlation between duration and other quality metrics

### Common Pitfalls

**Over-Filtering**: Removing too much data

```python
# Check retention rates before applying filters
retention_rate = filtered_count / original_count
if retention_rate < 0.5:  # Less than 50% retained
    print("Warning: Very aggressive filtering - consider relaxing thresholds")
```

**Under-Filtering**: Keeping problematic samples that may negatively impact training or processing efficiency.


## Real Working Example

Here's a complete working example from the NeMo Curator tutorials showing actual duration filtering in practice:

```python
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.audio.common import GetAudioDurationStage, PreserveByValueStage
from nemo_curator.stages.audio.datasets.fleurs.create_initial_manifest import CreateInitialManifestFleursStage
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.stages.audio.metrics.get_wer import GetPairwiseWerStage
from nemo_curator.stages.audio.io.convert import AudioToDocumentStage
from nemo_curator.stages.resources import Resources

def create_audio_pipeline(raw_data_dir: str, wer_threshold: float = 75.0) -> Pipeline:
    """Real working pipeline from NeMo Curator tutorials."""
    
    pipeline = Pipeline(name="audio_inference", description="Inference audio and filter by WER threshold.")
    
    # Load FLEURS dataset
    pipeline.add_stage(
        CreateInitialManifestFleursStage(
            lang="hy_am",
            split="dev", 
            raw_data_dir=raw_data_dir,
        ).with_(batch_size=4)
    )
    
    # ASR inference
    pipeline.add_stage(
        InferenceAsrNemoStage(
            model_name="nvidia/stt_hy_fastconformer_hybrid_large_pc"
        ).with_(resources=Resources(gpus=1.0))
    )
    
    # Calculate WER
    pipeline.add_stage(
        GetPairwiseWerStage(
            text_key="text", 
            pred_text_key="pred_text", 
            wer_key="wer"
        )
    )
    
    # Calculate duration
    pipeline.add_stage(
        GetAudioDurationStage(
            audio_filepath_key="audio_filepath", 
            duration_key="duration"
        )
    )
    
    # Filter by WER threshold
    pipeline.add_stage(
        PreserveByValueStage(
            input_value_key="wer", 
            target_value=wer_threshold, 
            operator="le"
        )
    )
    
    # Convert to document format
    pipeline.add_stage(AudioToDocumentStage().with_(batch_size=1))
    
    return pipeline
```

:::{note}
This example comes directly from `tutorials/audio/fleurs/pipeline.py` and shows the correct parameter names and usage patterns for the built-in stages.
:::

## Related Topics

- **[Quality Assessment Overview](index.md)**: Complete quality filtering workflow
- **[WER Filtering](wer-filtering.md)**: Transcription accuracy filtering
- **[Audio Analysis](../audio-analysis/index.md)**: Duration calculation and analysis
