# {py:mod}`modules.semantic_dedup.semanticclusterleveldedup`

```{py:module} modules.semantic_dedup.semanticclusterleveldedup
```

```{autodoc2-docstring} modules.semantic_dedup.semanticclusterleveldedup
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SemanticClusterLevelDedup <modules.semantic_dedup.semanticclusterleveldedup.SemanticClusterLevelDedup>`
  - ```{autodoc2-docstring} modules.semantic_dedup.semanticclusterleveldedup.SemanticClusterLevelDedup
    :summary:
    ```
````

### API

`````{py:class} SemanticClusterLevelDedup(n_clusters: int = 1000, emb_by_clust_dir: str = './clustering_results/embs_by_nearest_center', id_column: str = 'id', which_to_keep: str = 'hard', sim_metric: typing.Literal[cosine, l2] = 'cosine', output_dir: str = './clustering_results', embedding_column: str = 'embeddings', batched_cosine_similarity: int = 1024, logger: logging.Logger | str = './', profile_dir: str | None = None)
:canonical: modules.semantic_dedup.semanticclusterleveldedup.SemanticClusterLevelDedup

```{autodoc2-docstring} modules.semantic_dedup.semanticclusterleveldedup.SemanticClusterLevelDedup
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.semantic_dedup.semanticclusterleveldedup.SemanticClusterLevelDedup.__init__
```

````{py:method} compute_semantic_match_dfs() -> None
:canonical: modules.semantic_dedup.semanticclusterleveldedup.SemanticClusterLevelDedup.compute_semantic_match_dfs

```{autodoc2-docstring} modules.semantic_dedup.semanticclusterleveldedup.SemanticClusterLevelDedup.compute_semantic_match_dfs
```

````

````{py:method} extract_dedup_data(eps_to_extract: float) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.semantic_dedup.semanticclusterleveldedup.SemanticClusterLevelDedup.extract_dedup_data

```{autodoc2-docstring} modules.semantic_dedup.semanticclusterleveldedup.SemanticClusterLevelDedup.extract_dedup_data
```

````

`````
