---
description: "Guide to creating and managing custom Docker environments for specialized video curation pipeline requirements"
categories: ["video-curation"]
tags: ["customization", "docker", "environments", "pipeline", "deployment", "advanced"]
personas: ["mle-focused", "devops-focused"]
difficulty: "advanced"
content_type: "tutorial"
modality: "video-only"

---

(video-tutorials-pipeline-cust-env)=
# Add Custom Environment

Learn how to customize the NeMo Curator Container by adding new Conda Environments.

The NeMo Video Curator container includes a series of [default environments](reference-infrastructure-container-environments) with pre-installed dependencies, however, they may not always meet your pipeline requirements. In this tutorial, we'll demonstrate how to add a new custom environment to support a custom x stage.

## Before You Start

Before you begin adding a new conda environment, make sure that you have:

* Reviewed the [pipeline concepts and diagrams](about-concepts-video).  
* Downloaded the NeMo Video Curator container.  
* Reviewed the [default environments](reference-infrastructure-container-environments) available.  
* Optionally [created custom code](video-tutorials-pipeline-cust-add-code) that defines your new requirements.  

---

## How to Add a Custom Conda Environment

### Define Build Steps

1. Create an `environments` directory anywhere on your system to organize your custom pipeline stage environments.  
2. Create a new folder for your environment, for example: `my-env/`.
3. Create a `build_steps.dockerfile.j2` file. This file installs your new environment's dependencies on top of the container.

   ```bash
   RUN micromamba install -c nvidia/label/cuda-12.1.1 -c conda-forge \
       python=3.10.14 pip=23.2 cuda cuda-nvcc cuda-toolkit cuda-runtime pycuda

   RUN pip install accelerate==0.32.1 av==13.1.0 packaging==24.0 ninja==1.11.1.1 \
       torch==2.2.1 torchvision torchaudio transformers==4.42.3 \
       scenedetect==0.6.4 PyNvVideoCodec==1.0.2 timm==0.9.12
   RUN wget -P /tmp/ https://github.com/CVCUDA/CV-CUDA/releases/download/v0.11.0-beta/cvcuda_cu12-0.11.0b0-cp310-cp310-linux_x86_64.whl \
       && pip install /tmp/cvcuda_cu12-0.11.0b0-cp310-cp310-linux_x86_64.whl \
       && rm -f /tmp/cvcuda_cu12-0.11.0b0-cp310-cp310-linux_x86_64.whl
   RUN pip install flash-attn==2.6.1 --no-build-isolation
   ```

4. Save the file.

### Build the Container

Use the following command to extend the default NeMo Video Curator image using your new environment:

```bash
video_curator image extend \
    --base-image nemo_video_curator:1.0.0 \
    --new-envs my_env \
    --env-dirs ./environments/
```

The customized container image is output as `nemo_video_curator:1.0.0-ext`. Be sure to give it a unique name so that you don't overwrite when creating additional custom environments. You can retag the image to something more descriptive by running

```bash
docker tag nemo_video_curator:1.0.0-ext my_env_video_curator:1.1.0
```

## Next Steps

Now that you have created a custom environment, you can [create custom code](video-tutorials-pipeline-cust-add-code) for that environment.
