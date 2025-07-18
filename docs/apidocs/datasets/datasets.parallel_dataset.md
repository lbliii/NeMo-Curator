# {py:mod}`datasets.parallel_dataset`

```{py:module} datasets.parallel_dataset
```

```{autodoc2-docstring} datasets.parallel_dataset
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ParallelDataset <datasets.parallel_dataset.ParallelDataset>`
  - ```{autodoc2-docstring} datasets.parallel_dataset.ParallelDataset
    :summary:
    ```
````

### API

`````{py:class} ParallelDataset(dataset_df: dask.dataframe.DataFrame)
:canonical: datasets.parallel_dataset.ParallelDataset

Bases: {py:obj}`nemo_curator.datasets.doc_dataset.DocumentDataset`

```{autodoc2-docstring} datasets.parallel_dataset.ParallelDataset
```

```{rubric} Initialization
```

```{autodoc2-docstring} datasets.parallel_dataset.ParallelDataset.__init__
```

````{py:method} persist() -> datasets.parallel_dataset.ParallelDataset
:canonical: datasets.parallel_dataset.ParallelDataset.persist

```{autodoc2-docstring} datasets.parallel_dataset.ParallelDataset.persist
```

````

````{py:method} read_simple_bitext(src_input_files: str | list[str], tgt_input_files: str | list[str], src_lang: str, tgt_lang: str, backend: str = 'pandas', add_filename: bool | str = False, npartitions: int = 16) -> datasets.parallel_dataset.ParallelDataset
:canonical: datasets.parallel_dataset.ParallelDataset.read_simple_bitext
:classmethod:

```{autodoc2-docstring} datasets.parallel_dataset.ParallelDataset.read_simple_bitext
```

````

````{py:method} read_single_simple_bitext_file_pair(input_file_pair: tuple[str], src_lang: str, tgt_lang: str, doc_id: str | None = None, backend: str = 'cudf', add_filename: bool | str = False) -> Union[dask.dataframe.DataFrame, dask_cudf.DataFrame]
:canonical: datasets.parallel_dataset.ParallelDataset.read_single_simple_bitext_file_pair
:staticmethod:

```{autodoc2-docstring} datasets.parallel_dataset.ParallelDataset.read_single_simple_bitext_file_pair
```

````

````{py:method} to_bitext(output_file_dir: str, write_to_filename: bool | str = False) -> None
:canonical: datasets.parallel_dataset.ParallelDataset.to_bitext

```{autodoc2-docstring} datasets.parallel_dataset.ParallelDataset.to_bitext
```

````

`````
