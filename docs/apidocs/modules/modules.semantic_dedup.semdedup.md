# {py:mod}`modules.semantic_dedup.semdedup`

```{py:module} modules.semantic_dedup.semdedup
```

```{autodoc2-docstring} modules.semantic_dedup.semdedup
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SemDedup <modules.semantic_dedup.semdedup.SemDedup>`
  - ```{autodoc2-docstring} modules.semantic_dedup.semdedup.SemDedup
    :summary:
    ```
````

### API

`````{py:class} SemDedup(config: nemo_curator.modules.config.SemDedupConfig, input_column: str = 'text', id_column: str = 'id', perform_removal: bool = False, logger: logging.Logger | str = './')
:canonical: modules.semantic_dedup.semdedup.SemDedup

Bases: {py:obj}`nemo_curator.modules.base.BaseDeduplicationModule`

```{autodoc2-docstring} modules.semantic_dedup.semdedup.SemDedup
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.semantic_dedup.semdedup.SemDedup.__init__
```

````{py:method} identify_duplicates(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.semantic_dedup.semdedup.SemDedup.identify_duplicates

```{autodoc2-docstring} modules.semantic_dedup.semdedup.SemDedup.identify_duplicates
```

````

````{py:method} remove(dataset: nemo_curator.datasets.DocumentDataset, duplicates_to_remove: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.semantic_dedup.semdedup.SemDedup.remove

```{autodoc2-docstring} modules.semantic_dedup.semdedup.SemDedup.remove
```

````

`````
