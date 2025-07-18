# {py:mod}`modules.semantic_dedup.embeddings`

```{py:module} modules.semantic_dedup.embeddings
```

```{autodoc2-docstring} modules.semantic_dedup.embeddings
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EmbeddingConfig <modules.semantic_dedup.embeddings.EmbeddingConfig>`
  - ```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingConfig
    :summary:
    ```
* - {py:obj}`EmbeddingCreator <modules.semantic_dedup.embeddings.EmbeddingCreator>`
  - ```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCreator
    :summary:
    ```
* - {py:obj}`EmbeddingCrossFitModel <modules.semantic_dedup.embeddings.EmbeddingCrossFitModel>`
  - ```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCrossFitModel
    :summary:
    ```
* - {py:obj}`EmbeddingPytorchModel <modules.semantic_dedup.embeddings.EmbeddingPytorchModel>`
  - ```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingPytorchModel
    :summary:
    ```
````

### API

`````{py:class} EmbeddingConfig
:canonical: modules.semantic_dedup.embeddings.EmbeddingConfig

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingConfig
```

````{py:attribute} max_seq_length
:canonical: modules.semantic_dedup.embeddings.EmbeddingConfig.max_seq_length
:type: int
:value: >
   None

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingConfig.max_seq_length
```

````

````{py:attribute} model_name_or_path
:canonical: modules.semantic_dedup.embeddings.EmbeddingConfig.model_name_or_path
:type: str
:value: >
   None

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingConfig.model_name_or_path
```

````

````{py:attribute} pooling_strategy
:canonical: modules.semantic_dedup.embeddings.EmbeddingConfig.pooling_strategy
:type: str
:value: >
   'mean_pooling'

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingConfig.pooling_strategy
```

````

`````

`````{py:class} EmbeddingCreator(embedding_model_name_or_path: str = 'sentence-transformers/all-MiniLM-L6-v2', embedding_batch_size: int = 128, embedding_output_dir: str = './embeddings', embedding_max_mem_gb: int | None = None, embedding_pooling_strategy: str = 'mean_pooling', input_column: str = 'text', embedding_column: str = 'embeddings', write_embeddings_to_disk: bool = True, write_to_filename: bool = False, logger: logging.Logger | str = './', profile_dir: str | None = None)
:canonical: modules.semantic_dedup.embeddings.EmbeddingCreator

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCreator
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCreator.__init__
```

````{py:method} create_embeddings(ddf: dask_cudf.DataFrame, input_column: str = 'text') -> dask_cudf.DataFrame
:canonical: modules.semantic_dedup.embeddings.EmbeddingCreator.create_embeddings

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCreator.create_embeddings
```

````

`````

`````{py:class} EmbeddingCrossFitModel(config: modules.semantic_dedup.embeddings.EmbeddingConfig, max_mem_gb: int | None = None)
:canonical: modules.semantic_dedup.embeddings.EmbeddingCrossFitModel

Bases: {py:obj}`crossfit.backend.torch.hf.model.HFModel`

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCrossFitModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCrossFitModel.__init__
```

````{py:method} load_config() -> transformers.AutoConfig
:canonical: modules.semantic_dedup.embeddings.EmbeddingCrossFitModel.load_config

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCrossFitModel.load_config
```

````

````{py:method} load_model(device: str = 'cuda') -> modules.semantic_dedup.embeddings.EmbeddingPytorchModel
:canonical: modules.semantic_dedup.embeddings.EmbeddingCrossFitModel.load_model

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCrossFitModel.load_model
```

````

````{py:method} load_tokenizer() -> transformers.AutoTokenizer
:canonical: modules.semantic_dedup.embeddings.EmbeddingCrossFitModel.load_tokenizer

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCrossFitModel.load_tokenizer
```

````

````{py:method} max_seq_length() -> int
:canonical: modules.semantic_dedup.embeddings.EmbeddingCrossFitModel.max_seq_length

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingCrossFitModel.max_seq_length
```

````

`````

`````{py:class} EmbeddingPytorchModel(config: modules.semantic_dedup.embeddings.EmbeddingConfig)
:canonical: modules.semantic_dedup.embeddings.EmbeddingPytorchModel

Bases: {py:obj}`torch.nn.Module`

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingPytorchModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingPytorchModel.__init__
```

````{py:method} feature(input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor
:canonical: modules.semantic_dedup.embeddings.EmbeddingPytorchModel.feature

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingPytorchModel.feature
```

````

````{py:method} forward(batch: dict[str, torch.Tensor]) -> torch.Tensor
:canonical: modules.semantic_dedup.embeddings.EmbeddingPytorchModel.forward

```{autodoc2-docstring} modules.semantic_dedup.embeddings.EmbeddingPytorchModel.forward
```

````

`````
