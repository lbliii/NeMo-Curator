---
description: "Tutorial for adding custom code to video curation pipelines for specialized processing requirements"
categories: ["video-curation"]
tags: ["customization", "custom-code", "pipeline", "advanced", "development"]
personas: ["mle-focused"]
difficulty: "advanced"
content_type: "tutorial"
modality: "video-only"

---

(video-tutorials-pipeline-cust-add-code)=
# Adding Custom Code

Learn how to customize the NeMo Curator Container by adding custom code to either a new or existing pipeline stage.

The NeMo Video Curator container includes a robust set of default pipelines with commonly used stages, however, they may not always meet your pipeline requirements. In this tutorial, we'll demonstrate how to extend the default pipeline.

## Before You Start

Before you begin adding custom code, make sure that you have:

* Reviewed the [pipeline concepts and diagrams](about-concepts-video).  
* Downloaded the NeMo Video Curator container.  
* Reviewed the [default environments](reference-infrastructure-container-environments-video) available.  
* Installed the `nemo_curator/video` code base into your developer environment.  
* Optionally [created a custom environment](video-tutorials-pipeline-cust-env) to support your new custom code.

---

## How to Add Custom Code

### Define New Functionality

1. Create a `custom_code` directory anywhere on your system to organize your custom pipeline code.  
2. Create a new folder for your environment, for example: `new_stage/`.
3. Create a new file, for example `my_file.py`. This file must define a class (`MyClass`) made available for import.

   ```py
   # your code here
   ```

4. Import the class at x location to include it in your pipeline stages.

   ```py
   from nemo_curator.my_code.my_file import MyClass

   ...
   ```

5. Save the files.

### Build the Container

#### Extend

Use the following command to extend the default NeMo Video Curator image using your new code:

   ```bash
   video_curator image extend \
       --base-image nemo_video_curator:1.0.0 \
       --extra-code-paths custom_code/new_stage/
   ```

#### Overwrite

Use the following command to overwrite the default code in the container with the customized version in your local developer environment:

   ```bash
   video_curator image extend \
       --base-image nemo_video_curator:1.0.0 \
       --extra-code-paths nemo_curator/video/
   ```

The customized container image is output as `nemo_video_curator:1.0.0-ext`. Be sure to give it a unique name so that you don't overwrite when creating additional custom environments. You can retag the image to something more descriptive by running

```bash
docker tag nemo_video_curator:1.0.0-ext my_env_video_curator:1.1.0
```

## Next Steps

Now that you have created custom code, you can [create a custom stage](video-tutorials-pipeline-cust-add-stage) that uses your code.
