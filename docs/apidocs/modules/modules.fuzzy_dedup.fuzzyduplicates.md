# {py:mod}`modules.fuzzy_dedup.fuzzyduplicates`

```{py:module} modules.fuzzy_dedup.fuzzyduplicates
```

```{autodoc2-docstring} modules.fuzzy_dedup.fuzzyduplicates
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FuzzyDuplicates <modules.fuzzy_dedup.fuzzyduplicates.FuzzyDuplicates>`
  - ```{autodoc2-docstring} modules.fuzzy_dedup.fuzzyduplicates.FuzzyDuplicates
    :summary:
    ```
````

### API

`````{py:class} FuzzyDuplicates(config: nemo_curator.modules.config.FuzzyDuplicatesConfig, logger: logging.LoggerAdapter | str = './', perform_removal: bool = False)
:canonical: modules.fuzzy_dedup.fuzzyduplicates.FuzzyDuplicates

Bases: {py:obj}`nemo_curator.modules.base.BaseDeduplicationModule`

```{autodoc2-docstring} modules.fuzzy_dedup.fuzzyduplicates.FuzzyDuplicates
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.fuzzy_dedup.fuzzyduplicates.FuzzyDuplicates.__init__
```

````{py:method} identify_duplicates(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset | None
:canonical: modules.fuzzy_dedup.fuzzyduplicates.FuzzyDuplicates.identify_duplicates

```{autodoc2-docstring} modules.fuzzy_dedup.fuzzyduplicates.FuzzyDuplicates.identify_duplicates
```

````

````{py:method} remove(dataset: nemo_curator.datasets.DocumentDataset, duplicates_to_remove: nemo_curator.datasets.DocumentDataset | None) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.fuzzy_dedup.fuzzyduplicates.FuzzyDuplicates.remove

```{autodoc2-docstring} modules.fuzzy_dedup.fuzzyduplicates.FuzzyDuplicates.remove
```

````

`````
