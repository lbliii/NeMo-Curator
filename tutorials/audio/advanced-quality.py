# Copyright (c) 2025, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Advanced Audio Quality Assessment Tutorial

This tutorial demonstrates multi-criteria quality filtering for audio datasets,
showing how to combine multiple quality metrics to create sophisticated
data curation pipelines.

Features demonstrated:
- Multi-threshold WER filtering
- Duration-based filtering (min/max bounds)
- Character rate analysis
- Word rate analysis
- Combined quality criteria
- Quality distribution analysis
"""

import argparse
import os
import shutil

from loguru import logger

from nemo_curator.backends.xenna import XennaExecutor
from nemo_curator.pipeline import Pipeline
from nemo_curator.stages.audio.common import GetAudioDurationStage, PreserveByValueStage
from nemo_curator.stages.audio.datasets.fleurs.create_initial_manifest import CreateInitialManifestFleursStage
from nemo_curator.stages.audio.inference.asr_nemo import InferenceAsrNemoStage
from nemo_curator.stages.audio.io.convert import AudioToDocumentStage
from nemo_curator.stages.audio.metrics.get_wer import GetPairwiseWerStage
from nemo_curator.stages.resources import Resources
from nemo_curator.stages.text.io.writer import JsonlWriter


def create_advanced_quality_pipeline(
    data_dir: str,
    output_dir: str,
    model_name: str = "nvidia/parakeet-tdt-0.6b-v2",
    min_duration: float = 1.0,
    max_duration: float = 30.0,
    max_wer: float = 20.0,
    min_char_rate: float = 8.0,
    max_char_rate: float = 25.0,
    min_word_rate: float = 1.5,
    max_word_rate: float = 6.0,
) -> Pipeline:
    """
    Create an advanced audio quality assessment pipeline with multi-criteria filtering.
    
    This pipeline demonstrates sophisticated quality control by applying multiple
    filters in sequence to ensure high-quality audio data.
    
    Args:
        data_dir: Directory containing FLEURS dataset
        output_dir: Directory to save processed results
        model_name: NeMo ASR model for transcription
        min_duration: Minimum audio duration in seconds
        max_duration: Maximum audio duration in seconds  
        max_wer: Maximum word error rate (percentage)
        min_char_rate: Minimum character rate (chars/second)
        max_char_rate: Maximum character rate (chars/second)
        min_word_rate: Minimum word rate (words/second)
        max_word_rate: Maximum word rate (words/second)
    """
    pipeline = Pipeline()
    
    # Stage 1: Create initial manifest from FLEURS dataset
    logger.info("Setting up FLEURS dataset processing...")
    pipeline.add_stage(
        CreateInitialManifestFleursStage(
            output_manifest_file=os.path.join(output_dir, "initial_manifest.jsonl"),
            fleurs_data_dir=data_dir,
            language_code="en_us",  # Focus on English for this tutorial
        )
    )
    
    # Stage 2: Calculate audio durations
    logger.info("Adding duration calculation...")
    pipeline.add_stage(
        GetAudioDurationStage().with_(
            resources=Resources(gpus=0),  # CPU-only for duration calculation
            name="duration_calculation"
        )
    )
    
    # Stage 3: Apply duration-based filtering (first quality gate)
    logger.info(f"Adding duration filtering: {min_duration}s - {max_duration}s")
    pipeline.add_stage(
        PreserveByValueStage(
            field_name="duration", 
            operator=">=", 
            threshold=min_duration
        ).with_(name="filter_min_duration")
    )
    
    pipeline.add_stage(
        PreserveByValueStage(
            field_name="duration", 
            operator="<=", 
            threshold=max_duration
        ).with_(name="filter_max_duration")
    )
    
    # Stage 4: ASR inference for transcription
    logger.info(f"Adding ASR inference with model: {model_name}")
    pipeline.add_stage(
        InferenceAsrNemoStage(
            model_name=model_name,
            filepath_key="audio_filepath",
            pred_text_key="pred_text"
        ).with_(
            resources=Resources(gpus=1),
            batch_size=32,
            name="asr_inference"
        )
    )
    
    # Stage 5: Calculate WER and speech rate metrics
    logger.info("Adding quality metrics calculation...")
    pipeline.add_stage(
        GetPairwiseWerStage(
            pred_text_key="pred_text",
            ref_text_key="text"
        ).with_(
            resources=Resources(gpus=0),  # CPU-only for WER calculation
            name="quality_metrics"
        )
    )
    
    # Stage 6: Apply WER-based filtering (second quality gate)
    logger.info(f"Adding WER filtering: max {max_wer}%")
    pipeline.add_stage(
        PreserveByValueStage(
            field_name="wer", 
            operator="<=", 
            threshold=max_wer
        ).with_(name="filter_wer")
    )
    
    # Stage 7: Apply character rate filtering (third quality gate)
    logger.info(f"Adding character rate filtering: {min_char_rate} - {max_char_rate} chars/sec")
    pipeline.add_stage(
        PreserveByValueStage(
            field_name="char_rate", 
            operator=">=", 
            threshold=min_char_rate
        ).with_(name="filter_min_char_rate")
    )
    
    pipeline.add_stage(
        PreserveByValueStage(
            field_name="char_rate", 
            operator="<=", 
            threshold=max_char_rate
        ).with_(name="filter_max_char_rate")
    )
    
    # Stage 8: Apply word rate filtering (fourth quality gate)
    logger.info(f"Adding word rate filtering: {min_word_rate} - {max_word_rate} words/sec")
    pipeline.add_stage(
        PreserveByValueStage(
            field_name="word_rate", 
            operator=">=", 
            threshold=min_word_rate
        ).with_(name="filter_min_word_rate")
    )
    
    pipeline.add_stage(
        PreserveByValueStage(
            field_name="word_rate", 
            operator="<=", 
            threshold=max_word_rate
        ).with_(name="filter_max_word_rate")
    )
    
    # Stage 9: Convert to document format for final output
    pipeline.add_stage(
        AudioToDocumentStage().with_(name="convert_to_documents")
    )
    
    # Stage 10: Save high-quality filtered results
    pipeline.add_stage(
        JsonlWriter(path=os.path.join(output_dir, "high_quality_audio.jsonl"))
        .with_(name="save_results")
    )
    
    logger.info("Advanced quality assessment pipeline created successfully!")
    logger.info("Quality gates applied:")
    logger.info(f"  1. Duration: {min_duration}s - {max_duration}s")
    logger.info(f"  2. WER: ≤ {max_wer}%")
    logger.info(f"  3. Character rate: {min_char_rate} - {max_char_rate} chars/sec")
    logger.info(f"  4. Word rate: {min_word_rate} - {max_word_rate} words/sec")
    
    return pipeline


def main():
    parser = argparse.ArgumentParser(
        description="Advanced Audio Quality Assessment Tutorial",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Required arguments
    parser.add_argument(
        "--data-dir", 
        required=True, 
        help="Directory containing FLEURS dataset"
    )
    parser.add_argument(
        "--output-dir", 
        required=True, 
        help="Directory to save processed results"
    )
    
    # Model configuration
    parser.add_argument(
        "--model-name",
        default="nvidia/parakeet-tdt-0.6b-v2",
        help="NeMo ASR model name for transcription"
    )
    
    # Duration filtering parameters
    parser.add_argument(
        "--min-duration",
        type=float,
        default=1.0,
        help="Minimum audio duration in seconds"
    )
    parser.add_argument(
        "--max-duration", 
        type=float,
        default=30.0,
        help="Maximum audio duration in seconds"
    )
    
    # Quality filtering parameters
    parser.add_argument(
        "--max-wer",
        type=float,
        default=20.0,
        help="Maximum word error rate (percentage)"
    )
    parser.add_argument(
        "--min-char-rate",
        type=float, 
        default=8.0,
        help="Minimum character rate (chars/second)"
    )
    parser.add_argument(
        "--max-char-rate",
        type=float,
        default=25.0,
        help="Maximum character rate (chars/second)"
    )
    parser.add_argument(
        "--min-word-rate",
        type=float,
        default=1.5,
        help="Minimum word rate (words/second)"
    )
    parser.add_argument(
        "--max-word-rate",
        type=float,
        default=6.0,
        help="Maximum word rate (words/second)"
    )
    
    # Execution parameters
    parser.add_argument(
        "--device",
        default="auto",
        help="Device to use for processing (auto, cpu, cuda)"
    )
    parser.add_argument(
        "--num-workers",
        type=int,
        default=4,
        help="Number of worker processes"
    )
    
    args = parser.parse_args()
    
    # Setup output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    logger.info("Starting Advanced Audio Quality Assessment Tutorial")
    logger.info(f"Data directory: {args.data_dir}")
    logger.info(f"Output directory: {args.output_dir}")
    logger.info(f"ASR model: {args.model_name}")
    
    # Create the advanced quality pipeline
    pipeline = create_advanced_quality_pipeline(
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        model_name=args.model_name,
        min_duration=args.min_duration,
        max_duration=args.max_duration,
        max_wer=args.max_wer,
        min_char_rate=args.min_char_rate,
        max_char_rate=args.max_char_rate,
        min_word_rate=args.min_word_rate,
        max_word_rate=args.max_word_rate,
    )
    
    # Execute the pipeline
    executor = XennaExecutor(device=args.device, num_workers=args.num_workers)
    
    logger.info("Executing advanced quality assessment pipeline...")
    try:
        pipeline.run(executor=executor)
        logger.info("✅ Pipeline completed successfully!")
        logger.info(f"High-quality audio data saved to: {args.output_dir}/high_quality_audio.jsonl")
        
        # Log summary statistics if output file exists
        output_file = os.path.join(args.output_dir, "high_quality_audio.jsonl")
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                line_count = sum(1 for _ in f)
            logger.info(f"Final dataset contains {line_count} high-quality audio samples")
        
    except Exception as e:
        logger.error(f"❌ Pipeline failed with error: {e}")
        raise
    
    logger.info("Advanced Audio Quality Assessment Tutorial completed!")


if __name__ == "__main__":
    main()
