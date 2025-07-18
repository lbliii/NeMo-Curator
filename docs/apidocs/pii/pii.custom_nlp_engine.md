# {py:mod}`pii.custom_nlp_engine`

```{py:module} pii.custom_nlp_engine
```

```{autodoc2-docstring} pii.custom_nlp_engine
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CustomNlpEngine <pii.custom_nlp_engine.CustomNlpEngine>`
  - ```{autodoc2-docstring} pii.custom_nlp_engine.CustomNlpEngine
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <pii.custom_nlp_engine.logger>`
  - ```{autodoc2-docstring} pii.custom_nlp_engine.logger
    :summary:
    ```
````

### API

`````{py:class} CustomNlpEngine(models: list[dict[str, str]] | None = None, ner_model_configuration: presidio_analyzer.nlp_engine.NerModelConfiguration | None = None)
:canonical: pii.custom_nlp_engine.CustomNlpEngine

Bases: {py:obj}`presidio_analyzer.nlp_engine.SpacyNlpEngine`

```{autodoc2-docstring} pii.custom_nlp_engine.CustomNlpEngine
```

```{rubric} Initialization
```

```{autodoc2-docstring} pii.custom_nlp_engine.CustomNlpEngine.__init__
```

````{py:method} load() -> None
:canonical: pii.custom_nlp_engine.CustomNlpEngine.load

```{autodoc2-docstring} pii.custom_nlp_engine.CustomNlpEngine.load
```

````

````{py:method} process_batch(texts: list[str] | list[tuple[str, object]], language: str, as_tuples: bool = False, batch_size: int = 32) -> collections.abc.Iterator[presidio_analyzer.nlp_engine.NlpArtifacts | None]
:canonical: pii.custom_nlp_engine.CustomNlpEngine.process_batch

```{autodoc2-docstring} pii.custom_nlp_engine.CustomNlpEngine.process_batch
```

````

`````

````{py:data} logger
:canonical: pii.custom_nlp_engine.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} pii.custom_nlp_engine.logger
```

````
