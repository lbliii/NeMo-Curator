---
description: "Choose and configure execution backends for NeMo Curator pipelines"
categories: ["reference"]
tags: ["executors", "xenna", "ray", "ray-data", "actor-pool", "pipelines"]
personas: ["data-scientist-focused", "mle-focused", "admin-focused"]
difficulty: "reference"
content_type: "reference"
modality: "universal"
---

(reference-execution-backends)=

# Pipeline Execution Backends

Executors run NeMo Curator `Pipeline` workflows across your compute resources. This reference explains the available backends and how to configure them. It applies to all modalities (text, image, video).

## How it Works

Build your pipeline by adding stages, then run it with an executor:

```python
from ray_curator.pipeline import Pipeline

pipeline = Pipeline(name="example_pipeline", description="Curator pipeline")
# pipeline.add_stage(...)

# Choose an executor below and run
# results = pipeline.run(executor)
```

## Available Backends

### `XennaExecutor` (recommended)

```python
from ray_curator.backends.xenna import XennaExecutor

executor = XennaExecutor(
    config={
        # 'streaming' (default) or 'batch'
        "execution_mode": "streaming",
        # seconds between status logs
        "logging_interval": 60,
        # continue on failures
        "ignore_failures": False,
        # CPU allocation ratio (0-1)
        "cpu_allocation_percentage": 0.95,
        # streaming autoscale interval (seconds)
        "autoscale_interval_s": 180,
    }
)

results = pipeline.run(executor)
```

Pass options via `config`; they map to the executor’s pipeline configuration.

### `RayDataExecutor` (experimental)

```python
from ray_curator.backends.experimental.ray_data import RayDataExecutor

executor = RayDataExecutor()
results = pipeline.run(executor)
```

Notes:

- Emits an experimental warning; the API and performance characteristics may change.

### `RayActorPoolExecutor` (experimental)

```python
from ray_curator.backends.experimental.ray_actor_pool import RayActorPoolExecutor

executor = RayActorPoolExecutor(
    config={
        # Optional capacity reservations used by the actor planning logic
        "reserved_cpus": 0.0,
        "reserved_gpus": 0.0,
    }
)
results = pipeline.run(executor)
```

Notes:

- Uses Ray’s `ActorPool` for fine-grained load balancing and back-pressure control.
- Supports specialized RAFT actor stages when configured by a stage.

## Choosing a Backend

- **`XennaExecutor`**: default choice for most workloads; supports streaming and batch execution modes with auto-scaling.
- **Ray Data (experimental)**: useful for Ray Data–centric transformations; expect API evolution.
- **Ray Actor Pool (experimental)**: try for bespoke actor-level control and advanced scheduling patterns.

## Minimal End-to-End example

```python
from ray_curator.pipeline import Pipeline
from ray_curator.backends.xenna import XennaExecutor

# Build your pipeline
pipeline = Pipeline(name="curator_pipeline")
# pipeline.add_stage(stage1)
# pipeline.add_stage(stage2)

# Run with Xenna (recommended)
executor = XennaExecutor(config={"execution_mode": "streaming"})
results = pipeline.run(executor)

print(f"Completed with {len(results) if results else 0} output tasks")
```

To use a different backend, replace the executor with Ray Data or Ray Actor Pool as shown above.
