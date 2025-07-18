# {py:mod}`image.embedders.base`

```{py:module} image.embedders.base
```

```{autodoc2-docstring} image.embedders.base
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ImageEmbedder <image.embedders.base.ImageEmbedder>`
  - ```{autodoc2-docstring} image.embedders.base.ImageEmbedder
    :summary:
    ```
````

### API

`````{py:class} ImageEmbedder(model_name: str, image_embedding_column: str, classifiers: collections.abc.Iterable[nemo_curator.image.classifiers.ImageClassifier])
:canonical: image.embedders.base.ImageEmbedder

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} image.embedders.base.ImageEmbedder
```

```{rubric} Initialization
```

```{autodoc2-docstring} image.embedders.base.ImageEmbedder.__init__
```

````{py:method} load_dataset_shard(tar_path: str) -> collections.abc.Iterable
:canonical: image.embedders.base.ImageEmbedder.load_dataset_shard
:abstractmethod:

```{autodoc2-docstring} image.embedders.base.ImageEmbedder.load_dataset_shard
```

````

````{py:method} load_embedding_model(device: str) -> collections.abc.Callable
:canonical: image.embedders.base.ImageEmbedder.load_embedding_model
:abstractmethod:

```{autodoc2-docstring} image.embedders.base.ImageEmbedder.load_embedding_model
```

````

`````
