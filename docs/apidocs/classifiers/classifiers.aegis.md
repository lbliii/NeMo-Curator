# {py:mod}`classifiers.aegis`

```{py:module} classifiers.aegis
```

```{autodoc2-docstring} classifiers.aegis
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AegisClassifier <classifiers.aegis.AegisClassifier>`
  - ```{autodoc2-docstring} classifiers.aegis.AegisClassifier
    :summary:
    ```
* - {py:obj}`AegisConfig <classifiers.aegis.AegisConfig>`
  - ```{autodoc2-docstring} classifiers.aegis.AegisConfig
    :summary:
    ```
* - {py:obj}`AegisHFModel <classifiers.aegis.AegisHFModel>`
  - ```{autodoc2-docstring} classifiers.aegis.AegisHFModel
    :summary:
    ```
* - {py:obj}`AegisModel <classifiers.aegis.AegisModel>`
  - ```{autodoc2-docstring} classifiers.aegis.AegisModel
    :summary:
    ```
* - {py:obj}`InstructionDataGuardClassifier <classifiers.aegis.InstructionDataGuardClassifier>`
  - ```{autodoc2-docstring} classifiers.aegis.InstructionDataGuardClassifier
    :summary:
    ```
* - {py:obj}`InstructionDataGuardNet <classifiers.aegis.InstructionDataGuardNet>`
  - ```{autodoc2-docstring} classifiers.aegis.InstructionDataGuardNet
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ACCESS_ERROR_MESSAGE <classifiers.aegis.ACCESS_ERROR_MESSAGE>`
  - ```{autodoc2-docstring} classifiers.aegis.ACCESS_ERROR_MESSAGE
    :summary:
    ```
* - {py:obj}`AEGIS_LABELS <classifiers.aegis.AEGIS_LABELS>`
  - ```{autodoc2-docstring} classifiers.aegis.AEGIS_LABELS
    :summary:
    ```
````

### API

````{py:data} ACCESS_ERROR_MESSAGE
:canonical: classifiers.aegis.ACCESS_ERROR_MESSAGE
:value: <Multiline-String>

```{autodoc2-docstring} classifiers.aegis.ACCESS_ERROR_MESSAGE
```

````

