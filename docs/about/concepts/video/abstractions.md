---
description: "Key abstractions in video curation including stages, pipelines, and execution modes for scalable processing"
categories: ["concepts-architecture"]
tags: ["abstractions", "pipeline", "stages", "video-curation", "distributed", "ray"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "concept"
modality: "video-only"
only: not ga
---

(about-concepts-video-abstractions)=
# Key Abstractions

NeMo Curator introduces core abstractions to organize and scale video curation workflows:

- **Tasks**: The unit of data that flows through a pipeline (for video, `VideoTask` holding a `Video` and its `Clip` objects).
- **Stages**: Individual processing units that perform a single step (for example, reading, splitting, transcoding, filtering, embedding, captioning, writing).
- **Pipelines**: Ordered sequences of stages forming an end-to-end workflow.
- **Executors**: Components that run pipelines on a backend (Ray) with autoscaling.

![Stages and Pipelines](./_images/stages-pipelines-diagram.png)

## Stages

A stage represents a single step in your data curation workflow. For example, stages can:

- Download videos
- Transcode media
- Split videos into clips
- Generate embeddings
- Calculate scores

### Stage Architecture

Each processing stage:

1. Inherits from `ProcessingStage`
2. Declares a stable `name` and `resources: Resources` (CPUs, GPU memory or GPUs, optional NVDEC/NVENC)
3. Defines `inputs()`/`outputs()` to document required attributes and produced attributes on tasks
4. Implements `setup(worker_metadata)` for model initialization and `process(task)` to transform tasks

This design allows map-style, retry-safe execution and dynamic scaling per stage.

```python
class MyStage(ProcessingStage[X, Y]):
    @property
    def name(self) -> str: ...

    @property
    def resources(self) -> Resources: ...

    def inputs(self) -> tuple[list[str], list[str]]: ...
    def outputs(self) -> tuple[list[str], list[str]]: ...

    def setup(self, worker_metadata: WorkerMetadata | None = None) -> None: ...
    def process(self, task: X) -> Y | list[Y]: ...
```

Refer to the stage base and resources definitions in Curator for full details.

## Pipelines

A pipeline orchestrates multiple stages into an end-to-end workflow. Key characteristics:

- **Stage Sequence**: Stages must follow a logical order where each stage's output feeds into the next
- **Input Configuration**: Specifies the data source location
- **Model Configuration**: Defines the path to model weights, which are cached on each node
- **Execution Mode**: Supports streaming and batch processing via the executor

### Tasks (Video)

Video pipelines operate on task types defined in Curator:

- `VideoTask`: wraps a single input `Video`
- `Video`: holds decoded metadata, frames, and lists of `Clip`
- `Clip`: holds buffers, extracted frames, embeddings, and caption windows

These tasks are transformed stage-by-stage (for example, `VideoReader` populates `Video`, splitting stages create `Clip` objects, embedding and captioning stages annotate clips, and writer stages persist outputs).

### Executors

Executors run pipelines on a backend. Curator uses `XennaExecutor` to translate `ProcessingStage` definitions into Xenna stage specs and run them on Ray with autoscaling (streaming or batch).
