# {py:mod}`modules.fuzzy_dedup.lsh`

```{py:module} modules.fuzzy_dedup.lsh
```

```{autodoc2-docstring} modules.fuzzy_dedup.lsh
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LSH <modules.fuzzy_dedup.lsh.LSH>`
  - ```{autodoc2-docstring} modules.fuzzy_dedup.lsh.LSH
    :summary:
    ```
````

### API

`````{py:class} LSH(cache_dir: str, num_hashes: int, num_buckets: int, buckets_per_shuffle: int = 1, false_positive_check: bool = False, logger: logging.LoggerAdapter | str = './', id_fields: str | list = 'id', minhash_field: str = '_minhash_signature', profile_dir: str | None = None)
:canonical: modules.fuzzy_dedup.lsh.LSH

```{autodoc2-docstring} modules.fuzzy_dedup.lsh.LSH
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.fuzzy_dedup.lsh.LSH.__init__
```

````{py:method} bucket_id_to_int(bucket_ddf: dask_cudf.DataFrame, bucket_col_name: str = 'bucket_id', start_id: int = 0) -> tuple[dask_cudf.DataFrame, int]
:canonical: modules.fuzzy_dedup.lsh.LSH.bucket_id_to_int

```{autodoc2-docstring} modules.fuzzy_dedup.lsh.LSH.bucket_id_to_int
```

````

````{py:method} lsh(write_path: str, df: dask_cudf.DataFrame) -> bool
:canonical: modules.fuzzy_dedup.lsh.LSH.lsh

```{autodoc2-docstring} modules.fuzzy_dedup.lsh.LSH.lsh
```

````

````{py:method} minhash_to_buckets(df: cudf.DataFrame, bucket_ranges: list[list[int]]) -> cudf.DataFrame
:canonical: modules.fuzzy_dedup.lsh.LSH.minhash_to_buckets

```{autodoc2-docstring} modules.fuzzy_dedup.lsh.LSH.minhash_to_buckets
```

````

`````
