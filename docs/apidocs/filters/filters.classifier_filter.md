# {py:mod}`filters.classifier_filter`

```{py:module} filters.classifier_filter
```

```{autodoc2-docstring} filters.classifier_filter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FastTextLangId <filters.classifier_filter.FastTextLangId>`
  - ```{autodoc2-docstring} filters.classifier_filter.FastTextLangId
    :summary:
    ```
* - {py:obj}`FastTextQualityFilter <filters.classifier_filter.FastTextQualityFilter>`
  - ```{autodoc2-docstring} filters.classifier_filter.FastTextQualityFilter
    :summary:
    ```
* - {py:obj}`QualityEstimationFilter <filters.classifier_filter.QualityEstimationFilter>`
  - ```{autodoc2-docstring} filters.classifier_filter.QualityEstimationFilter
    :summary:
    ```
````

### API

`````{py:class} FastTextLangId(model_path: str | None = None, min_langid_score: float = 0.3)
:canonical: filters.classifier_filter.FastTextLangId

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.classifier_filter.FastTextLangId
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.classifier_filter.FastTextLangId.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.classifier_filter.FastTextLangId.keep_document

```{autodoc2-docstring} filters.classifier_filter.FastTextLangId.keep_document
```

````

````{py:method} score_document(df: pandas.Series) -> pandas.Series
:canonical: filters.classifier_filter.FastTextLangId.score_document

```{autodoc2-docstring} filters.classifier_filter.FastTextLangId.score_document
```

````

`````

`````{py:class} FastTextQualityFilter(model_path: str | None = None, label: str = '__label__hq', alpha: float = 3, seed: int = 42)
:canonical: filters.classifier_filter.FastTextQualityFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.classifier_filter.FastTextQualityFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.classifier_filter.FastTextQualityFilter.__init__
```

````{py:method} keep_document(df: pandas.Series) -> pandas.Series
:canonical: filters.classifier_filter.FastTextQualityFilter.keep_document

```{autodoc2-docstring} filters.classifier_filter.FastTextQualityFilter.keep_document
```

````

````{py:method} score_document(df: pandas.Series) -> pandas.Series
:canonical: filters.classifier_filter.FastTextQualityFilter.score_document

```{autodoc2-docstring} filters.classifier_filter.FastTextQualityFilter.score_document
```

````

`````

`````{py:class} QualityEstimationFilter(model_name: str, cutoff: float, mode: str = 'always_en_x', gpu: bool = False, **kwargs)
:canonical: filters.classifier_filter.QualityEstimationFilter

Bases: {py:obj}`nemo_curator.filters.bitext_filter.BitextFilter`

```{autodoc2-docstring} filters.classifier_filter.QualityEstimationFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.classifier_filter.QualityEstimationFilter.__init__
```

````{py:attribute} SUPPORTED_MODELS
:canonical: filters.classifier_filter.QualityEstimationFilter.SUPPORTED_MODELS
:type: typing.Final[dict[str, type[nemo_curator.filters.models.qe_models.QEModel]]]
:value: >
   None

```{autodoc2-docstring} filters.classifier_filter.QualityEstimationFilter.SUPPORTED_MODELS
```

````

````{py:method} keep_bitext(score: float) -> bool
:canonical: filters.classifier_filter.QualityEstimationFilter.keep_bitext

```{autodoc2-docstring} filters.classifier_filter.QualityEstimationFilter.keep_bitext
```

````

````{py:method} score_bitext(src: pandas.Series, tgt: pandas.Series, src_lang: pandas.Series, tgt_lang: pandas.Series) -> pandas.Series
:canonical: filters.classifier_filter.QualityEstimationFilter.score_bitext

```{autodoc2-docstring} filters.classifier_filter.QualityEstimationFilter.score_bitext
```

````

`````
