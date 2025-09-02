---
description: "Generate clip captions with Qwen and optional preview images"
categories: ["video-curation"]
tags: ["captions", "qwen", "preview", "video"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "howto"
modality: "video-only"
---

(video-process-captions-preview)=

# Captions and Preview

Prepare inputs, generate captions, optionally enhance them, and produce preview images.

## Preparation and previews

```python
from nemo_curator.stages.video.caption.caption_preparation import CaptionPreparationStage
from nemo_curator.stages.video.preview.preview import PreviewStage

prep = CaptionPreparationStage(
    model_variant="qwen",
    prompt_variant="default",
    prompt_text=None,
    sampling_fps=2.0,
    window_size=256,
    remainder_threshold=128,
    preprocess_dtype="float16",
    model_does_preprocess=False,
    generate_previews=True,
    verbose=True,
)
preview = PreviewStage(
    target_fps=1,
    target_height=240,
    verbose=True,
)
```

## Caption generation and enhancement

```python
from nemo_curator.stages.video.caption.caption_generation import CaptionGenerationStage
from nemo_curator.stages.video.caption.caption_enhancement import CaptionEnhancementStage

gen = CaptionGenerationStage(
    model_dir="/models",
    model_variant="qwen",
    caption_batch_size=8,
    fp8=False,
    max_output_tokens=512,
    model_does_preprocess=False,
    generate_stage2_caption=False,
    stage2_prompt_text=None,
    disable_mmcache=True,
)
enh = CaptionEnhancementStage(
    model_dir="/models",
    model_variant="qwen",
    prompt_variant="default",
    prompt_text=None,
    model_batch_size=128,
    fp8=False,
    max_output_tokens=512,
    verbose=True,
)
```

## Preview Generation

Generate lightweight `.webp` previews for each caption window to support review and QA workflows. A dedicated `PreviewStage` reads per-window `mp4` bytes and encodes WebP using `ffmpeg`.

### Preview Parameters

- `target_fps` (default `1.0`): Target frames per second for preview generation.
- `target_height` (default `240`): Output height. Width auto-scales to preserve aspect ratio.
- `compression_level` (range `0–6`, default `6`): WebP compression level. `0` is lossless; higher values reduce size with lower quality.
- `quality` (range `0–100`, default `50`): WebP quality. Higher values increase quality and size.
- `num_cpus_per_worker` (default `4.0`): Number of CPU threads mapped to `ffmpeg -threads`.
- `verbose` (default `False`): Emit more logs.

Behavior notes:

- If the input frame rate is lower than `target_fps` or the input height is lower than `target_height`, the stage logs a warning and preview quality can degrade.
- If `ffmpeg` fails, the stage logs the error and skips assigning preview bytes for that window.

### Example: Configure PreviewStage

```python
from nemo_curator.stages.video.preview.preview import PreviewStage

preview = PreviewStage(
    target_fps=1.0,
    target_height=240,
    compression_level=6,
    quality=50,
    num_cpus_per_worker=4.0,
    verbose=False,
)
```

### CLI Options (example pipeline)

When using the example pipeline, enable previews and set targets:

```bash
python examples/video/video_split_clip_example.py \
  --video-dir /data/videos \
  --model-dir /models \
  --output-clip-path /outputs \
  --generate-captions \
  --generate-previews \
  --preview-target-fps 1 \
  --preview-target-height 240
```

### Outputs

The stage writes `.webp` files under the `previews/` directory that `ClipWriterStage` manages. Use the helper to resolve the path:

```python
from nemo_curator.stages.video.io.clip_writer import ClipWriterStage
previews_dir = ClipWriterStage.get_output_path_previews("/outputs")
```

Refer to Save & Export for directory structure and file locations: [Save & Export](video-save-export).

### Requirements and Troubleshooting

- `ffmpeg` with WebP (`libwebp`) support must be available in the environment.
- If you observe warnings about low frame rate or height, consider lowering `target_fps` or `target_height` to better match inputs.
- On encoding errors, check logs for the `ffmpeg` command and output to diagnose missing encoders.

<!-- end -->
