---
description: "Validate audio file formats and detect corrupted files for robust audio curation pipelines"
categories: ["processors"]
tags: ["audio-validation", "format-support", "error-handling", "quality-control", "file-validation"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "how-to"
modality: "audio-only"
---

(audio-analysis-format-validation)=
# Format Validation

Validate audio file formats and detect corrupted files to ensure robust audio curation pipelines with reliable data quality.

## Overview

The format validation processor verifies audio file integrity, format compatibility, and accessibility before processing. This prevents pipeline failures and ensures consistent data quality across large audio datasets.

## Key Features

- **Format Detection**: Automatic audio format detection and validation
- **Corruption Detection**: Identifies corrupted or unreadable audio files
- **Compatibility Checking**: Ensures files are compatible with processing pipeline
- **Error Reporting**: Detailed error logs for debugging and quality control

## Supported Formats

NeMo Curator supports all formats compatible with the soundfile library:

- **WAV** - Uncompressed audio (recommended for high quality)
- **FLAC** - Lossless compression with metadata support
- **OGG** - Open-source compressed format
- **MP3** - Compressed format (requires additional dependencies)
- **M4A** - Apple compressed format
- **AIFF** - Apple uncompressed format

## How It Works

The format validation processor performs comprehensive checks on audio files:

```python
from nemo_curator.stages.audio import AudioFormatValidator

# Initialize format validator
format_validator = AudioFormatValidator()

# Validate AudioBatch files
validated_batch = format_validator(audio_batch)
```

### Validation Process

1. **File Existence**: Checks if audio files exist at specified paths
2. **Format Detection**: Identifies audio format using file headers
3. **Readability Test**: Attempts to read audio file metadata
4. **Compatibility Check**: Verifies format compatibility with pipeline
5. **Corruption Detection**: Tests file integrity and structure

## Configuration Options

### Basic Configuration

```python
from nemo_curator.stages.audio import AudioFormatValidator

# Default configuration
format_validator = AudioFormatValidator(
    audio_field="audio_filepath",     # Field containing audio file paths
    validation_field="is_valid",      # Output field for validation results
    supported_formats=["wav", "flac", "ogg"]  # Allowed formats
)
```

### Advanced Configuration

```python
# Comprehensive validation with detailed reporting
format_validator = AudioFormatValidator(
    audio_field="audio_filepath",
    validation_field="validation_status",
    supported_formats=["wav", "flac", "ogg", "mp3"],
    check_corruption=True,           # Deep corruption checking
    check_metadata=True,             # Validate metadata fields
    max_file_size_mb=500,           # Maximum file size limit
    min_file_size_kb=1,             # Minimum file size limit
    report_details=True,            # Include detailed error messages
    remove_invalid=False            # Keep invalid files with status
)
```

## Usage Examples

### Basic Format Validation

```python
from nemo_curator.datasets import AudioDataset
from nemo_curator.stages.audio import AudioFormatValidator

# Load audio dataset
audio_dataset = AudioDataset.from_manifest("audio_manifest.jsonl")
audio_batch = audio_dataset.to_batch()

# Validate formats
format_validator = AudioFormatValidator()
validated_batch = format_validator(audio_batch)

# Check validation results
valid_count = sum(1 for sample in validated_batch.data if sample.get("is_valid", False))
total_count = len(validated_batch.data)
print(f"Valid files: {valid_count}/{total_count}")
```

### Filtering Invalid Files

```python
from nemo_curator.stages.audio import AudioFormatValidator, AudioValidationFilter

# Validate and filter in pipeline
format_validator = AudioFormatValidator(remove_invalid=False)
validation_filter = AudioValidationFilter(validation_field="is_valid")

# Process pipeline
validated_batch = format_validator(audio_batch)
clean_batch = validation_filter(validated_batch)

print(f"Removed {len(audio_batch.data) - len(clean_batch.data)} invalid files")
```

### Detailed Error Reporting

```python
# Enable detailed validation reporting
format_validator = AudioFormatValidator(
    report_details=True,
    validation_field="validation_status"
)

validated_batch = format_validator(audio_batch)

# Analyze validation results
for sample in validated_batch.data:
    status = sample.get("validation_status", {})
    if not status.get("is_valid", False):
        print(f"Invalid file: {sample['audio_filepath']}")
        print(f"Error: {status.get('error_message', 'Unknown error')}")
        print(f"Format: {status.get('detected_format', 'Unknown')}")
```

### Custom Format Support

```python
# Add custom format support
format_validator = AudioFormatValidator(
    supported_formats=["wav", "flac", "ogg", "m4a", "aiff"],
    format_converters={
        "m4a": "ffmpeg",    # Use ffmpeg for M4A conversion
        "aiff": "soundfile" # Use soundfile for AIFF
    }
)
```

## Validation Results

The processor adds validation information to each audio sample:

```json
{
  "audio_filepath": "/path/to/audio.wav",
  "text": "Sample transcription",
  "is_valid": true,
  "validation_status": {
    "is_valid": true,
    "detected_format": "wav",
    "file_size_mb": 2.45,
    "sample_rate": 16000,
    "channels": 1,
    "duration": 12.3,
    "error_message": null
  }
}
```

## Integration with Pipeline

Format validation is typically the first step in audio processing pipelines:

```python
from nemo_curator.stages.audio import (
    AudioFormatValidator,
    AudioValidationFilter,
    AudioDurationCalculator,
    ASRInference
)

# Complete preprocessing pipeline
preprocessing_pipeline = [
    AudioFormatValidator(),           # Validate file formats
    AudioValidationFilter(),          # Remove invalid files
    AudioDurationCalculator(),        # Calculate durations
    ASRInference()                    # Perform transcription
]

# Process audio batch
processed_batch = audio_batch
for stage in preprocessing_pipeline:
    processed_batch = stage(processed_batch)
```

## Performance Optimization

### Parallel Validation

```python
# Use parallel processing for large datasets
format_validator = AudioFormatValidator(
    parallel_workers=8,        # Use 8 parallel workers
    chunk_size=100,           # Process 100 files per chunk
    use_threading=True        # Use threading for I/O operations
)
```

### Caching Results

```python
# Cache validation results to avoid reprocessing
format_validator = AudioFormatValidator(
    cache_validation=True,     # Cache results by file path
    cache_size=10000,         # Cache up to 10k validation results
    cache_ttl_hours=24        # Cache timeout of 24 hours
)
```

## Troubleshooting

### Common Issues

**Unsupported Format Errors**
```python
# Check format support before validation
import soundfile as sf
print("Available formats:", sf.available_formats())

# Add format conversion if needed
format_validator = AudioFormatValidator(
    auto_convert=True,         # Automatically convert unsupported formats
    conversion_format="wav",   # Target format for conversion
    keep_original=False        # Remove original after conversion
)
```

**File Permission Issues**
```python
# Handle permission errors gracefully
format_validator = AudioFormatValidator(
    handle_permissions=True,   # Skip files with permission issues
    log_permission_errors=True # Log permission errors for review
)
```

**Large File Handling**
```python
# Optimize for large audio files
format_validator = AudioFormatValidator(
    max_file_size_mb=1000,    # Allow files up to 1GB
    stream_validation=True,   # Stream large files for validation
    quick_check=True          # Use header-only validation for speed
)
```

## Error Handling

### Validation Modes

```python
# Different error handling strategies
strict_validator = AudioFormatValidator(
    validation_mode="strict",  # Fail on any invalid file
    stop_on_error=True        # Stop processing on first error
)

lenient_validator = AudioFormatValidator(
    validation_mode="lenient", # Continue with warnings
    log_errors=True,          # Log all errors for review
    fallback_validation=True  # Use fallback validation methods
)
```

### Custom Error Handling

```python
def custom_error_handler(filepath, error):
    """Custom error handling function"""
    print(f"Validation error for {filepath}: {error}")
    return {"is_valid": False, "error_type": type(error).__name__}

format_validator = AudioFormatValidator(
    error_handler=custom_error_handler,
    continue_on_error=True
)
```

## Best Practices

1. **Validate Early**: Run format validation before other processing stages
2. **Log Results**: Keep detailed logs of validation results for debugging
3. **Handle Errors**: Implement robust error handling for production pipelines
4. **Monitor Performance**: Track validation speed and resource usage
5. **Cache Results**: Use caching for repeated validation of the same files

## Related Topics

- **[Duration Calculation](duration-calculation.md)** - Calculate audio duration after validation
- **[Audio Analysis Overview](index.md)** - Complete audio analysis capabilities
- **[Quality Assessment](../quality-assessment/index.md)** - Quality filtering workflows
- **[Local File Loading](../../load-data/local-files.md)** - Loading audio files for validation
