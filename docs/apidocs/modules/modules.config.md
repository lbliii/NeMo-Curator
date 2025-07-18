# {py:mod}`modules.config`

```{py:module} modules.config
```

```{autodoc2-docstring} modules.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseConfig <modules.config.BaseConfig>`
  - ```{autodoc2-docstring} modules.config.BaseConfig
    :summary:
    ```
* - {py:obj}`FuzzyDuplicatesConfig <modules.config.FuzzyDuplicatesConfig>`
  - ```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig
    :summary:
    ```
* - {py:obj}`SemDedupConfig <modules.config.SemDedupConfig>`
  - ```{autodoc2-docstring} modules.config.SemDedupConfig
    :summary:
    ```
````

### API

`````{py:class} BaseConfig
:canonical: modules.config.BaseConfig

```{autodoc2-docstring} modules.config.BaseConfig
```

````{py:method} from_yaml(file_path: str) -> modules.config.BaseConfig
:canonical: modules.config.BaseConfig.from_yaml
:classmethod:

```{autodoc2-docstring} modules.config.BaseConfig.from_yaml
```

````

`````

`````{py:class} FuzzyDuplicatesConfig
:canonical: modules.config.FuzzyDuplicatesConfig

Bases: {py:obj}`modules.config.BaseConfig`

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig
```

````{py:attribute} bucket_mapping_blocksize
:canonical: modules.config.FuzzyDuplicatesConfig.bucket_mapping_blocksize
:type: int | None
:value: >
   None

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.bucket_mapping_blocksize
```

````

````{py:attribute} bucket_parts_per_worker
:canonical: modules.config.FuzzyDuplicatesConfig.bucket_parts_per_worker
:type: int | None
:value: >
   None

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.bucket_parts_per_worker
```

````

````{py:attribute} buckets_per_shuffle
:canonical: modules.config.FuzzyDuplicatesConfig.buckets_per_shuffle
:type: int
:value: >
   1

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.buckets_per_shuffle
```

````

````{py:attribute} cache_dir
:canonical: modules.config.FuzzyDuplicatesConfig.cache_dir
:type: str
:value: >
   None

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.cache_dir
```

````

````{py:attribute} char_ngrams
:canonical: modules.config.FuzzyDuplicatesConfig.char_ngrams
:type: int
:value: >
   24

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.char_ngrams
```

````

````{py:attribute} false_positive_check
:canonical: modules.config.FuzzyDuplicatesConfig.false_positive_check
:type: bool
:value: >
   False

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.false_positive_check
```

````

````{py:attribute} hashes_per_bucket
:canonical: modules.config.FuzzyDuplicatesConfig.hashes_per_bucket
:type: int
:value: >
   13

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.hashes_per_bucket
```

````

````{py:attribute} id_field
:canonical: modules.config.FuzzyDuplicatesConfig.id_field
:type: str
:value: >
   'id'

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.id_field
```

````

````{py:attribute} jaccard_threshold
:canonical: modules.config.FuzzyDuplicatesConfig.jaccard_threshold
:type: float | None
:value: >
   None

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.jaccard_threshold
```

````

````{py:attribute} num_anchors
:canonical: modules.config.FuzzyDuplicatesConfig.num_anchors
:type: int | None
:value: >
   None

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.num_anchors
```

````

````{py:attribute} num_buckets
:canonical: modules.config.FuzzyDuplicatesConfig.num_buckets
:type: int
:value: >
   20

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.num_buckets
```

````

````{py:attribute} parts_per_worker
:canonical: modules.config.FuzzyDuplicatesConfig.parts_per_worker
:type: int | None
:value: >
   None

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.parts_per_worker
```

````

````{py:attribute} perform_removal
:canonical: modules.config.FuzzyDuplicatesConfig.perform_removal
:type: bool
:value: >
   False

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.perform_removal
```

````

````{py:attribute} profile_dir
:canonical: modules.config.FuzzyDuplicatesConfig.profile_dir
:type: str | None
:value: >
   None

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.profile_dir
```

````

````{py:attribute} seed
:canonical: modules.config.FuzzyDuplicatesConfig.seed
:type: int
:value: >
   42

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.seed
```

````

````{py:attribute} text_field
:canonical: modules.config.FuzzyDuplicatesConfig.text_field
:type: str
:value: >
   'text'

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.text_field
```

````

````{py:attribute} use_64_bit_hash
:canonical: modules.config.FuzzyDuplicatesConfig.use_64_bit_hash
:type: bool
:value: >
   False

```{autodoc2-docstring} modules.config.FuzzyDuplicatesConfig.use_64_bit_hash
```

````

`````

`````{py:class} SemDedupConfig
:canonical: modules.config.SemDedupConfig

Bases: {py:obj}`modules.config.BaseConfig`

```{autodoc2-docstring} modules.config.SemDedupConfig
```

