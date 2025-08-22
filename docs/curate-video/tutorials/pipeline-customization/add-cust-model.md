---
description: "Tutorial for integrating custom models into video curation pipelines for specialized captioning, embedding, or filtering tasks"
categories: ["video-curation"]
tags: ["customization", "models", "machine-learning", "pipeline", "captioning", "embedding", "advanced"]
personas: ["mle-focused", "data-scientist-focused"]
difficulty: "advanced"
content_type: "tutorial"
modality: "video-only"

---

(video-tutorials-pipeline-cust-add-model)=
# Adding Custom Models

Learn how to customize the NeMo Curator Container by adding custom models.

The NeMo Video Curator container includes a robust set of default models, however, they may not always meet your pipeline requirements. In this tutorial, we'll demonstrate how to add a custom x model used in a new pipeline stage.

## Before You Start

Before you begin adding a custom model, make sure that you have:

* Reviewed the [pipeline concepts and diagrams](about-concepts-video).  
* Downloaded the NeMo Video Curator container.  
* Reviewed the [default environments](reference-infrastructure-container-environments) available.  
* Installed the `nemo_curator/video` code base into your developer environment.  
* Optionally [created a custom environment](video-tutorials-pipeline-cust-env) to support your new custom model.

---

## How to Add Custom Code

### Review Model Interface

In NeMo Curator, models are defined by classes inheriting from `nemo_curator.video.models.model_utils.ModelInterface`. The interface looks like this:

```py
class ModelInterface(abc.ABC):
    """
    Abstract base class that defines an interface for machine learning models,
    specifically focused on their weight handling and environmental setup.

    This interface allows our pipeline code to download weights locally and setup models in a uniform
    way. It does not place any restrictions on how inference is run.
    """

    @property
    @abc.abstractmethod
    def weights_names(self) -> list[str]:
        """
        Returns a list of weight names associated with the model.

        In NeMo Curator, each set of weights has a name associated with it. This is oftem the huggingspace name for those
        weights (e.g. Salesforce/instructblip-vicuna-13b). but doesn't need to be. We use these names to push/pull
        weights to/from S3.

        Returns:
            A list of strings.
        """
        pass

    @property
    @abc.abstractmethod
    def id_file_mapping(self) -> dict[str, list[str]]:
        """
        Returns a mapping of model id to a list of file names associated with the model ids.

        In NeMo Curator, each set of weights has a name associated with it. This is often the huggingspace name for those
        weights (e.g. Salesforce/instructblip-vicuna-13b). but doesn't need to be. We use these names to push/pull
        weights to/from S3.

        Returns:
            A dictionary of model id to a list of file names. If the list of files is None, that means all files should be
            downloaded.
        """
        pass

    @property
    def num_gpus(self) -> float:
        """
        Returns the number of GPUs needed to run a single instance of this model.

        This will typically be 1, but may be greater than 1 for model-parallel models or less than one for models which
        only take up a small amount of a GPUs memory footprint or processing power. If less than one, multiple models may be scheduled on the same GPU.

        Defaults to 1.0 if not sepcified.

        Returns:
            A float representing the number of GPUs.
        """
        return 1.0

    @property
    @abc.abstractmethod
    def conda_env_name(self) -> str:
        """
        Returns the name of the conda environment that this model must be run from.

        Returns:
            A string representing the conda environment name.
        """
        pass

    @abc.abstractmethod
    def setup(self) -> None:
        """
        Sets up the model for use, such as loading weights and building computation graphs.
        """
        pass
```

### Create New Model

For this tutorial, we'll create a simplified version of our C-RADIO model.

```py

import math
from typing import Optional, Union

import numpy as np
import numpy.typing as npt
import torch
from loguru import logger

from nemo_curator.video.models import model_utils
from nemo_curator.video.utils import conda_utils

# Guard the import so there are no errors for actors not using this env
if conda_utils.is_running_in_env("my_env"):
    from transformers import AutoModel

# The name of the model on HuggingFace
WEIGHTS_NAME = "nvidia/C-RADIO"

class CRadioCore(torch.nn.Module):
    def __init__(self, max_width: int, max_height: Optional[int]):
        super().__init__()
        self.max_width = max_width
        self.max_height = max_height
        weight_file = model_utils.get_local_dir_for_weights_name(WEIGHTS_NAME)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.cradio = AutoModel.from_pretrained(weight_file, trust_remote_code=True).to(self.device)
        self.dtype = torch.float32

    @torch.no_grad()
    def __call__(
        self, images: Union[torch.Tensor, npt.NDArray[np.uint8]]
    ) -> torch.Tensor:
        inputs = images.to(self.dtype).to(self.device)
        inputs = inputs / 255
        embed, _ = self.cradio(inputs)
        return embed

class CRadio(model_utils.ModelInterface):
    def __init__(self, resolution: str = "256") -> None:
        self.resolution = resolution

    def setup(self) -> None:
        max_width = int(self.resolution)
        max_height = None
        self.model = CRadioCore(max_width, max_height)
        self.model.eval()

    @property
    def weights_names(self) -> list[str]:
        return [WEIGHTS_NAME]

    @property
    def id_file_mapping(self) -> dict[str, list[str]]:
        return {
            WEIGHTS_NAME: None,
        }

    @property
    def conda_env_name(self) -> str:
        return "video_splitting"

    @property
    def num_gpus(self) -> float:
        return 1.0

    def __call__(
        self, images: Union[torch.Tensor, npt.NDArray[np.uint8]]
    ) -> torch.Tensor:
        return self.model(images)
```

