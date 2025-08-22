---
description: "Beginner-friendly tutorial for getting started with video curation using NeMo Curator's default pipelines"
categories: ["video-curation"]
tags: ["beginner", "tutorial", "quickstart", "pipeline", "video-processing", "docker"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "beginner"
content_type: "tutorial"
modality: "video-only"

---

(video-tutorials-beginner)=
# Create a Basic Pipeline

To get started, we will run the `hello_world_pipeline`.

This example pipeline is a simple pipeline which processes simple strings, first converting them to lowercase, then printing them, and finally generating a response using a GPT-2 model.

## Build the image

All pipelines are contained in docker images. To build the image called `example_pipeline`, run the following command:

```{seealso}
For information about video container environments, see [Video Curator Environments](reference-infrastructure-container-environments-video).
```

```bash
video_curator image build \
    --image-name example_pipeline \
    --image-tag 1.0.0 \
    --envs model_download,transformers \
    --extra-code-paths nemo_curator/video/
```

Once done, you should be able to see the image in the local docker registry.

```text
docker images
REPOSITORY                   TAG       IMAGE ID       CREATED             SIZE
example_pipeline             1.0.0     bce56d59af46   About an hour ago   37.1GB
```

:::{note}
If you have previously created the image, and wish to remove the old image, you can do so with the following command:

```bash
docker rmi example_pipeline:1.0.0
```
:::

## Download GPT-2 model

The pipeline uses a GPT-2 model, which must be downloaded into the container:

```bash
cp nemo_curator/video/config/example_model_download.yaml ~/nemo_curator_local_workspace/
video_curator launch \
    --image-name example_pipeline \
    --image-tag 1.0.0 \
    --curator-path . -- \
        python3 -m nemo_curator.video.models.model_cli download \
        --config-file /config/example_model_download.yaml
```

## Run the pipeline

Now that the image is fully prepared, we can run the pipeline:

```bash
video_curator launch \
    --image-name example_pipeline \
    --image-tag 1.0.0 \
    --curator-path . -- \
      python3 -m nemo_curator.video.pipelines.examples.hello_world_pipeline
```

Running this will output a considerable amount of text. A few specific lines are notable showing the progress of one run through the pipeline can be seen here:

```
(Stage00-_LowerCase pid=453) 2025-03-19 01:42:40.655 | DEBUG    | __main__:process_data:48 - processing task prompt='A good recipe always starts with' in stage=_LowerCaseStage pid=453 env=
...
(Stage01-_Print pid=452) 2025-03-19 01:42:40.792 | DEBUG    | __main__:process_data:63 - processing task prompt='a good recipe always starts with' in stage=_PrintStage pid=452 env=
(Stage01-_Print pid=452) 2025-03-19 01:42:40.792 | INFO     | __main__:process_data:65 - a good recipe always starts with
...
(Stage02-_GPT2 pid=2474) 2025-03-19 01:42:43.995 | DEBUG    | __main__:process_data:82 - processing task prompt='a good recipe always starts with' in stage=_GPT2Stage pid=2474 env=transformers
...
(Stage02-_GPT2 pid=2474) 2025-03-19 01:42:44.442 | INFO     | __main__:process_data:85 - a good recipe always starts with a little bit of salt. The best way to make this is by adding some water and baking it in the oven for about 10 minutes, or until golden brown on top. I like mine at least 1 hour longer than my regular one so you can get your hands dirty if that's
...
2025-03-19 01:42:46.642 | INFO     | nemo_curator.video.ray_utils.execution_modes._streaming:run_pipeline:231 - All stages are done. Finishing pipeline.
2025-03-19 01:42:46.659 | INFO     | nemo_curator.video.ray_utils._pipelines:run_pipeline:282 - Disconnecting from Ray cluster in 5 seconds
2025-03-19 01:42:53.197 | INFO     | __main__:main:104 - Pipeline completed
```
