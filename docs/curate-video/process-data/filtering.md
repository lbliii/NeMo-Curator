---
description: "Filter clips by motion or aesthetics to improve dataset quality"
categories: ["video-curation"]
tags: ["filtering", "motion", "aesthetic", "video"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "howto"
modality: "video-only"
---

(video-process-filtering)=

# Filtering

Apply motion-based filtering and aesthetic filtering to prune low-quality clips during curation.

## How it Works

Filtering runs in two passes that balance speed and quality:

1. **Motion pass** (fast): The pipeline decodes lightweight motion vectors and computes motion scores to drop static or near‑static clips early. This step adds `decoded_motion_data` per clip, then writes `motion_score_global_mean` and `motion_score_per_patch_min_256`. Clips below thresholds move to `video.filtered_clips`, and `video.clip_stats.num_filtered_by_motion` increments.
2. **Aesthetic pass** (model based): Upstream, the pipeline extracts frames using the `sequence` policy at a chosen `target_fps`. The aesthetic stage reads `extracted_frames[sequence-<target_fps>]`, produces an `aesthetic_score`, and removes clips below the threshold. These clips move to `video.filtered_clips`, and `video.clip_stats.num_filtered_by_aesthetic` increments.

### Pipeline Stages

At a glance, the stage order is:

1. Decode motion vectors
2. Filter by motion
3. Extract frames (sequence, `target_fps`)
4. Filter by aesthetics

### Data

Data lives in:

- Source clips: `video.clips`
- Removed clips: `video.filtered_clips`
- Temporary motion decode: `decoded_motion_data`
- Frame store: `extracted_frames[sequence-<target_fps>]`
- Stats: `video.clip_stats`

---

## Motion Filtering

Motion filtering is a two‑step process: first decode motion vectors, then filter clips based on motion scores.

### Decode Motion Vectors

Add `MotionVectorDecodeStage` to sample motion vectors from each clip.

```python
from nemo_curator.stages.video.filtering.motion_filter import MotionVectorDecodeStage

decode = MotionVectorDecodeStage(
    target_fps=2.0,
    target_duration_ratio=0.5,
    num_cpus_per_worker=4.0,
)
```

#### Decode Parameters

```{list-table} Motion vector decoding parameters
:header-rows: 1
:widths: 22 12 12 54

* - Parameter
  - Type
  - Default
  - Description
* - `num_cpus_per_worker`
  - float
  - 6.0
  - CPU cores reserved per worker for decoding motion vectors.
* - `target_fps`
  - float
  - 2.0
  - Target frames per second for sampling motion vectors.
* - `target_duration_ratio`
  - float
  - 0.5
  - Fraction of each clip's duration to decode for motion analysis.
* - `verbose`
  - bool
  - `False`
  - Log warnings and per‑clip issues during decoding.
```

#### Decode Outputs

- Adds `decoded_motion_data` to each clip, or records an error in `clip.errors`.

### Filter by Motion

Then add `MotionFilterStage` to compute motion scores and filter out low‑motion clips.

```python
from nemo_curator.stages.video.filtering.motion_filter import MotionFilterStage

motion = MotionFilterStage(
    score_only=False,
    global_mean_threshold=0.00098,
    per_patch_min_256_threshold=0.000001,
    motion_filter_batch_size=64,
    num_gpus_per_worker=0.5,
    verbose=True,
)
```

The default `motion_filter_batch_size` is 256. The example uses 64 to lower memory requirements on resource‑constrained nodes.

#### Filter Parameters

```{list-table} Motion filtering parameters
:header-rows: 1
:widths: 22 12 12 54

* - Parameter
  - Type
  - Default
  - Description
* - `score_only`
  - bool
  - `False`
  - Compute motion scores without filtering out clips.
* - `global_mean_threshold`
  - float
  - 0.00098
  - Threshold on the global mean motion score; lower implies less motion.
* - `per_patch_min_256_threshold`
  - float
  - 0.000001
  - Threshold on the minimum per‑patch score over 256 patches.
* - `motion_filter_batch_size`
  - int
  - 256
  - Batch size for GPU computation; decrease to reduce memory usage.
* - `num_gpus_per_worker`
  - float
  - 0.0
  - GPUs reserved per worker for motion scoring (0 uses CPU path).
* - `verbose`
  - bool
  - `False`
  - Log per‑clip decisions and scores.
```

#### Filter outputs

- Adds `motion_score_global_mean` and `motion_score_per_patch_min_256` to each clip.
- Moves filtered clips to `video.filtered_clips` and increments `video.clip_stats.num_filtered_by_motion`.

## Aesthetic Filtering

Aesthetic filtering works best when you prepare frames first, then score clips using a CLIP‑based aesthetic model.

### Prepare Frames

Extract frames earlier in the pipeline. Use a frame extraction stage with a `sequence` policy and set a `target_fps` that matches the aesthetic stage. Refer to [Frame Extraction](video-process-frame-extraction) for guidance.

```python
# Example: upstream frame extraction snippet (pseudocode)
from nemo_curator.stages.video.frame_extraction import FrameExtractionStage
frames = FrameExtractionStage(policy="sequence", target_fps=1.0)
```

#### Frame Requirements

- Use `sequence` frame extraction policy.
- Match `target_fps` here and in the aesthetic stage.
- Ensure `clip.extracted_frames` contains frames for the signature `sequence-<target_fps>`.

### Filter by Aesthetics

Add `ClipAestheticFilterStage` to score each clip and drop clips below a threshold.

```python
from nemo_curator.stages.video.filtering.clip_aesthetic_filter import ClipAestheticFilterStage

aesthetic = ClipAestheticFilterStage(
    model_dir="/models",
    score_threshold=3.5,
    reduction="min",  # or "mean"
    target_fps=1.0,
    num_gpus_per_worker=0.25,
    verbose=True,
)
```

#### Aesthetic Parameters

```{list-table} CLIP aesthetic filtering parameters
:header-rows: 1
:widths: 22 12 12 54

* - Parameter
  - Type
  - Default
  - Description
* - `model_dir`
  - str
  - `"models/clip_aesthetic"`
  - Directory for model weights; downloaded on each node if missing.
* - `score_threshold`
  - float
  - 0.5
  - Minimum aesthetic score required to keep a clip.
* - `reduction`
  - {"mean", "min"}
  - `"min"`
  - Aggregate frame‑level scores using mean or minimum.
* - `target_fps`
  - float
  - 1.0
  - Frame sampling rate expected to match extracted frames.
* - `num_gpus_per_worker`
  - float
  - 0.25
  - GPUs reserved per worker for aesthetic scoring.
* - `verbose`
  - bool
  - `False`
  - Log per‑clip aesthetic scores and decisions.
```

#### Aesthetic Outputs

- Adds `aesthetic_score` to each clip.
- Moves filtered clips to `video.filtered_clips` and increments `video.clip_stats.num_filtered_by_aesthetic`.


