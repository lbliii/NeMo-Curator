# {py:mod}`classifiers.quality`

```{py:module} classifiers.quality
```

```{autodoc2-docstring} classifiers.quality
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`QualityClassifier <classifiers.quality.QualityClassifier>`
  - ```{autodoc2-docstring} classifiers.quality.QualityClassifier
    :summary:
    ```
* - {py:obj}`QualityModel <classifiers.quality.QualityModel>`
  - ```{autodoc2-docstring} classifiers.quality.QualityModel
    :summary:
    ```
* - {py:obj}`QualityModelConfig <classifiers.quality.QualityModelConfig>`
  - ```{autodoc2-docstring} classifiers.quality.QualityModelConfig
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`QUALITY_IDENTIFIER <classifiers.quality.QUALITY_IDENTIFIER>`
  - ```{autodoc2-docstring} classifiers.quality.QUALITY_IDENTIFIER
    :summary:
    ```
````

### API

````{py:data} QUALITY_IDENTIFIER
:canonical: classifiers.quality.QUALITY_IDENTIFIER
:value: >
   'nvidia/quality-classifier-deberta'

```{autodoc2-docstring} classifiers.quality.QUALITY_IDENTIFIER
```

````

````{py:class} QualityClassifier(filter_by: list[str] | None = None, batch_size: int = 256, text_field: str = 'text', pred_column: str = 'quality_pred', prob_column: str = 'quality_prob', max_chars: int = 6000, device_type: str = 'cuda', autocast: bool = True, max_mem_gb: int | None = None)
:canonical: classifiers.quality.QualityClassifier

Bases: {py:obj}`nemo_curator.classifiers.base.DistributedDataClassifier`

```{autodoc2-docstring} classifiers.quality.QualityClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.quality.QualityClassifier.__init__
```

````

`````{py:class} QualityModel(config: classifiers.quality.QualityModelConfig, autocast: bool = False, max_mem_gb: int | None = None)
:canonical: classifiers.quality.QualityModel

Bases: {py:obj}`crossfit.backend.torch.hf.model.HFModel`

```{autodoc2-docstring} classifiers.quality.QualityModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.quality.QualityModel.__init__
```

````{py:method} load_config() -> transformers.AutoConfig
:canonical: classifiers.quality.QualityModel.load_config

```{autodoc2-docstring} classifiers.quality.QualityModel.load_config
```

````

````{py:method} load_model(device: str = 'cuda') -> nemo_curator.classifiers.base.HFDeberta
:canonical: classifiers.quality.QualityModel.load_model

```{autodoc2-docstring} classifiers.quality.QualityModel.load_model
```

````

````{py:method} load_tokenizer() -> transformers.AutoTokenizer
:canonical: classifiers.quality.QualityModel.load_tokenizer

```{autodoc2-docstring} classifiers.quality.QualityModel.load_tokenizer
```

````

`````

`````{py:class} QualityModelConfig
:canonical: classifiers.quality.QualityModelConfig

```{autodoc2-docstring} classifiers.quality.QualityModelConfig
```

````{py:attribute} fc_dropout
:canonical: classifiers.quality.QualityModelConfig.fc_dropout
:type: float
:value: >
   0.2

```{autodoc2-docstring} classifiers.quality.QualityModelConfig.fc_dropout
```

````

````{py:attribute} max_len
:canonical: classifiers.quality.QualityModelConfig.max_len
:type: int
:value: >
   1024

```{autodoc2-docstring} classifiers.quality.QualityModelConfig.max_len
```

````

````{py:attribute} model
:canonical: classifiers.quality.QualityModelConfig.model
:type: str
:value: >
   'microsoft/deberta-v3-base'

```{autodoc2-docstring} classifiers.quality.QualityModelConfig.model
```

````

`````
