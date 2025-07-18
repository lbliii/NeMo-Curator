# {py:mod}`classifiers.fineweb_edu`

```{py:module} classifiers.fineweb_edu
```

```{autodoc2-docstring} classifiers.fineweb_edu
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FineWebEduClassifier <classifiers.fineweb_edu.FineWebEduClassifier>`
  - ```{autodoc2-docstring} classifiers.fineweb_edu.FineWebEduClassifier
    :summary:
    ```
* - {py:obj}`FineWebMixtralEduClassifier <classifiers.fineweb_edu.FineWebMixtralEduClassifier>`
  - ```{autodoc2-docstring} classifiers.fineweb_edu.FineWebMixtralEduClassifier
    :summary:
    ```
* - {py:obj}`FineWebNemotronEduClassifier <classifiers.fineweb_edu.FineWebNemotronEduClassifier>`
  - ```{autodoc2-docstring} classifiers.fineweb_edu.FineWebNemotronEduClassifier
    :summary:
    ```
* - {py:obj}`FinewebEduModel <classifiers.fineweb_edu.FinewebEduModel>`
  - ```{autodoc2-docstring} classifiers.fineweb_edu.FinewebEduModel
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FINEWEB_EDU_IDENTIFIER <classifiers.fineweb_edu.FINEWEB_EDU_IDENTIFIER>`
  - ```{autodoc2-docstring} classifiers.fineweb_edu.FINEWEB_EDU_IDENTIFIER
    :summary:
    ```
* - {py:obj}`FINEWEB_MIXTRAL_IDENTIFIER <classifiers.fineweb_edu.FINEWEB_MIXTRAL_IDENTIFIER>`
  - ```{autodoc2-docstring} classifiers.fineweb_edu.FINEWEB_MIXTRAL_IDENTIFIER
    :summary:
    ```
* - {py:obj}`FINEWEB_NEMOTRON_IDENTIFIER <classifiers.fineweb_edu.FINEWEB_NEMOTRON_IDENTIFIER>`
  - ```{autodoc2-docstring} classifiers.fineweb_edu.FINEWEB_NEMOTRON_IDENTIFIER
    :summary:
    ```
````

### API

````{py:data} FINEWEB_EDU_IDENTIFIER
:canonical: classifiers.fineweb_edu.FINEWEB_EDU_IDENTIFIER
:value: >
   'HuggingFaceFW/fineweb-edu-classifier'

```{autodoc2-docstring} classifiers.fineweb_edu.FINEWEB_EDU_IDENTIFIER
```

````

````{py:data} FINEWEB_MIXTRAL_IDENTIFIER
:canonical: classifiers.fineweb_edu.FINEWEB_MIXTRAL_IDENTIFIER
:value: >
   'nvidia/nemocurator-fineweb-mixtral-edu-classifier'

```{autodoc2-docstring} classifiers.fineweb_edu.FINEWEB_MIXTRAL_IDENTIFIER
```

````

````{py:data} FINEWEB_NEMOTRON_IDENTIFIER
:canonical: classifiers.fineweb_edu.FINEWEB_NEMOTRON_IDENTIFIER
:value: >
   'nvidia/nemocurator-fineweb-nemotron-4-edu-classifier'

```{autodoc2-docstring} classifiers.fineweb_edu.FINEWEB_NEMOTRON_IDENTIFIER
```

````

````{py:class} FineWebEduClassifier(batch_size: int = 256, text_field: str = 'text', pred_column: str = 'fineweb-edu-score', int_column: str = 'fineweb-edu-score-int', max_chars: int = -1, device_type: str = 'cuda', autocast: bool = True, max_mem_gb: int | None = None)
:canonical: classifiers.fineweb_edu.FineWebEduClassifier

Bases: {py:obj}`classifiers.fineweb_edu._FineWebBaseClassifier`

```{autodoc2-docstring} classifiers.fineweb_edu.FineWebEduClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.fineweb_edu.FineWebEduClassifier.__init__
```

````

````{py:class} FineWebMixtralEduClassifier(batch_size: int = 1024, text_field: str = 'text', pred_column: str = 'fineweb-mixtral-edu-score', int_column: str = 'fineweb-mixtral-edu-score-int', quality_label_column: str = 'fineweb-mixtral-edu-score-label', max_chars: int = -1, device_type: str = 'cuda', autocast: bool = True, max_mem_gb: int | None = None)
:canonical: classifiers.fineweb_edu.FineWebMixtralEduClassifier

Bases: {py:obj}`classifiers.fineweb_edu._FineWebBaseClassifier`

```{autodoc2-docstring} classifiers.fineweb_edu.FineWebMixtralEduClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.fineweb_edu.FineWebMixtralEduClassifier.__init__
```

````

````{py:class} FineWebNemotronEduClassifier(batch_size: int = 1024, text_field: str = 'text', pred_column: str = 'fineweb-nemotron-edu-score', int_column: str = 'fineweb-nemotron-edu-score-int', quality_label_column: str = 'fineweb-nemotron-edu-score-label', max_chars: int = -1, device_type: str = 'cuda', autocast: bool = True, max_mem_gb: int | None = None)
:canonical: classifiers.fineweb_edu.FineWebNemotronEduClassifier

Bases: {py:obj}`classifiers.fineweb_edu._FineWebBaseClassifier`

```{autodoc2-docstring} classifiers.fineweb_edu.FineWebNemotronEduClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.fineweb_edu.FineWebNemotronEduClassifier.__init__
```

````

`````{py:class} FinewebEduModel(path_or_name: str, max_mem_gb: int | None = None, autocast: bool = False)
:canonical: classifiers.fineweb_edu.FinewebEduModel

Bases: {py:obj}`crossfit.backend.torch.hf.model.HFModel`

```{autodoc2-docstring} classifiers.fineweb_edu.FinewebEduModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.fineweb_edu.FinewebEduModel.__init__
```

````{py:method} configure_forward(model: torch.nn.Module, autocast: bool = True) -> torch.nn.Module
:canonical: classifiers.fineweb_edu.FinewebEduModel.configure_forward
:staticmethod:

```{autodoc2-docstring} classifiers.fineweb_edu.FinewebEduModel.configure_forward
```

````

````{py:method} load_config() -> transformers.AutoConfig
:canonical: classifiers.fineweb_edu.FinewebEduModel.load_config

```{autodoc2-docstring} classifiers.fineweb_edu.FinewebEduModel.load_config
```

````

````{py:method} load_model(device: str = 'cuda') -> torch.nn.Module
:canonical: classifiers.fineweb_edu.FinewebEduModel.load_model

```{autodoc2-docstring} classifiers.fineweb_edu.FinewebEduModel.load_model
```

````

````{py:method} load_tokenizer() -> transformers.AutoTokenizer
:canonical: classifiers.fineweb_edu.FinewebEduModel.load_tokenizer

```{autodoc2-docstring} classifiers.fineweb_edu.FinewebEduModel.load_tokenizer
```

````

`````
