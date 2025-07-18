# {py:mod}`pii.algorithm`

```{py:module} pii.algorithm
```

```{autodoc2-docstring} pii.algorithm
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PiiDeidentifier <pii.algorithm.PiiDeidentifier>`
  - ```{autodoc2-docstring} pii.algorithm.PiiDeidentifier
    :summary:
    ```
````

### API

`````{py:class} PiiDeidentifier(language: str = DEFAULT_LANGUAGE, supported_entities: list[str] | None = None, anonymize_action: str = 'replace', **kwargs)
:canonical: pii.algorithm.PiiDeidentifier

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.__init__
```

````{py:method} add_custom_operator(entity: str, operator: presidio_anonymizer.entities.OperatorConfig) -> None
:canonical: pii.algorithm.PiiDeidentifier.add_custom_operator

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.add_custom_operator
```

````

````{py:method} add_custom_recognizer(recognizer: presidio_analyzer.EntityRecognizer) -> None
:canonical: pii.algorithm.PiiDeidentifier.add_custom_recognizer

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.add_custom_recognizer
```

````

````{py:method} analyze_text(text: str, entities: list[str] | None = None, language: str = 'en') -> list[list[presidio_analyzer.RecognizerResult]]
:canonical: pii.algorithm.PiiDeidentifier.analyze_text

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.analyze_text
```

````

````{py:method} analyze_text_batch(texts: list[str], entities: list[str] | None = None, language: str = 'en', batch_size: int = 32) -> list[list[presidio_analyzer.RecognizerResult]]
:canonical: pii.algorithm.PiiDeidentifier.analyze_text_batch

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.analyze_text_batch
```

````

````{py:method} deidentify_text(text: str) -> str
:canonical: pii.algorithm.PiiDeidentifier.deidentify_text

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.deidentify_text
```

````

````{py:method} deidentify_text_batch(texts: list[str], batch_size: int = 32) -> list[str]
:canonical: pii.algorithm.PiiDeidentifier.deidentify_text_batch

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.deidentify_text_batch
```

````

````{py:method} from_config(config: collections.abc.Mapping[str, Any]) -> pii.algorithm.PiiDeidentifier
:canonical: pii.algorithm.PiiDeidentifier.from_config
:staticmethod:

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.from_config
```

````

````{py:method} from_default_config() -> pii.algorithm.PiiDeidentifier
:canonical: pii.algorithm.PiiDeidentifier.from_default_config
:staticmethod:

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.from_default_config
```

````

````{py:method} from_yaml_file(path: pathlib.Path | str) -> pii.algorithm.PiiDeidentifier
:canonical: pii.algorithm.PiiDeidentifier.from_yaml_file
:staticmethod:

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.from_yaml_file
```

````

````{py:method} list_operators() -> dict[str, presidio_anonymizer.entities.OperatorConfig]
:canonical: pii.algorithm.PiiDeidentifier.list_operators

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.list_operators
```

````

````{py:method} list_supported_entities() -> list[str]
:canonical: pii.algorithm.PiiDeidentifier.list_supported_entities

```{autodoc2-docstring} pii.algorithm.PiiDeidentifier.list_supported_entities
```

````

`````
