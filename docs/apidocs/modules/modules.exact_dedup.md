# {py:mod}`modules.exact_dedup`

```{py:module} modules.exact_dedup
```

```{autodoc2-docstring} modules.exact_dedup
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ExactDuplicates <modules.exact_dedup.ExactDuplicates>`
  - ```{autodoc2-docstring} modules.exact_dedup.ExactDuplicates
    :summary:
    ```
````

### API

`````{py:class} ExactDuplicates(logger: logging.LoggerAdapter | str = './', id_field: str = 'id', text_field: str = 'text', hash_method: str = 'md5', perform_removal: bool = False, profile_dir: str | None = None, cache_dir: str | None = None)
:canonical: modules.exact_dedup.ExactDuplicates

Bases: {py:obj}`nemo_curator.modules.base.BaseDeduplicationModule`

```{autodoc2-docstring} modules.exact_dedup.ExactDuplicates
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.exact_dedup.ExactDuplicates.__init__
```

````{py:attribute} SUPPORTED_HASHES
:canonical: modules.exact_dedup.ExactDuplicates.SUPPORTED_HASHES
:value: >
   'frozenset(...)'

```{autodoc2-docstring} modules.exact_dedup.ExactDuplicates.SUPPORTED_HASHES
```

````

````{py:method} hash_documents(df: cudf.Series | pandas.Series) -> cudf.Series | pandas.Series
:canonical: modules.exact_dedup.ExactDuplicates.hash_documents

```{autodoc2-docstring} modules.exact_dedup.ExactDuplicates.hash_documents
```

````

````{py:method} identify_duplicates(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.exact_dedup.ExactDuplicates.identify_duplicates

```{autodoc2-docstring} modules.exact_dedup.ExactDuplicates.identify_duplicates
```

````

````{py:method} remove(dataset: nemo_curator.datasets.DocumentDataset, duplicates_to_remove: nemo_curator.datasets.DocumentDataset | None) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.exact_dedup.ExactDuplicates.remove

```{autodoc2-docstring} modules.exact_dedup.ExactDuplicates.remove
```

````

`````
