# {py:mod}`utils.fuzzy_dedup_utils.output_map_utils`

```{py:module} utils.fuzzy_dedup_utils.output_map_utils
```

```{autodoc2-docstring} utils.fuzzy_dedup_utils.output_map_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`build_partition <utils.fuzzy_dedup_utils.output_map_utils.build_partition>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.output_map_utils.build_partition
    :summary:
    ```
* - {py:obj}`get_agg_text_bytes_df <utils.fuzzy_dedup_utils.output_map_utils.get_agg_text_bytes_df>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.output_map_utils.get_agg_text_bytes_df
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`dask_cudf <utils.fuzzy_dedup_utils.output_map_utils.dask_cudf>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.output_map_utils.dask_cudf
    :summary:
    ```
````

### API

````{py:function} build_partition(sizes: numpy.ndarray, max_size: int) -> numpy.ndarray
:canonical: utils.fuzzy_dedup_utils.output_map_utils.build_partition

```{autodoc2-docstring} utils.fuzzy_dedup_utils.output_map_utils.build_partition
```
````

````{py:data} dask_cudf
:canonical: utils.fuzzy_dedup_utils.output_map_utils.dask_cudf
:value: >
   'gpu_only_import(...)'

```{autodoc2-docstring} utils.fuzzy_dedup_utils.output_map_utils.dask_cudf
```

````

````{py:function} get_agg_text_bytes_df(df: utils.fuzzy_dedup_utils.output_map_utils.dask_cudf, agg_column: str, bytes_column: str, n_partitions: int, shuffle: bool = False) -> tuple[utils.fuzzy_dedup_utils.output_map_utils.dask_cudf, int]
:canonical: utils.fuzzy_dedup_utils.output_map_utils.get_agg_text_bytes_df

```{autodoc2-docstring} utils.fuzzy_dedup_utils.output_map_utils.get_agg_text_bytes_df
```
````
