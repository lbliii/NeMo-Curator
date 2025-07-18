# {py:mod}`datasets.image_text_pair_dataset`

```{py:module} datasets.image_text_pair_dataset
```

```{autodoc2-docstring} datasets.image_text_pair_dataset
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ImageTextPairDataset <datasets.image_text_pair_dataset.ImageTextPairDataset>`
  - ```{autodoc2-docstring} datasets.image_text_pair_dataset.ImageTextPairDataset
    :summary:
    ```
````

### API

`````{py:class} ImageTextPairDataset(path: str, metadata: dask.dataframe.DataFrame, tar_files: list[str], id_col: str)
:canonical: datasets.image_text_pair_dataset.ImageTextPairDataset

```{autodoc2-docstring} datasets.image_text_pair_dataset.ImageTextPairDataset
```

```{rubric} Initialization
```

```{autodoc2-docstring} datasets.image_text_pair_dataset.ImageTextPairDataset.__init__
```

````{py:method} from_webdataset(path: str, id_col: str) -> datasets.image_text_pair_dataset.ImageTextPairDataset
:canonical: datasets.image_text_pair_dataset.ImageTextPairDataset.from_webdataset
:classmethod:

```{autodoc2-docstring} datasets.image_text_pair_dataset.ImageTextPairDataset.from_webdataset
```

````

````{py:method} save_metadata(path: str | None = None, columns: list[str] | None = None) -> None
:canonical: datasets.image_text_pair_dataset.ImageTextPairDataset.save_metadata

```{autodoc2-docstring} datasets.image_text_pair_dataset.ImageTextPairDataset.save_metadata
```

````

````{py:method} to_webdataset(path: str, filter_column: str, samples_per_shard: int = 10000, max_shards: int = 5, old_id_col: str | None = None) -> None
:canonical: datasets.image_text_pair_dataset.ImageTextPairDataset.to_webdataset

```{autodoc2-docstring} datasets.image_text_pair_dataset.ImageTextPairDataset.to_webdataset
```

````

`````