Let's go through each part of the code piece by piece.

#### Define Guard Imports

```py
if conda_utils.is_running_in_env("video_splitting"):
    from transformers import AutoModel
```

This condition checks to make sure we are running in a Conda environment that has our model's dependencies.

#### Define the PyTorch Model

```py
# The name of the model on HuggingFace
WEIGHTS_NAME = "nvidia/C-RADIO"

class CRadioCore(torch.nn.Module):
    def __init__(self, max_width: int, max_height: Optional[int]):
        super().__init__()
        self.max_width = max_width
        self.max_height = max_height
        weight_file = model_utils.get_local_dir_for_weights_name(WEIGHTS_NAME)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.cradio = AutoModel.from_pretrained(weight_file, trust_remote_code=True).to(self.device)
        self.dtype = torch.float32
```

`WEIGHTS_NAME = "nvidia/C-RADIO"` is used to define where the model is on HuggingFace, and where it will be in our local model weights cache. During the execution of the pipelines the model weights for all models will be downloaded before `CRadio.setup()` is called (and therefore before `CRadioCore` is constructed), so you may assume the weights will be at `model_utils.get_local_dir_for_weights_name(WEIGHTS_NAME)`

#### Define the Model Interface

```py
class CRadio(model_utils.ModelInterface):
	...
```

Our `CRadio` class implements the model interface. It defines a collection of methods that ensure the model weights can be downloaded and that it is initialized properly.

```py
    def setup(self) -> None:
        max_width = int(self.resolution)
        max_height = None
        self.model = CRadioCore(max_width, max_height)
        self.model.eval()
```

The setup method initializes the underlying `CRadioCore` class that performs the model inference.

```py
    @property
    def weights_names(self) -> list[str]:
        return [WEIGHTS_NAME]
```

The `weights_names` property returns a list of weights. These are used to identify the model weights that are cached locally or on S3. They typically correspond to the name of the HuggingFace models, but they don't have to.

```py
    @property
    def id_file_mapping(self) -> dict[str, list[str]]:
        return {
            WEIGHTS_NAME: None,
        }
```

`id_file_mapping` is used when running the model download/upload script to selectively choose which files from the model repository should be downloaded. We don't need to make such a selection here, so we mark it as `None`.

```py
    @property
    def conda_env_name(self) -> str:
        return "video_splitting"
```

`conda_env_name` defines the conda environment that should be used when running this model in a pipeline.

```py
    @property
    def num_gpus(self) -> float:
        return 1.0
```

`num_gpus` specifies the fractional amount of GPU resources that this model will need. This value is only used for scheduling workers across GPUs or on the same GPU, and it does nothing to actually limit the usage of the GPU(s) allocated to this model.

### Modify the model download config

NeMo Curator's model download utility reads from a configuration file to determine which model weights to download. We should add our model to the config located at `nemo_curator/video/config/model_download.yaml`. Assuming your new model is placed under `nemo_curator/video/models/my_model.py`, we should modify it to look like this

```yaml
models:
  - class: nemo_curator.video.models.cradio.CRadio
  - class: nemo_curator.video.models.internvideo2_mm.InternVideo2MultiModality
  - class: nemo_curator.video.models.qwen_vl.QwenVL
  - class: nemo_curator.video.models.t5_encoder.T5Encoder
    params:
      variant: 1
  - class: nemo_curator.video.models.transnetv2.TransNetV2
  - class: nemo_curator.video.models.my_model.MyModelClass
```

## Next Steps

Now that you have created a custom model, you can [create a custom stage](video-tutorials-pipeline-cust-add-stage) that uses your code.