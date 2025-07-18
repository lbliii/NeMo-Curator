# {py:mod}`utils.semdedup_utils`

```{py:module} utils.semdedup_utils
```

```{autodoc2-docstring} utils.semdedup_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`add_l2_cosine_dist_to_centroid <utils.semdedup_utils.add_l2_cosine_dist_to_centroid>`
  - ```{autodoc2-docstring} utils.semdedup_utils.add_l2_cosine_dist_to_centroid
    :summary:
    ```
* - {py:obj}`get_array_from_df <utils.semdedup_utils.get_array_from_df>`
  - ```{autodoc2-docstring} utils.semdedup_utils.get_array_from_df
    :summary:
    ```
* - {py:obj}`get_semantic_matches_per_cluster <utils.semdedup_utils.get_semantic_matches_per_cluster>`
  - ```{autodoc2-docstring} utils.semdedup_utils.get_semantic_matches_per_cluster
    :summary:
    ```
* - {py:obj}`normalize_embeddings_col_in_df <utils.semdedup_utils.normalize_embeddings_col_in_df>`
  - ```{autodoc2-docstring} utils.semdedup_utils.normalize_embeddings_col_in_df
    :summary:
    ```
* - {py:obj}`pairwise_cosine_similarity <utils.semdedup_utils.pairwise_cosine_similarity>`
  - ```{autodoc2-docstring} utils.semdedup_utils.pairwise_cosine_similarity
    :summary:
    ```
* - {py:obj}`pairwise_cosine_similarity_batched <utils.semdedup_utils.pairwise_cosine_similarity_batched>`
  - ```{autodoc2-docstring} utils.semdedup_utils.pairwise_cosine_similarity_batched
    :summary:
    ```
* - {py:obj}`prune_single_cluster <utils.semdedup_utils.prune_single_cluster>`
  - ```{autodoc2-docstring} utils.semdedup_utils.prune_single_cluster
    :summary:
    ```
* - {py:obj}`write_pruned_summary_file <utils.semdedup_utils.write_pruned_summary_file>`
  - ```{autodoc2-docstring} utils.semdedup_utils.write_pruned_summary_file
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`COSINE_DIST_TO_CENT_COL <utils.semdedup_utils.COSINE_DIST_TO_CENT_COL>`
  - ```{autodoc2-docstring} utils.semdedup_utils.COSINE_DIST_TO_CENT_COL
    :summary:
    ```
* - {py:obj}`L2_DIST_TO_CENT_COL <utils.semdedup_utils.L2_DIST_TO_CENT_COL>`
  - ```{autodoc2-docstring} utils.semdedup_utils.L2_DIST_TO_CENT_COL
    :summary:
    ```
````

### API

````{py:data} COSINE_DIST_TO_CENT_COL
:canonical: utils.semdedup_utils.COSINE_DIST_TO_CENT_COL
:value: >
   'cosine_dist_to_cent'

```{autodoc2-docstring} utils.semdedup_utils.COSINE_DIST_TO_CENT_COL
```

````

````{py:data} L2_DIST_TO_CENT_COL
:canonical: utils.semdedup_utils.L2_DIST_TO_CENT_COL
:value: >
   'l2_dist_to_cent'

```{autodoc2-docstring} utils.semdedup_utils.L2_DIST_TO_CENT_COL
```

````

````{py:function} add_l2_cosine_dist_to_centroid(df: cudf.DataFrame, embedding_col: str, centroids: cupy.ndarray) -> cudf.DataFrame
:canonical: utils.semdedup_utils.add_l2_cosine_dist_to_centroid

```{autodoc2-docstring} utils.semdedup_utils.add_l2_cosine_dist_to_centroid
```
````

````{py:function} get_array_from_df(df: cudf.DataFrame, embedding_col: str) -> cupy.ndarray
:canonical: utils.semdedup_utils.get_array_from_df

```{autodoc2-docstring} utils.semdedup_utils.get_array_from_df
```
````

````{py:function} get_semantic_matches_per_cluster(cluster_id: int, emb_by_clust_dir: str, id_col: str, output_dir: str, embedding_col: str, which_to_keep: typing.Literal[hard, easy, random], sim_metric: typing.Literal[cosine, l2], batched_cosine_similarity: int = 1024) -> None
:canonical: utils.semdedup_utils.get_semantic_matches_per_cluster

```{autodoc2-docstring} utils.semdedup_utils.get_semantic_matches_per_cluster
```
````

````{py:function} normalize_embeddings_col_in_df(df: cudf.DataFrame, embedding_col: str) -> cudf.DataFrame
:canonical: utils.semdedup_utils.normalize_embeddings_col_in_df

```{autodoc2-docstring} utils.semdedup_utils.normalize_embeddings_col_in_df
```
````

````{py:function} pairwise_cosine_similarity(cluster_reps: torch.Tensor, device: typing.Literal[cuda, cpu]) -> tuple[cupy.ndarray, cupy.ndarray]
:canonical: utils.semdedup_utils.pairwise_cosine_similarity

```{autodoc2-docstring} utils.semdedup_utils.pairwise_cosine_similarity
```
````

````{py:function} pairwise_cosine_similarity_batched(cluster_reps: torch.Tensor, device: typing.Literal[cuda, cpu], batch_size: int = 1024) -> tuple[cupy.ndarray, cupy.ndarray]
:canonical: utils.semdedup_utils.pairwise_cosine_similarity_batched

```{autodoc2-docstring} utils.semdedup_utils.pairwise_cosine_similarity_batched
```
````

````{py:function} prune_single_cluster(cluster_id: int, id_col: str, emb_by_clust_dir: str, semdedup_pruning_tables_dir: str, eps: float) -> cudf.DataFrame
:canonical: utils.semdedup_utils.prune_single_cluster

```{autodoc2-docstring} utils.semdedup_utils.prune_single_cluster
```
````

````{py:function} write_pruned_summary_file(eps: float, emb_by_clust_dir: str, filtered_unique_ids_path: str, output_summary_file: str, logger: logging.Logger) -> None
:canonical: utils.semdedup_utils.write_pruned_summary_file

```{autodoc2-docstring} utils.semdedup_utils.write_pruned_summary_file
```
````
