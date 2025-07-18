# {py:mod}`utils.fuzzy_dedup_utils.shuffle_utils`

```{py:module} utils.fuzzy_dedup_utils.shuffle_utils
```

```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_shuffle_part_ids_df <utils.fuzzy_dedup_utils.shuffle_utils.get_shuffle_part_ids_df>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.get_shuffle_part_ids_df
    :summary:
    ```
* - {py:obj}`rearange_by_column_direct <utils.fuzzy_dedup_utils.shuffle_utils.rearange_by_column_direct>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.rearange_by_column_direct
    :summary:
    ```
* - {py:obj}`write_partitioned_file <utils.fuzzy_dedup_utils.shuffle_utils.write_partitioned_file>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.write_partitioned_file
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`USE_EXCOMMS <utils.fuzzy_dedup_utils.shuffle_utils.USE_EXCOMMS>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.USE_EXCOMMS
    :summary:
    ```
* - {py:obj}`dask_cuda_version <utils.fuzzy_dedup_utils.shuffle_utils.dask_cuda_version>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.dask_cuda_version
    :summary:
    ```
````

### API

````{py:data} USE_EXCOMMS
:canonical: utils.fuzzy_dedup_utils.shuffle_utils.USE_EXCOMMS
:value: >
   None

```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.USE_EXCOMMS
```

````

````{py:data} dask_cuda_version
:canonical: utils.fuzzy_dedup_utils.shuffle_utils.dask_cuda_version
:value: >
   'Version(...)'

```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.dask_cuda_version
```

````

````{py:function} get_shuffle_part_ids_df(agg_df: cudf.DataFrame, partition_on: str, output_col: str, size_col: str, num_workers: int = 0) -> cudf.DataFrame
:canonical: utils.fuzzy_dedup_utils.shuffle_utils.get_shuffle_part_ids_df

```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.get_shuffle_part_ids_df
```
````

````{py:function} rearange_by_column_direct(df: cudf.DataFrame, col: str, npartitions: int, ignore_index: bool, excomms_default: bool = USE_EXCOMMS) -> cudf.DataFrame
:canonical: utils.fuzzy_dedup_utils.shuffle_utils.rearange_by_column_direct

```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.rearange_by_column_direct
```
````

````{py:function} write_partitioned_file(df: cudf.DataFrame, output_path: str, partition_on: str, batch_id: int) -> cudf.Series
:canonical: utils.fuzzy_dedup_utils.shuffle_utils.write_partitioned_file

```{autodoc2-docstring} utils.fuzzy_dedup_utils.shuffle_utils.write_partitioned_file
```
````
