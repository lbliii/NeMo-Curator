# {py:mod}`filters.bitext_filter`

```{py:module} filters.bitext_filter
```

```{autodoc2-docstring} filters.bitext_filter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BitextFilter <filters.bitext_filter.BitextFilter>`
  - ```{autodoc2-docstring} filters.bitext_filter.BitextFilter
    :summary:
    ```
````

### API

`````{py:class} BitextFilter(src_field: str = 'src', tgt_field: str = 'tgt', metadata_fields: list[str] | str | None = None, metadata_field_name_mapping: dict[str, str] | None = None, score_field: str | None = None, score_type: type | str | None = None, invert: bool = False)
:canonical: filters.bitext_filter.BitextFilter

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} filters.bitext_filter.BitextFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.bitext_filter.BitextFilter.__init__
```

````{py:method} keep_bitext(**kwargs) -> bool
:canonical: filters.bitext_filter.BitextFilter.keep_bitext
:abstractmethod:

```{autodoc2-docstring} filters.bitext_filter.BitextFilter.keep_bitext
```

````

````{py:method} score_bitext(src: pandas.Series, tgt: pandas.Series, **kwargs) -> pandas.Series
:canonical: filters.bitext_filter.BitextFilter.score_bitext
:abstractmethod:

```{autodoc2-docstring} filters.bitext_filter.BitextFilter.score_bitext
```

````

`````
