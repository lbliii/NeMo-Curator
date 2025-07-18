# {py:mod}`image.embedders.timm`

```{py:module} image.embedders.timm
```

```{autodoc2-docstring} image.embedders.timm
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TimmImageEmbedder <image.embedders.timm.TimmImageEmbedder>`
  - ```{autodoc2-docstring} image.embedders.timm.TimmImageEmbedder
    :summary:
    ```
````

### API

`````{py:class} TimmImageEmbedder(model_name: str, pretrained: bool = False, batch_size: int = 1, num_threads_per_worker: int = 4, image_embedding_column: str = 'image_embedding', normalize_embeddings: bool = True, classifiers: collections.abc.Iterable = [], autocast: bool = True, use_index_files: bool = False)
:canonical: image.embedders.timm.TimmImageEmbedder

Bases: {py:obj}`nemo_curator.image.embedders.base.ImageEmbedder`

```{autodoc2-docstring} image.embedders.timm.TimmImageEmbedder
```

```{rubric} Initialization
```

```{autodoc2-docstring} image.embedders.timm.TimmImageEmbedder.__init__
```

````{py:method} load_dataset_shard(tar_path: str) -> collections.abc.Iterable
:canonical: image.embedders.timm.TimmImageEmbedder.load_dataset_shard

```{autodoc2-docstring} image.embedders.timm.TimmImageEmbedder.load_dataset_shard
```

````

````{py:method} load_embedding_model(device: str = 'cuda') -> torch.nn.Module
:canonical: image.embedders.timm.TimmImageEmbedder.load_embedding_model

```{autodoc2-docstring} image.embedders.timm.TimmImageEmbedder.load_embedding_model
```

````

`````
