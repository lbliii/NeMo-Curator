# {py:mod}`classifiers.prompt_task_complexity`

```{py:module} classifiers.prompt_task_complexity
```

```{autodoc2-docstring} classifiers.prompt_task_complexity
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CustomHFDeberta <classifiers.prompt_task_complexity.CustomHFDeberta>`
  - ```{autodoc2-docstring} classifiers.prompt_task_complexity.CustomHFDeberta
    :summary:
    ```
* - {py:obj}`MeanPooling <classifiers.prompt_task_complexity.MeanPooling>`
  - ```{autodoc2-docstring} classifiers.prompt_task_complexity.MeanPooling
    :summary:
    ```
* - {py:obj}`MulticlassHead <classifiers.prompt_task_complexity.MulticlassHead>`
  - ```{autodoc2-docstring} classifiers.prompt_task_complexity.MulticlassHead
    :summary:
    ```
* - {py:obj}`PromptTaskComplexityClassifier <classifiers.prompt_task_complexity.PromptTaskComplexityClassifier>`
  - ```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityClassifier
    :summary:
    ```
* - {py:obj}`PromptTaskComplexityConfig <classifiers.prompt_task_complexity.PromptTaskComplexityConfig>`
  - ```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityConfig
    :summary:
    ```
* - {py:obj}`PromptTaskComplexityModel <classifiers.prompt_task_complexity.PromptTaskComplexityModel>`
  - ```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityModel
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PROMPT_TASK_COMPLEXITY_IDENTIFIER <classifiers.prompt_task_complexity.PROMPT_TASK_COMPLEXITY_IDENTIFIER>`
  - ```{autodoc2-docstring} classifiers.prompt_task_complexity.PROMPT_TASK_COMPLEXITY_IDENTIFIER
    :summary:
    ```
````

### API

`````{py:class} CustomHFDeberta(config: dataclasses.dataclass)
:canonical: classifiers.prompt_task_complexity.CustomHFDeberta

Bases: {py:obj}`torch.nn.Module`, {py:obj}`huggingface_hub.PyTorchModelHubMixin`

```{autodoc2-docstring} classifiers.prompt_task_complexity.CustomHFDeberta
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.prompt_task_complexity.CustomHFDeberta.__init__
```

````{py:method} compute_results(preds: torch.Tensor, target: str, decimal: int = 4) -> tuple[list[str], list[str], list[float]]
:canonical: classifiers.prompt_task_complexity.CustomHFDeberta.compute_results

```{autodoc2-docstring} classifiers.prompt_task_complexity.CustomHFDeberta.compute_results
```

````

````{py:method} forward(batch: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]
:canonical: classifiers.prompt_task_complexity.CustomHFDeberta.forward

```{autodoc2-docstring} classifiers.prompt_task_complexity.CustomHFDeberta.forward
```

````

````{py:method} process_logits(logits: list[torch.Tensor]) -> dict[str, torch.Tensor]
:canonical: classifiers.prompt_task_complexity.CustomHFDeberta.process_logits

```{autodoc2-docstring} classifiers.prompt_task_complexity.CustomHFDeberta.process_logits
```

````

````{py:method} set_autocast(autocast: bool) -> None
:canonical: classifiers.prompt_task_complexity.CustomHFDeberta.set_autocast

```{autodoc2-docstring} classifiers.prompt_task_complexity.CustomHFDeberta.set_autocast
```

````

`````

`````{py:class} MeanPooling()
:canonical: classifiers.prompt_task_complexity.MeanPooling

Bases: {py:obj}`torch.nn.Module`

```{autodoc2-docstring} classifiers.prompt_task_complexity.MeanPooling
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.prompt_task_complexity.MeanPooling.__init__
```

````{py:method} forward(last_hidden_state: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor
:canonical: classifiers.prompt_task_complexity.MeanPooling.forward

```{autodoc2-docstring} classifiers.prompt_task_complexity.MeanPooling.forward
```

````

`````

`````{py:class} MulticlassHead(input_size: int, num_classes: int)
:canonical: classifiers.prompt_task_complexity.MulticlassHead

Bases: {py:obj}`torch.nn.Module`

```{autodoc2-docstring} classifiers.prompt_task_complexity.MulticlassHead
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.prompt_task_complexity.MulticlassHead.__init__
```

````{py:method} forward(x: torch.Tensor) -> torch.Tensor
:canonical: classifiers.prompt_task_complexity.MulticlassHead.forward

```{autodoc2-docstring} classifiers.prompt_task_complexity.MulticlassHead.forward
```

````

`````

````{py:data} PROMPT_TASK_COMPLEXITY_IDENTIFIER
:canonical: classifiers.prompt_task_complexity.PROMPT_TASK_COMPLEXITY_IDENTIFIER
:value: >
   'nvidia/prompt-task-and-complexity-classifier'

```{autodoc2-docstring} classifiers.prompt_task_complexity.PROMPT_TASK_COMPLEXITY_IDENTIFIER
```

````

`````{py:class} PromptTaskComplexityClassifier(batch_size: int = 256, text_field: str = 'text', max_chars: int = 2000, device_type: str = 'cuda', autocast: bool = True, max_mem_gb: int | None = None)
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityClassifier

Bases: {py:obj}`nemo_curator.classifiers.base.DistributedDataClassifier`

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityClassifier.__init__
```

````{py:method} get_labels() -> list[str]
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityClassifier.get_labels

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityClassifier.get_labels
```

````

`````

`````{py:class} PromptTaskComplexityConfig
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityConfig

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityConfig
```

````{py:attribute} base_model
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityConfig.base_model
:type: str
:value: >
   'microsoft/DeBERTa-v3-base'

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityConfig.base_model
```

````

````{py:attribute} max_len
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityConfig.max_len
:type: int
:value: >
   512

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityConfig.max_len
```

````

````{py:attribute} model_output_type
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityConfig.model_output_type
:type: dict
:value: >
   'field(...)'

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityConfig.model_output_type
```

````

`````

`````{py:class} PromptTaskComplexityModel(config: classifiers.prompt_task_complexity.PromptTaskComplexityConfig, autocast: bool, max_mem_gb: int | None)
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityModel

Bases: {py:obj}`crossfit.backend.torch.hf.model.HFModel`

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityModel.__init__
```

````{py:method} load_config() -> transformers.AutoConfig
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityModel.load_config

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityModel.load_config
```

````

````{py:method} load_model(device: str = 'cuda') -> classifiers.prompt_task_complexity.CustomHFDeberta
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityModel.load_model

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityModel.load_model
```

````

````{py:method} load_tokenizer() -> transformers.AutoTokenizer
:canonical: classifiers.prompt_task_complexity.PromptTaskComplexityModel.load_tokenizer

```{autodoc2-docstring} classifiers.prompt_task_complexity.PromptTaskComplexityModel.load_tokenizer
```

````

`````
