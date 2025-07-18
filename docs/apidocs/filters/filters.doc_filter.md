# {py:mod}`filters.doc_filter`

```{py:module} filters.doc_filter
```

```{autodoc2-docstring} filters.doc_filter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DocumentFilter <filters.doc_filter.DocumentFilter>`
  - ```{autodoc2-docstring} filters.doc_filter.DocumentFilter
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`import_filter <filters.doc_filter.import_filter>`
  - ```{autodoc2-docstring} filters.doc_filter.import_filter
    :summary:
    ```
````

### API

`````{py:class} DocumentFilter()
:canonical: filters.doc_filter.DocumentFilter

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} filters.doc_filter.DocumentFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.doc_filter.DocumentFilter.__init__
```

````{py:property} backend
:canonical: filters.doc_filter.DocumentFilter.backend
:type: typing.Literal[pandas, cudf, any]

```{autodoc2-docstring} filters.doc_filter.DocumentFilter.backend
```

````

````{py:method} keep_document(scores: float | list[int | float]) -> bool
:canonical: filters.doc_filter.DocumentFilter.keep_document
:abstractmethod:

```{autodoc2-docstring} filters.doc_filter.DocumentFilter.keep_document
```

````

````{py:property} name
:canonical: filters.doc_filter.DocumentFilter.name
:type: str

```{autodoc2-docstring} filters.doc_filter.DocumentFilter.name
```

````

````{py:property} ngrams
:canonical: filters.doc_filter.DocumentFilter.ngrams
:type: dict

```{autodoc2-docstring} filters.doc_filter.DocumentFilter.ngrams
```

````

````{py:property} paragraphs
:canonical: filters.doc_filter.DocumentFilter.paragraphs
:type: list

```{autodoc2-docstring} filters.doc_filter.DocumentFilter.paragraphs
```

````

````{py:method} score_document(text: str) -> float | list[int | float]
:canonical: filters.doc_filter.DocumentFilter.score_document
:abstractmethod:

```{autodoc2-docstring} filters.doc_filter.DocumentFilter.score_document
```

````

````{py:property} sentences
:canonical: filters.doc_filter.DocumentFilter.sentences
:type: list

```{autodoc2-docstring} filters.doc_filter.DocumentFilter.sentences
```

````

`````

````{py:function} import_filter(filter_path: str) -> filters.doc_filter.DocumentFilter | nemo_curator.filters.bitext_filter.BitextFilter
:canonical: filters.doc_filter.import_filter

```{autodoc2-docstring} filters.doc_filter.import_filter
```
````
