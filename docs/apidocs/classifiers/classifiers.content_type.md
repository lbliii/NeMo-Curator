# {py:mod}`classifiers.content_type`

```{py:module} classifiers.content_type
```

```{autodoc2-docstring} classifiers.content_type
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ContentTypeClassifier <classifiers.content_type.ContentTypeClassifier>`
  - ```{autodoc2-docstring} classifiers.content_type.ContentTypeClassifier
    :summary:
    ```
* - {py:obj}`ContentTypeModel <classifiers.content_type.ContentTypeModel>`
  - ```{autodoc2-docstring} classifiers.content_type.ContentTypeModel
    :summary:
    ```
* - {py:obj}`ContentTypeModelConfig <classifiers.content_type.ContentTypeModelConfig>`
  - ```{autodoc2-docstring} classifiers.content_type.ContentTypeModelConfig
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CONTENT_TYPE_IDENTIFIER <classifiers.content_type.CONTENT_TYPE_IDENTIFIER>`
  - ```{autodoc2-docstring} classifiers.content_type.CONTENT_TYPE_IDENTIFIER
    :summary:
    ```
````

### API

````{py:data} CONTENT_TYPE_IDENTIFIER
:canonical: classifiers.content_type.CONTENT_TYPE_IDENTIFIER
:value: >
   'nvidia/content-type-classifier-deberta'

```{autodoc2-docstring} classifiers.content_type.CONTENT_TYPE_IDENTIFIER
```

````

````{py:class} ContentTypeClassifier(filter_by: list[str] | None = None, batch_size: int = 256, text_field: str = 'text', pred_column: str = 'content_pred', prob_column: str | None = None, max_chars: int = 5000, device_type: str = 'cuda', autocast: bool = True, max_mem_gb: int | None = None)
:canonical: classifiers.content_type.ContentTypeClassifier

Bases: {py:obj}`nemo_curator.classifiers.base.DistributedDataClassifier`

```{autodoc2-docstring} classifiers.content_type.ContentTypeClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.content_type.ContentTypeClassifier.__init__
```

````

`````{py:class} ContentTypeModel(config: classifiers.content_type.ContentTypeModelConfig, autocast: bool = False, max_mem_gb: int | None = None)
:canonical: classifiers.content_type.ContentTypeModel

Bases: {py:obj}`crossfit.backend.torch.hf.model.HFModel`

```{autodoc2-docstring} classifiers.content_type.ContentTypeModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.content_type.ContentTypeModel.__init__
```

````{py:method} load_config() -> transformers.AutoConfig
:canonical: classifiers.content_type.ContentTypeModel.load_config

```{autodoc2-docstring} classifiers.content_type.ContentTypeModel.load_config
```

````

````{py:method} load_model(device: str = 'cuda') -> nemo_curator.classifiers.base.HFDeberta
:canonical: classifiers.content_type.ContentTypeModel.load_model

```{autodoc2-docstring} classifiers.content_type.ContentTypeModel.load_model
```

````

````{py:method} load_tokenizer() -> transformers.AutoTokenizer
:canonical: classifiers.content_type.ContentTypeModel.load_tokenizer

```{autodoc2-docstring} classifiers.content_type.ContentTypeModel.load_tokenizer
```

````

`````

`````{py:class} ContentTypeModelConfig
:canonical: classifiers.content_type.ContentTypeModelConfig

```{autodoc2-docstring} classifiers.content_type.ContentTypeModelConfig
```

````{py:attribute} fc_dropout
:canonical: classifiers.content_type.ContentTypeModelConfig.fc_dropout
:type: float
:value: >
   0.2

```{autodoc2-docstring} classifiers.content_type.ContentTypeModelConfig.fc_dropout
```

````

````{py:attribute} max_len
:canonical: classifiers.content_type.ContentTypeModelConfig.max_len
:type: int
:value: >
   1024

```{autodoc2-docstring} classifiers.content_type.ContentTypeModelConfig.max_len
```

````

````{py:attribute} model
:canonical: classifiers.content_type.ContentTypeModelConfig.model
:type: str
:value: >
   'microsoft/deberta-v3-base'

```{autodoc2-docstring} classifiers.content_type.ContentTypeModelConfig.model
```

````

`````
