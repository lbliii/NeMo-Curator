# {py:mod}`modules.fuzzy_dedup.jaccardsimilarity`

```{py:module} modules.fuzzy_dedup.jaccardsimilarity
```

```{autodoc2-docstring} modules.fuzzy_dedup.jaccardsimilarity
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`JaccardSimilarity <modules.fuzzy_dedup.jaccardsimilarity.JaccardSimilarity>`
  - ```{autodoc2-docstring} modules.fuzzy_dedup.jaccardsimilarity.JaccardSimilarity
    :summary:
    ```
````

### API

`````{py:class} JaccardSimilarity(id_field: str = 'id', anchor_id_fields: list[str] | None = None, text_field: str = 'text', ngram_width: int = 5)
:canonical: modules.fuzzy_dedup.jaccardsimilarity.JaccardSimilarity

```{autodoc2-docstring} modules.fuzzy_dedup.jaccardsimilarity.JaccardSimilarity
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.fuzzy_dedup.jaccardsimilarity.JaccardSimilarity.__init__
```

````{py:method} jaccard_compute(shuffled_docs_path: str) -> cudf.DataFrame
:canonical: modules.fuzzy_dedup.jaccardsimilarity.JaccardSimilarity.jaccard_compute

```{autodoc2-docstring} modules.fuzzy_dedup.jaccardsimilarity.JaccardSimilarity.jaccard_compute
```

````

`````
