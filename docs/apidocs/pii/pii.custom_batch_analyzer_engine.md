# {py:mod}`pii.custom_batch_analyzer_engine`

```{py:module} pii.custom_batch_analyzer_engine
```

```{autodoc2-docstring} pii.custom_batch_analyzer_engine
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CustomBatchAnalyzerEngine <pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine>`
  - ```{autodoc2-docstring} pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <pii.custom_batch_analyzer_engine.logger>`
  - ```{autodoc2-docstring} pii.custom_batch_analyzer_engine.logger
    :summary:
    ```
````

### API

`````{py:class} CustomBatchAnalyzerEngine(analyzer_engine: presidio_analyzer.AnalyzerEngine | None = None)
:canonical: pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine

Bases: {py:obj}`presidio_analyzer.BatchAnalyzerEngine`

```{autodoc2-docstring} pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine
```

```{rubric} Initialization
```

```{autodoc2-docstring} pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine.__init__
```

````{py:method} analyze_batch(texts: collections.abc.Iterable[str], language: str, entities: list[str] | None = None, correlation_id: str | None = None, score_threshold: float | None = None, return_decision_process: bool | None = False, ad_hoc_recognizers: list[presidio_analyzer.EntityRecognizer] | None = None, context: list[str] | None = None, allow_list: list[str] | None = None, nlp_artifacts_batch: collections.abc.Iterable[presidio_analyzer.nlp_engine.NlpArtifacts] | None = None) -> list[list[presidio_analyzer.RecognizerResult]]
:canonical: pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine.analyze_batch

```{autodoc2-docstring} pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine.analyze_batch
```

````

````{py:method} analyze_dict(input_dict: dict[str, Any | collections.abc.Iterable[Any]], language: str, keys_to_skip: list[str] | None = None, **kwargs) -> collections.abc.Iterator[presidio_analyzer.DictAnalyzerResult]
:canonical: pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine.analyze_dict

```{autodoc2-docstring} pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine.analyze_dict
```

````

````{py:method} analyze_iterator(texts: collections.abc.Iterable[str | bool | float | int], language: str, batch_size: int = 32, **kwargs) -> list[list[presidio_analyzer.RecognizerResult]]
:canonical: pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine.analyze_iterator

```{autodoc2-docstring} pii.custom_batch_analyzer_engine.CustomBatchAnalyzerEngine.analyze_iterator
```

````

`````

````{py:data} logger
:canonical: pii.custom_batch_analyzer_engine.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} pii.custom_batch_analyzer_engine.logger
```

````
