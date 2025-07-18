# {py:mod}`classifiers.domain`

```{py:module} classifiers.domain
```

```{autodoc2-docstring} classifiers.domain
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DomainClassifier <classifiers.domain.DomainClassifier>`
  - ```{autodoc2-docstring} classifiers.domain.DomainClassifier
    :summary:
    ```
* - {py:obj}`DomainModel <classifiers.domain.DomainModel>`
  - ```{autodoc2-docstring} classifiers.domain.DomainModel
    :summary:
    ```
* - {py:obj}`DomainModelConfig <classifiers.domain.DomainModelConfig>`
  - ```{autodoc2-docstring} classifiers.domain.DomainModelConfig
    :summary:
    ```
* - {py:obj}`MultilingualDomainClassifier <classifiers.domain.MultilingualDomainClassifier>`
  - ```{autodoc2-docstring} classifiers.domain.MultilingualDomainClassifier
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DOMAIN_BASE_MODEL <classifiers.domain.DOMAIN_BASE_MODEL>`
  - ```{autodoc2-docstring} classifiers.domain.DOMAIN_BASE_MODEL
    :summary:
    ```
* - {py:obj}`DOMAIN_IDENTIFIER <classifiers.domain.DOMAIN_IDENTIFIER>`
  - ```{autodoc2-docstring} classifiers.domain.DOMAIN_IDENTIFIER
    :summary:
    ```
* - {py:obj}`MULTILINGUAL_DOMAIN_BASE_MODEL <classifiers.domain.MULTILINGUAL_DOMAIN_BASE_MODEL>`
  - ```{autodoc2-docstring} classifiers.domain.MULTILINGUAL_DOMAIN_BASE_MODEL
    :summary:
    ```
* - {py:obj}`MULTILINGUAL_DOMAIN_IDENTIFIER <classifiers.domain.MULTILINGUAL_DOMAIN_IDENTIFIER>`
  - ```{autodoc2-docstring} classifiers.domain.MULTILINGUAL_DOMAIN_IDENTIFIER
    :summary:
    ```
````

### API

````{py:data} DOMAIN_BASE_MODEL
:canonical: classifiers.domain.DOMAIN_BASE_MODEL
:value: >
   'microsoft/deberta-v3-base'

```{autodoc2-docstring} classifiers.domain.DOMAIN_BASE_MODEL
```

````

````{py:data} DOMAIN_IDENTIFIER
:canonical: classifiers.domain.DOMAIN_IDENTIFIER
:value: >
   'nvidia/domain-classifier'

```{autodoc2-docstring} classifiers.domain.DOMAIN_IDENTIFIER
```

````

````{py:class} DomainClassifier(filter_by: list[str] | None = None, batch_size: int = 256, text_field: str = 'text', pred_column: str = 'domain_pred', prob_column: str | None = None, max_chars: int = 2000, device_type: str = 'cuda', autocast: bool = True, max_mem_gb: int | None = None)
:canonical: classifiers.domain.DomainClassifier

Bases: {py:obj}`classifiers.domain._DomainClassifier`

```{autodoc2-docstring} classifiers.domain.DomainClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.domain.DomainClassifier.__init__
```

````

`````{py:class} DomainModel(config: classifiers.domain.DomainModelConfig, autocast: bool = False, max_mem_gb: int | None = None)
:canonical: classifiers.domain.DomainModel

Bases: {py:obj}`crossfit.backend.torch.hf.model.HFModel`

```{autodoc2-docstring} classifiers.domain.DomainModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.domain.DomainModel.__init__
```

````{py:method} load_config() -> transformers.AutoConfig
:canonical: classifiers.domain.DomainModel.load_config

```{autodoc2-docstring} classifiers.domain.DomainModel.load_config
```

````

````{py:method} load_model(device: str = 'cuda') -> nemo_curator.classifiers.base.HFDeberta
:canonical: classifiers.domain.DomainModel.load_model

```{autodoc2-docstring} classifiers.domain.DomainModel.load_model
```

````

````{py:method} load_tokenizer() -> transformers.AutoTokenizer
:canonical: classifiers.domain.DomainModel.load_tokenizer

```{autodoc2-docstring} classifiers.domain.DomainModel.load_tokenizer
```

````

`````

`````{py:class} DomainModelConfig
:canonical: classifiers.domain.DomainModelConfig

```{autodoc2-docstring} classifiers.domain.DomainModelConfig
```

````{py:attribute} base_model
:canonical: classifiers.domain.DomainModelConfig.base_model
:type: str
:value: >
   None

```{autodoc2-docstring} classifiers.domain.DomainModelConfig.base_model
```

````

````{py:attribute} fc_dropout
:canonical: classifiers.domain.DomainModelConfig.fc_dropout
:type: float
:value: >
   0.2

```{autodoc2-docstring} classifiers.domain.DomainModelConfig.fc_dropout
```

````

````{py:attribute} identifier
:canonical: classifiers.domain.DomainModelConfig.identifier
:type: str
:value: >
   None

```{autodoc2-docstring} classifiers.domain.DomainModelConfig.identifier
```

````

````{py:attribute} max_len
:canonical: classifiers.domain.DomainModelConfig.max_len
:type: int
:value: >
   512

```{autodoc2-docstring} classifiers.domain.DomainModelConfig.max_len
```

````

`````

````{py:data} MULTILINGUAL_DOMAIN_BASE_MODEL
:canonical: classifiers.domain.MULTILINGUAL_DOMAIN_BASE_MODEL
:value: >
   'microsoft/mdeberta-v3-base'

```{autodoc2-docstring} classifiers.domain.MULTILINGUAL_DOMAIN_BASE_MODEL
```

````

````{py:data} MULTILINGUAL_DOMAIN_IDENTIFIER
:canonical: classifiers.domain.MULTILINGUAL_DOMAIN_IDENTIFIER
:value: >
   'nvidia/multilingual-domain-classifier'

```{autodoc2-docstring} classifiers.domain.MULTILINGUAL_DOMAIN_IDENTIFIER
```

````

````{py:class} MultilingualDomainClassifier(filter_by: list[str] | None = None, batch_size: int = 256, text_field: str = 'text', pred_column: str = 'domain_pred', prob_column: str | None = None, max_chars: int = 2000, device_type: str = 'cuda', autocast: bool = True, max_mem_gb: int | None = None)
:canonical: classifiers.domain.MultilingualDomainClassifier

Bases: {py:obj}`classifiers.domain._DomainClassifier`

```{autodoc2-docstring} classifiers.domain.MultilingualDomainClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.domain.MultilingualDomainClassifier.__init__
```

````
