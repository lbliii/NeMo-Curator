# {py:mod}`utils.file_utils`

```{py:module} utils.file_utils
```

```{autodoc2-docstring} utils.file_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`expand_outdir_and_mkdir <utils.file_utils.expand_outdir_and_mkdir>`
  - ```{autodoc2-docstring} utils.file_utils.expand_outdir_and_mkdir
    :summary:
    ```
* - {py:obj}`filter_files_by_extension <utils.file_utils.filter_files_by_extension>`
  - ```{autodoc2-docstring} utils.file_utils.filter_files_by_extension
    :summary:
    ```
* - {py:obj}`get_all_files_paths_under <utils.file_utils.get_all_files_paths_under>`
  - ```{autodoc2-docstring} utils.file_utils.get_all_files_paths_under
    :summary:
    ```
* - {py:obj}`get_batched_files <utils.file_utils.get_batched_files>`
  - ```{autodoc2-docstring} utils.file_utils.get_batched_files
    :summary:
    ```
* - {py:obj}`get_remaining_files <utils.file_utils.get_remaining_files>`
  - ```{autodoc2-docstring} utils.file_utils.get_remaining_files
    :summary:
    ```
* - {py:obj}`merge_counts <utils.file_utils.merge_counts>`
  - ```{autodoc2-docstring} utils.file_utils.merge_counts
    :summary:
    ```
* - {py:obj}`mkdir <utils.file_utils.mkdir>`
  - ```{autodoc2-docstring} utils.file_utils.mkdir
    :summary:
    ```
* - {py:obj}`parse_str_of_num_bytes <utils.file_utils.parse_str_of_num_bytes>`
  - ```{autodoc2-docstring} utils.file_utils.parse_str_of_num_bytes
    :summary:
    ```
* - {py:obj}`remove_path_extension <utils.file_utils.remove_path_extension>`
  - ```{autodoc2-docstring} utils.file_utils.remove_path_extension
    :summary:
    ```
* - {py:obj}`reshard_jsonl <utils.file_utils.reshard_jsonl>`
  - ```{autodoc2-docstring} utils.file_utils.reshard_jsonl
    :summary:
    ```
* - {py:obj}`separate_by_metadata <utils.file_utils.separate_by_metadata>`
  - ```{autodoc2-docstring} utils.file_utils.separate_by_metadata
    :summary:
    ```
* - {py:obj}`write_dataframe_by_meta <utils.file_utils.write_dataframe_by_meta>`
  - ```{autodoc2-docstring} utils.file_utils.write_dataframe_by_meta
    :summary:
    ```
* - {py:obj}`write_record <utils.file_utils.write_record>`
  - ```{autodoc2-docstring} utils.file_utils.write_record
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NEMO_CURATOR_HOME <utils.file_utils.NEMO_CURATOR_HOME>`
  - ```{autodoc2-docstring} utils.file_utils.NEMO_CURATOR_HOME
    :summary:
    ```
````

### API

````{py:data} NEMO_CURATOR_HOME
:canonical: utils.file_utils.NEMO_CURATOR_HOME
:value: >
   'get(...)'

```{autodoc2-docstring} utils.file_utils.NEMO_CURATOR_HOME
```

````

````{py:function} expand_outdir_and_mkdir(outdir: str) -> str
:canonical: utils.file_utils.expand_outdir_and_mkdir

```{autodoc2-docstring} utils.file_utils.expand_outdir_and_mkdir
```
````

````{py:function} filter_files_by_extension(files_list: list[str], keep_extensions: str | list[str]) -> list[str]
:canonical: utils.file_utils.filter_files_by_extension

```{autodoc2-docstring} utils.file_utils.filter_files_by_extension
```
````

````{py:function} get_all_files_paths_under(root: str, recurse_subdirectories: bool = True, followlinks: bool = False, keep_extensions: str | list[str] | None = None) -> list[str]
:canonical: utils.file_utils.get_all_files_paths_under

```{autodoc2-docstring} utils.file_utils.get_all_files_paths_under
```
````

````{py:function} get_batched_files(input_file_path: str, output_file_path: str, input_file_type: str, batch_size: int = 64) -> list[list[str]]
:canonical: utils.file_utils.get_batched_files

```{autodoc2-docstring} utils.file_utils.get_batched_files
```
````

````{py:function} get_remaining_files(input_file_path: str, output_file_path: str, input_file_type: str, output_file_type: str | None = None, num_files: int = -1) -> list[str]
:canonical: utils.file_utils.get_remaining_files

```{autodoc2-docstring} utils.file_utils.get_remaining_files
```
````

````{py:function} merge_counts(first: dict, second: dict) -> dict
:canonical: utils.file_utils.merge_counts

```{autodoc2-docstring} utils.file_utils.merge_counts
```
````

````{py:function} mkdir(d: str) -> None
:canonical: utils.file_utils.mkdir

```{autodoc2-docstring} utils.file_utils.mkdir
```
````

````{py:function} parse_str_of_num_bytes(s: str, return_str: bool = False) -> str | int
:canonical: utils.file_utils.parse_str_of_num_bytes

```{autodoc2-docstring} utils.file_utils.parse_str_of_num_bytes
```
````

````{py:function} remove_path_extension(path: str) -> str
:canonical: utils.file_utils.remove_path_extension

```{autodoc2-docstring} utils.file_utils.remove_path_extension
```
````

````{py:function} reshard_jsonl(input_dir: str, output_dir: str, output_file_size: str = '100M', start_index: int = 0, file_prefix: str = '') -> None
:canonical: utils.file_utils.reshard_jsonl

```{autodoc2-docstring} utils.file_utils.reshard_jsonl
```
````

````{py:function} separate_by_metadata(input_data: dask.dataframe.DataFrame | str, output_dir: str, metadata_field: str, remove_metadata: bool = False, output_type: str = 'jsonl', input_type: str = 'jsonl', include_values: list[str] | None = None, exclude_values: list[str] | None = None, filename_col: str = 'file_name') -> dict
:canonical: utils.file_utils.separate_by_metadata

```{autodoc2-docstring} utils.file_utils.separate_by_metadata
```
````

````{py:function} write_dataframe_by_meta(df: pandas.DataFrame, output_dir: str, metadata_field: str, remove_metadata: bool = False, output_type: str = 'jsonl', include_values: list[str] | None = None, exclude_values: list[str] | None = None, filename_col: str = 'file_name') -> dict
:canonical: utils.file_utils.write_dataframe_by_meta

```{autodoc2-docstring} utils.file_utils.write_dataframe_by_meta
```
````

````{py:function} write_record(input_dir: str, file_name: str, line: str, field: str, output_dir: str, include_values: list[str] | None = None, exclude_values: list[str] | None = None) -> str | None
:canonical: utils.file_utils.write_record

```{autodoc2-docstring} utils.file_utils.write_record
```
````