````{py:data} AEGIS_LABELS
:canonical: classifiers.aegis.AEGIS_LABELS
:value: >
   ['unknown', 'safe', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10', 'O11', 'O12', 'O13'...

```{autodoc2-docstring} classifiers.aegis.AEGIS_LABELS
```

````

````{py:class} AegisClassifier(aegis_variant: str = 'nvidia/Aegis-AI-Content-Safety-LlamaGuard-Defensive-1.0', token: str | bool | None = None, filter_by: list[str] | None = None, batch_size: int = 64, text_field: str = 'text', pred_column: str = 'aegis_pred', raw_pred_column: str = '_aegis_raw_pred', keep_raw_pred: bool = False, max_chars: int = 6000, device_type: str = 'cuda', autocast: bool = True, max_mem_gb: int | None = None)
:canonical: classifiers.aegis.AegisClassifier

Bases: {py:obj}`nemo_curator.classifiers.base.DistributedDataClassifier`

```{autodoc2-docstring} classifiers.aegis.AegisClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.aegis.AegisClassifier.__init__
```

````

`````{py:class} AegisConfig
:canonical: classifiers.aegis.AegisConfig

```{autodoc2-docstring} classifiers.aegis.AegisConfig
```

````{py:attribute} add_instruction_data_guard
:canonical: classifiers.aegis.AegisConfig.add_instruction_data_guard
:type: bool
:value: >
   False

```{autodoc2-docstring} classifiers.aegis.AegisConfig.add_instruction_data_guard
```

````

````{py:attribute} dtype
:canonical: classifiers.aegis.AegisConfig.dtype
:type: torch.dtype
:value: >
   None

```{autodoc2-docstring} classifiers.aegis.AegisConfig.dtype
```

````

````{py:attribute} instruction_data_guard_path
:canonical: classifiers.aegis.AegisConfig.instruction_data_guard_path
:type: str
:value: >
   'nvidia/instruction-data-guard'

```{autodoc2-docstring} classifiers.aegis.AegisConfig.instruction_data_guard_path
```

````

````{py:attribute} max_length
:canonical: classifiers.aegis.AegisConfig.max_length
:type: int
:value: >
   4096

```{autodoc2-docstring} classifiers.aegis.AegisConfig.max_length
```

````

````{py:attribute} peft_model_name_or_path
:canonical: classifiers.aegis.AegisConfig.peft_model_name_or_path
:type: str
:value: >
   None

```{autodoc2-docstring} classifiers.aegis.AegisConfig.peft_model_name_or_path
```

````

````{py:attribute} pretrained_model_name_or_path
:canonical: classifiers.aegis.AegisConfig.pretrained_model_name_or_path
:type: str
:value: >
   'meta-llama/LlamaGuard-7b'

```{autodoc2-docstring} classifiers.aegis.AegisConfig.pretrained_model_name_or_path
```

````

````{py:attribute} token
:canonical: classifiers.aegis.AegisConfig.token
:type: str | bool | None
:value: >
   None

```{autodoc2-docstring} classifiers.aegis.AegisConfig.token
```

````

`````

`````{py:class} AegisHFModel(config: classifiers.aegis.AegisConfig, max_mem_gb: int | None = None)
:canonical: classifiers.aegis.AegisHFModel

Bases: {py:obj}`crossfit.backend.torch.hf.model.HFModel`

```{autodoc2-docstring} classifiers.aegis.AegisHFModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.aegis.AegisHFModel.__init__
```

````{py:method} load_cfg() -> transformers.AutoConfig
:canonical: classifiers.aegis.AegisHFModel.load_cfg

```{autodoc2-docstring} classifiers.aegis.AegisHFModel.load_cfg
```

````

````{py:method} load_config() -> transformers.AutoConfig
:canonical: classifiers.aegis.AegisHFModel.load_config

```{autodoc2-docstring} classifiers.aegis.AegisHFModel.load_config
```

````

````{py:method} load_model(device: str = 'cuda') -> classifiers.aegis.AegisModel
:canonical: classifiers.aegis.AegisHFModel.load_model

```{autodoc2-docstring} classifiers.aegis.AegisHFModel.load_model
```

````

````{py:method} load_tokenizer() -> transformers.AutoTokenizer
:canonical: classifiers.aegis.AegisHFModel.load_tokenizer

```{autodoc2-docstring} classifiers.aegis.AegisHFModel.load_tokenizer
```

````

````{py:method} max_seq_length() -> int
:canonical: classifiers.aegis.AegisHFModel.max_seq_length

```{autodoc2-docstring} classifiers.aegis.AegisHFModel.max_seq_length
```

````

`````

`````{py:class} AegisModel(pretrained_model_name_or_path: str, peft_model_name_or_path: str, dtype: torch.dtype, token: str | bool | None, add_instruction_data_guard: bool = False, autocast: bool = False)
:canonical: classifiers.aegis.AegisModel

Bases: {py:obj}`torch.nn.Module`

```{autodoc2-docstring} classifiers.aegis.AegisModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.aegis.AegisModel.__init__
```

````{py:method} forward(batch: dict[str, torch.Tensor]) -> torch.Tensor
:canonical: classifiers.aegis.AegisModel.forward

```{autodoc2-docstring} classifiers.aegis.AegisModel.forward
```

````

`````

````{py:class} InstructionDataGuardClassifier(token: str | bool | None = None, batch_size: int = 64, text_field: str = 'text', pred_column: str = 'is_poisoned', prob_column: str = 'instruction_data_guard_poisoning_score', max_chars: int = 6000, autocast: bool = True, device_type: str = 'cuda', max_mem_gb: int | None = None)
:canonical: classifiers.aegis.InstructionDataGuardClassifier

Bases: {py:obj}`nemo_curator.classifiers.base.DistributedDataClassifier`

```{autodoc2-docstring} classifiers.aegis.InstructionDataGuardClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.aegis.InstructionDataGuardClassifier.__init__
```

````

`````{py:class} InstructionDataGuardNet(input_dim: int, dropout: float = 0.7)
:canonical: classifiers.aegis.InstructionDataGuardNet

Bases: {py:obj}`torch.nn.Module`, {py:obj}`huggingface_hub.PyTorchModelHubMixin`

```{autodoc2-docstring} classifiers.aegis.InstructionDataGuardNet
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.aegis.InstructionDataGuardNet.__init__
```

````{py:method} forward(x: torch.Tensor) -> torch.Tensor
:canonical: classifiers.aegis.InstructionDataGuardNet.forward

```{autodoc2-docstring} classifiers.aegis.InstructionDataGuardNet.forward
```

````

`````
