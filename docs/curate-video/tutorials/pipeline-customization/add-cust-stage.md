---
description: "Advanced tutorial for adding custom processing stages to video curation pipelines for specialized workflow requirements"
categories: ["video-curation"]
tags: ["customization", "pipeline", "stages", "workflow", "advanced", "development"]
personas: ["mle-focused"]
difficulty: "advanced"
content_type: "tutorial"
modality: "video-only"

---

(video-tutorials-pipeline-cust-add-stage)=
# Adding Custom Stages

Learn how to customize the NeMo Curator Container by adding new pipeline stages.

The NeMo Video Curator container includes a series of pipelines with default stages, however, they may not always meet your pipeline requirements. In this tutorial, we'll demonstrate how to add a new pipeline stage that uses a new environment, code, and model.

## Before You Start

Before you begin adding a new pipeline stage, make sure that you have:

* Reviewed the [pipeline concepts and diagrams](about-concepts-video).  
* Downloaded the NeMo Video Curator container.  
* Reviewed the [default environments](reference-infrastructure-container-environments) available.  
* Optionally [created custom code](video-tutorials-pipeline-cust-add-code) that defines your new requirements.  
* Optionally [created a custom environment](video-tutorials-pipeline-cust-env) to support your new custom code.  
* Optionally [created a custom model](video-tutorials-pipeline-cust-add-model).  

## How to Add a Custom Pipeline Stage

### 1. Define the Stage Class

```py
class CRadioEmbeddingStage(ray_utils.Stage):
    def __init__(self) -> None:
        model_resolution = "256"
        self._model = CRadio(resolution=model_resolution)
        self.interp = cv2.INTER_LINEAR
```

### 2. Specify Resource Requirements

```py
@property 
def conda_env_name(self) -> str: 
return "video_splitting"

@property 
def num_gpus_per_worker(self) -> Optional[float]: 
return 1.0

@property 
def model(self) -> model_utils.ModelInterface: 
return self._model 
```

### 3. Implement Core Methods

Required methods for every stage:

#### Setup Method

```py
def setup(self) -> None: 
self._model.setup()
```

#### Process Data Method

```py
def process_data(self, task: SplitPipeTask) -> List[SplitPipeTask]: 
# Process implementation return [task]
```

### 4. Update Data Model

Modify the pipeline's data model to include your stage's outputs:

```py
@attrs.define 
class Clip: 
# Existing fields... 
# your_new_field: Optional[npt.NDArray[np.float32]] = None 
```

### 5. Modify Pipeline Output Handling

Update the ClipWriterStage to handle your stage's output:

1. Create a writer method:

   ```py
   def _write_custom_output(self, clip: Clip) -> None:
   # writing implementation
   ```

2. Add to the main process:

   ```py
   def process_data(self, task: SplitPipeTask) -> Optional[List[SplitPipeTask]]:
         # existing processing
   self._write_custom_output(clip)
    # continue processing
   ```

## Integration Steps

### 1. Update Container Code

```sh
video_curator image extend \
    --base-image nemo_video_curator:1.0.0 \
    --extra-code-paths nemo_curator/video/
```

### 2. Download Required Model Weights

```sh
video_curator launch \
    --image-name nemo_video_curator \
    --image-tag 1.0.0 \
    --curator-path . \
    --python3 -m nemo_curator.video.models.model_cli download
```

### 3. Run Updated Pipeline

```sh
video_curator launch \
   --image-name nemo_video_curator \
   --image-tag 1.0.0 \
   --python3 -m nemo_curator.video.pipelines.video.run_pipeline split \
   --input-video-path /config/input_videos/ \
   --output-clip-path /config/clips/ 
```
