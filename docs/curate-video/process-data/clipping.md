---
description: "Split videos into clips using fixed stride or TransNetV2 scene-change detection"
categories: ["video-curation"]
tags: ["clipping", "fixed-stride", "transnetv2", "video"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "howto"
modality: "video-only"
---

(video-process-clipping)=

# Video Clipping

Split long videos into shorter clips for downstream processing.

NeMo Curator provides two clipping stages: **Fixed Stride** and **TransNetV2** scene-change detection.

- Use Fixed Stride create uniform segments.
- Use TransNetV2 to cut at visual shot boundaries.

---

## Clipping Options

### Fixed Stride

The `FixedStrideExtractorStage` steps through the video duration by `clip_stride_s`, creating spans of length `clip_len_s` (it truncates the final span at the video end when needed). It filters spans shorter than `min_clip_length_s` and appends `Clip` objects identified by source and frame indices.

```python
from nemo_curator.stages.video.clipping.clip_extraction_stages import FixedStrideExtractorStage

stage = FixedStrideExtractorStage(
    clip_len_s=10.0,
    clip_stride_s=10.0,
    min_clip_length_s=2.0,
    limit_clips=0,
)
```

:::{tip} If `limit_clips > 0` and the `Video` already has clips, the stage skips processing. It does not cap the number of clips generated within the same run.
:::

### TransNetV2 Scene-Change Detection

TransNetV2 is a shot-boundary detection model that identifies transitions between shots. The stage converts those transitions into scenes, applies length/crop rules, and emits clips aligned to scene boundaries.

Using extracted frames of size 27×48×3, the model predicts shot transitions, converts them into scenes, and applies filtering: `min_length_s`, `max_length_s` with `max_length_mode` ("truncate" or "stride"), and optional `crop_s` at both ends. It creates `Clip` objects for the resulting spans, then stops after it reaches `limit_clips` (> 0), and releases frames from memory after processing.

1. Run `VideoFrameExtractionStage` first to populate `video.frame_array`.

   ```python
   from nemo_curator.stages.video.clipping.video_frame_extraction import VideoFrameExtractionStage
   from nemo_curator.stages.video.clipping.transnetv2_extraction import TransNetV2ClipExtractionStage

   frame_extractor = VideoFrameExtractionStage(
       decoder_mode="pynvc",  # or "ffmpeg_gpu", "ffmpeg_cpu"
       verbose=True,
   )
   ```

    :::{important}
    Frames must be `(27, 48, 3)` per frame; the stage accepts arrays shaped `(num_frames, 27, 48, 3)` and transposes from `(48, 27, 3)` automatically.
    :::

2. Configure TransNetV2 and run the stage in your pipeline to generate clips from the detected scenes.

   ```python
   transnet = TransNetV2ClipExtractionStage(
       model_dir="/models",
       threshold=0.4,
       min_length_s=2.0,
       max_length_s=10.0,
       max_length_mode="stride",  # or "truncate"
       crop_s=0.5,
       gpu_memory_gb=10.0,
       limit_clips=-1,
       verbose=True,
   )
   ```