````{py:attribute} batched_cosine_similarity
:canonical: modules.config.SemDedupConfig.batched_cosine_similarity
:type: bool | int
:value: >
   1024

```{autodoc2-docstring} modules.config.SemDedupConfig.batched_cosine_similarity
```

````

````{py:attribute} cache_dir
:canonical: modules.config.SemDedupConfig.cache_dir
:type: str
:value: >
   None

```{autodoc2-docstring} modules.config.SemDedupConfig.cache_dir
```

````

````{py:attribute} clustering_input_partition_size
:canonical: modules.config.SemDedupConfig.clustering_input_partition_size
:type: str
:value: >
   '2gb'

```{autodoc2-docstring} modules.config.SemDedupConfig.clustering_input_partition_size
```

````

````{py:attribute} clustering_save_loc
:canonical: modules.config.SemDedupConfig.clustering_save_loc
:type: str
:value: >
   'clustering_results'

```{autodoc2-docstring} modules.config.SemDedupConfig.clustering_save_loc
```

````

````{py:attribute} embedding_batch_size
:canonical: modules.config.SemDedupConfig.embedding_batch_size
:type: int
:value: >
   128

```{autodoc2-docstring} modules.config.SemDedupConfig.embedding_batch_size
```

````

````{py:attribute} embedding_column
:canonical: modules.config.SemDedupConfig.embedding_column
:type: str
:value: >
   'embeddings'

```{autodoc2-docstring} modules.config.SemDedupConfig.embedding_column
```

````

````{py:attribute} embedding_max_mem_gb
:canonical: modules.config.SemDedupConfig.embedding_max_mem_gb
:type: int | None
:value: >
   None

```{autodoc2-docstring} modules.config.SemDedupConfig.embedding_max_mem_gb
```

````

````{py:attribute} embedding_model_name_or_path
:canonical: modules.config.SemDedupConfig.embedding_model_name_or_path
:type: str
:value: >
   'sentence-transformers/all-MiniLM-L6-v2'

```{autodoc2-docstring} modules.config.SemDedupConfig.embedding_model_name_or_path
```

````

````{py:attribute} embedding_pooling_strategy
:canonical: modules.config.SemDedupConfig.embedding_pooling_strategy
:type: str
:value: >
   'mean_pooling'

```{autodoc2-docstring} modules.config.SemDedupConfig.embedding_pooling_strategy
```

````

````{py:attribute} embeddings_save_loc
:canonical: modules.config.SemDedupConfig.embeddings_save_loc
:type: str
:value: >
   'embeddings'

```{autodoc2-docstring} modules.config.SemDedupConfig.embeddings_save_loc
```

````

````{py:attribute} eps_to_extract
:canonical: modules.config.SemDedupConfig.eps_to_extract
:type: float
:value: >
   0.01

```{autodoc2-docstring} modules.config.SemDedupConfig.eps_to_extract
```

````

````{py:attribute} max_iter
:canonical: modules.config.SemDedupConfig.max_iter
:type: int
:value: >
   100

```{autodoc2-docstring} modules.config.SemDedupConfig.max_iter
```

````

````{py:attribute} n_clusters
:canonical: modules.config.SemDedupConfig.n_clusters
:type: int
:value: >
   1000

```{autodoc2-docstring} modules.config.SemDedupConfig.n_clusters
```

````

````{py:attribute} num_files
:canonical: modules.config.SemDedupConfig.num_files
:type: int
:value: >
   None

```{autodoc2-docstring} modules.config.SemDedupConfig.num_files
```

````

````{py:attribute} profile_dir
:canonical: modules.config.SemDedupConfig.profile_dir
:type: str | None
:value: >
   None

```{autodoc2-docstring} modules.config.SemDedupConfig.profile_dir
```

````

````{py:attribute} random_state
:canonical: modules.config.SemDedupConfig.random_state
:type: int
:value: >
   1234

```{autodoc2-docstring} modules.config.SemDedupConfig.random_state
```

````

````{py:attribute} sim_metric
:canonical: modules.config.SemDedupConfig.sim_metric
:type: typing.Literal[cosine, l2]
:value: >
   'cosine'

```{autodoc2-docstring} modules.config.SemDedupConfig.sim_metric
```

````

````{py:attribute} which_to_keep
:canonical: modules.config.SemDedupConfig.which_to_keep
:type: typing.Literal[hard, easy, random]
:value: >
   'hard'

```{autodoc2-docstring} modules.config.SemDedupConfig.which_to_keep
```

````

````{py:attribute} write_embeddings_to_disk
:canonical: modules.config.SemDedupConfig.write_embeddings_to_disk
:type: bool
:value: >
   True

```{autodoc2-docstring} modules.config.SemDedupConfig.write_embeddings_to_disk
```

````

````{py:attribute} write_to_filename
:canonical: modules.config.SemDedupConfig.write_to_filename
:type: bool
:value: >
   False

```{autodoc2-docstring} modules.config.SemDedupConfig.write_to_filename
```

````

`````
