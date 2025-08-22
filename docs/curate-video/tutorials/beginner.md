---
description: "Beginner-friendly tutorial for running your first Ray-based video splitting pipeline using the Python example"
categories: ["video-curation"]
tags: ["beginner", "tutorial", "quickstart", "pipeline", "video-processing", "ray", "python"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "beginner"
content_type: "tutorial"
modality: "video-only"

---

(video-tutorials-beginner)=
# Create a Basic Pipeline

To get started, run the video splitting example script that reads videos, splits clips, and writes outputs.

## Prerequisites

Follow the [Get Started guide](gs-video) to install the package, prepare the model directory, and set up your data paths.

## Run the example

Define your paths:

```bash
DATA_DIR=/path/to/videos
OUT_DIR=/path/to/output_clips
MODEL_DIR=/path/to/models
```

Run the splitting example:

```bash
python -m ray_curator.examples.video.video_split_clip_example \
  --video-dir "$DATA_DIR" \
  --model-dir "$MODEL_DIR" \
  --output-clip-path "$OUT_DIR" \
  --splitting-algorithm fixed_stride \
  --fixed-stride-split-duration 10.0 \
  --embedding-algorithm internvideo2 \
  --transcode-encoder libopenh264 \
  --verbose
```

You should see the pipeline description, executor start, and stage logs during execution. Once complete, outputs are under `$OUT_DIR`.

```{seealso}
See [Splitting Pipeline](video-pipelines-splitting) for more options and performance tuning.
```
