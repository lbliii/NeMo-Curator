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

### Adaptive WER Thresholds

```python
from dataclasses import dataclass, field

@dataclass
class AdaptiveWerFilterStage(LegacySpeechStage):
    """Apply WER filtering with adaptive thresholds based on dataset characteristics."""
    
    base_threshold: float = 30.0
    language_adjustments: dict = field(default_factory=lambda: {
        "en": 0.0,      # No adjustment for English
        "es": 5.0,      # Slightly more lenient for Spanish  
        "hy": 15.0,     # More lenient for Armenian (low-resource)
        "zh": 10.0      # Moderate adjustment for Chinese
    })
    domain_adjustments: dict = field(default_factory=lambda: {
        "telephony": 10.0,     # More lenient for telephony
        "broadcast": -5.0,     # Stricter for broadcast
        "conversational": 5.0   # Slightly more lenient for conversation
    })
    
    def process_dataset_entry(self, data_entry: dict) -> list[AudioBatch]:
        wer = data_entry.get("wer", 100.0)
        language = data_entry.get("language", "en")
        domain = data_entry.get("domain", "general")
        
        # Calculate adaptive threshold
        threshold = self.base_threshold
        threshold += self.language_adjustments.get(language, 0)
        threshold += self.domain_adjustments.get(domain, 0)
        
        # Apply filter
        if wer <= threshold:
            data_entry["wer_threshold_used"] = threshold
            data_entry["wer_filter_passed"] = True
            return [AudioBatch(data=data_entry)]
        else:
            return []  # Filter out
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

### Multilingual Considerations

```python
def create_language_aware_wer_filter(language_thresholds: dict) -> Pipeline:
    """Create WER filter with language-specific thresholds."""
    from nemo_curator.stages.function_decorators import processing_stage
    
    pipeline = Pipeline(name="language_aware_wer")
    
    @processing_stage(name="language_wer_filter")
    def language_specific_filter(audio_batch: AudioBatch) -> AudioBatch:
        filtered_data = []
        
        for item in audio_batch.data:
            language = item.get("language", "unknown")
            wer = item.get("wer", 100.0)
            
            # Get language-specific threshold
            threshold = language_thresholds.get(language, 50.0)  # Default threshold
            
            if wer <= threshold:
                item["language_wer_threshold"] = threshold
                filtered_data.append(item)
        
        return AudioBatch(data=filtered_data, filepath_key=audio_batch.filepath_key)
    
    pipeline.add_stage(language_specific_filter)
    return pipeline

# Language-specific thresholds
language_thresholds = {
    "en": 20.0,    # Strict for high-resource English
    "es": 25.0,    # Moderate for Spanish
    "fr": 25.0,    # Moderate for French
    "de": 30.0,    # Slightly lenient for German
    "hy": 45.0,    # Very lenient for low-resource Armenian
    "zh": 35.0     # Moderate-lenient for Chinese
}

language_filter = create_language_aware_wer_filter(language_thresholds)
```


## Filtering Strategies

### Progressive Filtering

```python
def create_progressive_wer_pipeline() -> Pipeline:
    """Create pipeline with progressive WER filtering stages."""
    from nemo_curator.stages.function_decorators import processing_stage
    
    pipeline = Pipeline(name="progressive_wer")
    
    # Calculate WER
    pipeline.add_stage(GetPairwiseWerStage())
    
    # Stage 1: Remove very poor quality (WER > 75%)
    pipeline.add_stage(
        PreserveByValueStage(
            input_value_key="wer",
            target_value=75.0,
            operator="lt"  # strictly less than
        )
    )
    
    # Stage 2: Mark quality tiers
    @processing_stage(name="quality_tier_marking")
    def mark_quality_tiers(audio_batch: AudioBatch) -> AudioBatch:
        for item in audio_batch.data:
            wer = item["wer"]
            
            if wer <= 10:
                item["quality_tier"] = "tier1_excellent"
            elif wer <= 25:
                item["quality_tier"] = "tier2_good"
            elif wer <= 50:
                item["quality_tier"] = "tier3_moderate"
            else:
                item["quality_tier"] = "tier4_poor"
        
        return audio_batch
    
    pipeline.add_stage(mark_quality_tiers)
    
    # Stage 3: Apply final threshold based on data availability
    @processing_stage(name="adaptive_final_filter")
    def adaptive_final_filter(audio_batch: AudioBatch) -> AudioBatch:
        # Count samples in each tier
        tier_counts = {}
        for item in audio_batch.data:
            tier = item["quality_tier"]
            tier_counts[tier] = tier_counts.get(tier, 0) + 1
        
        # Adaptive threshold based on data availability
        total_samples = len(audio_batch.data)
        tier1_ratio = tier_counts.get("tier1_excellent", 0) / total_samples
        tier2_ratio = tier_counts.get("tier2_good", 0) / total_samples
        
        if tier1_ratio >= 0.3:  # 30%+ excellent quality
            threshold = 10.0    # Use only excellent
        elif tier1_ratio + tier2_ratio >= 0.6:  # 60%+ good quality  
            threshold = 25.0    # Use excellent + good
        else:
            threshold = 50.0    # Include moderate quality
        
        # Apply adaptive threshold
        filtered_data = [
            item for item in audio_batch.data
            if item["wer"] <= threshold
        ]
        
        for item in filtered_data:
            item["adaptive_threshold_used"] = threshold
        
        return AudioBatch(data=filtered_data, filepath_key=audio_batch.filepath_key)
    
    pipeline.add_stage(adaptive_final_filter)
    
    return pipeline
```

### Context-Aware Filtering

```python
from dataclasses import dataclass

@dataclass
class ContextAwareWerFilterStage(LegacySpeechStage):
    """Filter based on WER with context awareness."""
    
    base_threshold: float = 30.0
    
    def process_dataset_entry(self, data_entry: dict) -> list[AudioBatch]:
        wer = data_entry.get("wer", 100.0)
        text = data_entry.get("text", "")
        pred_text = data_entry.get("pred_text", "")
        duration = data_entry.get("duration", 0)
        
        # Context-aware threshold adjustment
        threshold = self.base_threshold
        
        # Adjust for text complexity
        word_count = len(text.split())
        if word_count < 3:
            threshold -= 10.0  # Stricter for short utterances
        elif word_count > 20:
            threshold += 5.0   # More lenient for long utterances
        
        # Adjust for duration
        if duration < 1.0:
            threshold -= 5.0   # Stricter for very short audio
        elif duration > 15.0:
            threshold += 5.0   # More lenient for long audio
        
        # Adjust for prediction length consistency
        pred_word_count = len(pred_text.split())
        length_ratio = pred_word_count / word_count if word_count > 0 else 0
        
        if length_ratio < 0.5 or length_ratio > 2.0:
            threshold -= 10.0  # Stricter for length mismatches
        
        # Apply adjusted threshold
        if wer <= threshold:
            data_entry["context_threshold_used"] = threshold
            data_entry["context_adjustments"] = {
                "word_count_adj": word_count,
                "duration_adj": duration,
                "length_ratio_adj": length_ratio
            }
            return [AudioBatch(data=data_entry)]
        else:
            return []
```
