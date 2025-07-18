# {py:mod}`modules.fuzzy_dedup.connectedcomponents`

```{py:module} modules.fuzzy_dedup.connectedcomponents
```

```{autodoc2-docstring} modules.fuzzy_dedup.connectedcomponents
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ConnectedComponents <modules.fuzzy_dedup.connectedcomponents.ConnectedComponents>`
  - ```{autodoc2-docstring} modules.fuzzy_dedup.connectedcomponents.ConnectedComponents
    :summary:
    ```
````

### API

`````{py:class} ConnectedComponents(cache_dir: str, jaccard_pairs_path: str, id_column: str = 'id', jaccard_threshold: float = 0.8, logger: logging.LoggerAdapter | str = './', profile_dir: str | None = None)
:canonical: modules.fuzzy_dedup.connectedcomponents.ConnectedComponents

```{autodoc2-docstring} modules.fuzzy_dedup.connectedcomponents.ConnectedComponents
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.fuzzy_dedup.connectedcomponents.ConnectedComponents.__init__
```

````{py:method} cc_workflow(output_path: str) -> None
:canonical: modules.fuzzy_dedup.connectedcomponents.ConnectedComponents.cc_workflow

```{autodoc2-docstring} modules.fuzzy_dedup.connectedcomponents.ConnectedComponents.cc_workflow
```

````

````{py:method} thresholding(df: cudf.DataFrame, threshold: float, column_to_threshold: str) -> cudf.DataFrame
:canonical: modules.fuzzy_dedup.connectedcomponents.ConnectedComponents.thresholding
:staticmethod:

```{autodoc2-docstring} modules.fuzzy_dedup.connectedcomponents.ConnectedComponents.thresholding
```

````

`````
