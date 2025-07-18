# {py:mod}`datasets.doc_dataset`

```{py:module} datasets.doc_dataset
```

```{autodoc2-docstring} datasets.doc_dataset
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DocumentDataset <datasets.doc_dataset.DocumentDataset>`
  - ```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset
    :summary:
    ```
````

### API

`````{py:class} DocumentDataset(dataset_df: dask.dataframe.DataFrame)
:canonical: datasets.doc_dataset.DocumentDataset

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset
```

```{rubric} Initialization
```

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.__init__
```

````{py:method} from_pandas(data: pandas.DataFrame, npartitions: int | None = 1, chunksize: int | None = None, sort: bool | None = True, name: str | None = None) -> datasets.doc_dataset.DocumentDataset
:canonical: datasets.doc_dataset.DocumentDataset.from_pandas
:classmethod:

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.from_pandas
```

````

````{py:method} head(n: int = 5) -> Union[datasets.doc_dataset.cudf, pandas.DataFrame]
:canonical: datasets.doc_dataset.DocumentDataset.head

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.head
```

````

````{py:method} persist() -> datasets.doc_dataset.DocumentDataset
:canonical: datasets.doc_dataset.DocumentDataset.persist

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.persist
```

````

````{py:method} read_custom(input_files: str | list[str], file_type: str, read_func_single_partition: collections.abc.Callable[[list[str], str, bool, str | dict, dict], Union[datasets.doc_dataset.cudf, pandas.DataFrame]], files_per_partition: int | None = None, backend: typing.Literal[pandas, datasets.doc_dataset.cudf] | None = None, add_filename: bool | str = False, columns: list[str] | None = None, input_meta: str | dict | None = None, **kwargs) -> datasets.doc_dataset.DocumentDataset
:canonical: datasets.doc_dataset.DocumentDataset.read_custom
:classmethod:

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.read_custom
```

````

````{py:method} read_json(input_files: str | list[str], backend: typing.Literal[pandas, datasets.doc_dataset.cudf] = 'pandas', files_per_partition: int | None = None, blocksize: str | None = '1gb', add_filename: bool | str = False, input_meta: str | dict | None = None, columns: list[str] | None = None, **kwargs) -> datasets.doc_dataset.DocumentDataset
:canonical: datasets.doc_dataset.DocumentDataset.read_json
:classmethod:

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.read_json
```

````

````{py:method} read_parquet(input_files: str | list[str], backend: typing.Literal[pandas, datasets.doc_dataset.cudf] = 'pandas', files_per_partition: int | None = None, blocksize: str | None = '1gb', add_filename: bool | str = False, columns: list[str] | None = None, **kwargs) -> datasets.doc_dataset.DocumentDataset
:canonical: datasets.doc_dataset.DocumentDataset.read_parquet
:classmethod:

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.read_parquet
```

````

````{py:method} read_pickle(input_files: str | list[str], backend: typing.Literal[pandas, datasets.doc_dataset.cudf] = 'pandas', columns: list[str] | None = None, **kwargs) -> datasets.doc_dataset.DocumentDataset
:canonical: datasets.doc_dataset.DocumentDataset.read_pickle
:classmethod:

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.read_pickle
```

````

````{py:method} repartition(*args, **kwargs) -> datasets.doc_dataset.DocumentDataset
:canonical: datasets.doc_dataset.DocumentDataset.repartition

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.repartition
```

````

````{py:method} to_json(output_path: str, write_to_filename: bool | str = False, keep_filename_column: bool = False, partition_on: str | None = None, compression: str | None = None) -> None
:canonical: datasets.doc_dataset.DocumentDataset.to_json

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.to_json
```

````

````{py:method} to_pandas() -> pandas.DataFrame
:canonical: datasets.doc_dataset.DocumentDataset.to_pandas

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.to_pandas
```

````

````{py:method} to_parquet(output_path: str, write_to_filename: bool | str = False, keep_filename_column: bool = False, partition_on: str | None = None) -> None
:canonical: datasets.doc_dataset.DocumentDataset.to_parquet

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.to_parquet
```

````

````{py:method} to_pickle(output_path: str, write_to_filename: bool | str = False) -> None
:canonical: datasets.doc_dataset.DocumentDataset.to_pickle

```{autodoc2-docstring} datasets.doc_dataset.DocumentDataset.to_pickle
```

````

`````
