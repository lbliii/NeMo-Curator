# {py:mod}`utils.fuzzy_dedup_utils.io_utils`

```{py:module} utils.fuzzy_dedup_utils.io_utils
```

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`aggregated_anchor_docs_with_bk_read <utils.fuzzy_dedup_utils.io_utils.aggregated_anchor_docs_with_bk_read>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.aggregated_anchor_docs_with_bk_read
    :summary:
    ```
* - {py:obj}`check_empty_buckets <utils.fuzzy_dedup_utils.io_utils.check_empty_buckets>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.check_empty_buckets
    :summary:
    ```
* - {py:obj}`chunk_files <utils.fuzzy_dedup_utils.io_utils.chunk_files>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.chunk_files
    :summary:
    ```
* - {py:obj}`get_bucket_ddf_from_parquet_path <utils.fuzzy_dedup_utils.io_utils.get_bucket_ddf_from_parquet_path>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_bucket_ddf_from_parquet_path
    :summary:
    ```
* - {py:obj}`get_file_size <utils.fuzzy_dedup_utils.io_utils.get_file_size>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_file_size
    :summary:
    ```
* - {py:obj}`get_frag_size <utils.fuzzy_dedup_utils.io_utils.get_frag_size>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_frag_size
    :summary:
    ```
* - {py:obj}`get_restart_offsets <utils.fuzzy_dedup_utils.io_utils.get_restart_offsets>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_restart_offsets
    :summary:
    ```
* - {py:obj}`get_text_ddf_from_json_path_with_blocksize <utils.fuzzy_dedup_utils.io_utils.get_text_ddf_from_json_path_with_blocksize>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_text_ddf_from_json_path_with_blocksize
    :summary:
    ```
* - {py:obj}`strip_trailing_sep <utils.fuzzy_dedup_utils.io_utils.strip_trailing_sep>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.strip_trailing_sep
    :summary:
    ```
* - {py:obj}`update_restart_offsets <utils.fuzzy_dedup_utils.io_utils.update_restart_offsets>`
  - ```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.update_restart_offsets
    :summary:
    ```
````

### API

````{py:function} aggregated_anchor_docs_with_bk_read(path: str, blocksize: int) -> dask.dataframe.DataFrame
:canonical: utils.fuzzy_dedup_utils.io_utils.aggregated_anchor_docs_with_bk_read

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.aggregated_anchor_docs_with_bk_read
```
````

````{py:function} check_empty_buckets(bucket_path: str) -> bool
:canonical: utils.fuzzy_dedup_utils.io_utils.check_empty_buckets

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.check_empty_buckets
```
````

````{py:function} chunk_files(file_list: list[str | pyarrow.dataset.Fragment], max_size_mb: int) -> list[list[str]]
:canonical: utils.fuzzy_dedup_utils.io_utils.chunk_files

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.chunk_files
```
````

````{py:function} get_bucket_ddf_from_parquet_path(input_bucket_path: str, num_workers: int) -> dask.dataframe.DataFrame
:canonical: utils.fuzzy_dedup_utils.io_utils.get_bucket_ddf_from_parquet_path

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_bucket_ddf_from_parquet_path
```
````

````{py:function} get_file_size(file_path: str) -> int
:canonical: utils.fuzzy_dedup_utils.io_utils.get_file_size

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_file_size
```
````

````{py:function} get_frag_size(frag: pyarrow.dataset.Fragment) -> int
:canonical: utils.fuzzy_dedup_utils.io_utils.get_frag_size

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_frag_size
```
````

````{py:function} get_restart_offsets(output_path: str) -> tuple[int, int]
:canonical: utils.fuzzy_dedup_utils.io_utils.get_restart_offsets

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_restart_offsets
```
````

````{py:function} get_text_ddf_from_json_path_with_blocksize(input_data_paths: list[str], num_files: int, blocksize: int, id_column: str, text_column: str, input_meta: dict[str, str] | None = None) -> dask.dataframe.DataFrame
:canonical: utils.fuzzy_dedup_utils.io_utils.get_text_ddf_from_json_path_with_blocksize

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.get_text_ddf_from_json_path_with_blocksize
```
````

````{py:function} strip_trailing_sep(path: str) -> str
:canonical: utils.fuzzy_dedup_utils.io_utils.strip_trailing_sep

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.strip_trailing_sep
```
````

````{py:function} update_restart_offsets(output_path: str, bucket_offset: int, text_offset: int) -> None
:canonical: utils.fuzzy_dedup_utils.io_utils.update_restart_offsets

```{autodoc2-docstring} utils.fuzzy_dedup_utils.io_utils.update_restart_offsets
```
````
