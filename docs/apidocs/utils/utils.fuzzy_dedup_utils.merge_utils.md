# {py:mod}`utils.fuzzy_dedup_utils.merge_utils`

```{py:module} utils.fuzzy_dedup_utils.merge_utils
```

```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`apply_bk_mapping <utils.fuzzy_dedup_utils.merge_utils.apply_bk_mapping>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.apply_bk_mapping
    :summary:
    ```
* - {py:obj}`blockwise_merge <utils.fuzzy_dedup_utils.merge_utils.blockwise_merge>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.blockwise_merge
    :summary:
    ```
* - {py:obj}`extract_partitioning_index <utils.fuzzy_dedup_utils.merge_utils.extract_partitioning_index>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.extract_partitioning_index
    :summary:
    ```
* - {py:obj}`filter_text_rows_by_bucket_batch <utils.fuzzy_dedup_utils.merge_utils.filter_text_rows_by_bucket_batch>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.filter_text_rows_by_bucket_batch
    :summary:
    ```
* - {py:obj}`merge_left_to_shuffled_right <utils.fuzzy_dedup_utils.merge_utils.merge_left_to_shuffled_right>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.merge_left_to_shuffled_right
    :summary:
    ```
````

### API

````{py:function} apply_bk_mapping(part: Union[utils.fuzzy_dedup_utils.merge_utils.cudf, pandas.DataFrame], bk_map: Union[utils.fuzzy_dedup_utils.merge_utils.cudf, pandas.DataFrame]) -> Union[utils.fuzzy_dedup_utils.merge_utils.cudf, pandas.Series]
:canonical: utils.fuzzy_dedup_utils.merge_utils.apply_bk_mapping

```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.apply_bk_mapping
```
````

````{py:function} blockwise_merge(left: dask.dataframe.DataFrame, right: dask.dataframe.DataFrame, on: str, how: str = 'inner') -> dask.dataframe.DataFrame
:canonical: utils.fuzzy_dedup_utils.merge_utils.blockwise_merge

```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.blockwise_merge
```
````

````{py:function} extract_partitioning_index(left_df: dask.dataframe.DataFrame, merge_on: str, bk_mapping: dask.dataframe.DataFrame, parts_per_bucket_batch: int, total_bucket_partitions: int) -> tuple[dask.dataframe.DataFrame, dask.dataframe.Series]
:canonical: utils.fuzzy_dedup_utils.merge_utils.extract_partitioning_index

```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.extract_partitioning_index
```
````

````{py:function} filter_text_rows_by_bucket_batch(left_df: dask.dataframe.DataFrame, global_partitioning_index: dask.dataframe.Series, bucket_part_offset: int, bucket_part_end_offset: int, total_bucket_partitions: int) -> dask.dataframe.DataFrame
:canonical: utils.fuzzy_dedup_utils.merge_utils.filter_text_rows_by_bucket_batch

```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.filter_text_rows_by_bucket_batch
```
````

````{py:function} merge_left_to_shuffled_right(subset_text_df: dask.dataframe.DataFrame, subset_bucket_df: dask.dataframe.DataFrame, merge_on: str) -> dask.dataframe.DataFrame
:canonical: utils.fuzzy_dedup_utils.merge_utils.merge_left_to_shuffled_right

```{autodoc2-docstring} utils.fuzzy_dedup_utils.merge_utils.merge_left_to_shuffled_right
```
````
