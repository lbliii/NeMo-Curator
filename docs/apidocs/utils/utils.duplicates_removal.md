# {py:mod}`utils.duplicates_removal`

```{py:module} utils.duplicates_removal
```

```{autodoc2-docstring} utils.duplicates_removal
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`deduplicate_groups <utils.duplicates_removal.deduplicate_groups>`
  - ```{autodoc2-docstring} utils.duplicates_removal.deduplicate_groups
    :summary:
    ```
* - {py:obj}`left_anti_join <utils.duplicates_removal.left_anti_join>`
  - ```{autodoc2-docstring} utils.duplicates_removal.left_anti_join
    :summary:
    ```
* - {py:obj}`remove_duplicates <utils.duplicates_removal.remove_duplicates>`
  - ```{autodoc2-docstring} utils.duplicates_removal.remove_duplicates
    :summary:
    ```
````

### API

````{py:function} deduplicate_groups(duplicates: dask.dataframe.DataFrame, group_field: str | None, perform_shuffle: bool) -> dask.dataframe.DataFrame
:canonical: utils.duplicates_removal.deduplicate_groups

```{autodoc2-docstring} utils.duplicates_removal.deduplicate_groups
```
````

````{py:function} left_anti_join(left: dask.dataframe.DataFrame, right: dask.dataframe.DataFrame, left_on: str | list[str], right_on: str | list[str]) -> dask.dataframe.DataFrame
:canonical: utils.duplicates_removal.left_anti_join

```{autodoc2-docstring} utils.duplicates_removal.left_anti_join
```
````

````{py:function} remove_duplicates(left: dask.dataframe.DataFrame, duplicates: dask.dataframe.DataFrame, id_field: str, group_field: str | None = None, perform_shuffle: bool = False) -> dask.dataframe.DataFrame
:canonical: utils.duplicates_removal.remove_duplicates

```{autodoc2-docstring} utils.duplicates_removal.remove_duplicates
```
````
