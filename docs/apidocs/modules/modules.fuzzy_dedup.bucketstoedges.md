# {py:mod}`modules.fuzzy_dedup.bucketstoedges`

```{py:module} modules.fuzzy_dedup.bucketstoedges
```

```{autodoc2-docstring} modules.fuzzy_dedup.bucketstoedges
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BucketsToEdges <modules.fuzzy_dedup.bucketstoedges.BucketsToEdges>`
  - ```{autodoc2-docstring} modules.fuzzy_dedup.bucketstoedges.BucketsToEdges
    :summary:
    ```
````

### API

`````{py:class} BucketsToEdges(cache_dir: str | None = None, id_fields: list | str = 'id', str_id_name: str = 'id', bucket_field: str = '_bucket_id', logger: logging.LoggerAdapter | str = './', profile_dir: str | None = None)
:canonical: modules.fuzzy_dedup.bucketstoedges.BucketsToEdges

```{autodoc2-docstring} modules.fuzzy_dedup.bucketstoedges.BucketsToEdges
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.fuzzy_dedup.bucketstoedges.BucketsToEdges.__init__
```

````{py:method} buckets_to_edges(buckets_df: cudf.DataFrame) -> cudf.DataFrame
:canonical: modules.fuzzy_dedup.bucketstoedges.BucketsToEdges.buckets_to_edges

```{autodoc2-docstring} modules.fuzzy_dedup.bucketstoedges.BucketsToEdges.buckets_to_edges
```

````

`````
