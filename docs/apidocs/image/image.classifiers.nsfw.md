# {py:mod}`image.classifiers.nsfw`

```{py:module} image.classifiers.nsfw
```

```{autodoc2-docstring} image.classifiers.nsfw
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NSFWModel <image.classifiers.nsfw.NSFWModel>`
  - ```{autodoc2-docstring} image.classifiers.nsfw.NSFWModel
    :summary:
    ```
* - {py:obj}`Normalization <image.classifiers.nsfw.Normalization>`
  - ```{autodoc2-docstring} image.classifiers.nsfw.Normalization
    :summary:
    ```
* - {py:obj}`NsfwClassifier <image.classifiers.nsfw.NsfwClassifier>`
  - ```{autodoc2-docstring} image.classifiers.nsfw.NsfwClassifier
    :summary:
    ```
````

### API

`````{py:class} NSFWModel()
:canonical: image.classifiers.nsfw.NSFWModel

Bases: {py:obj}`torch.nn.Module`

```{autodoc2-docstring} image.classifiers.nsfw.NSFWModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} image.classifiers.nsfw.NSFWModel.__init__
```

````{py:method} forward(x: torch.Tensor) -> torch.Tensor
:canonical: image.classifiers.nsfw.NSFWModel.forward

```{autodoc2-docstring} image.classifiers.nsfw.NSFWModel.forward
```

````

`````

`````{py:class} Normalization(shape: list[int])
:canonical: image.classifiers.nsfw.Normalization

Bases: {py:obj}`torch.nn.Module`

```{autodoc2-docstring} image.classifiers.nsfw.Normalization
```

```{rubric} Initialization
```

```{autodoc2-docstring} image.classifiers.nsfw.Normalization.__init__
```

````{py:method} forward(x: torch.Tensor) -> torch.Tensor
:canonical: image.classifiers.nsfw.Normalization.forward

```{autodoc2-docstring} image.classifiers.nsfw.Normalization.forward
```

````

`````

`````{py:class} NsfwClassifier(embedding_column: str = 'image_embedding', pred_column: str = 'nsfw_score', batch_size: int = -1, model_path: str | None = None)
:canonical: image.classifiers.nsfw.NsfwClassifier

Bases: {py:obj}`nemo_curator.image.classifiers.base.ImageClassifier`

```{autodoc2-docstring} image.classifiers.nsfw.NsfwClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} image.classifiers.nsfw.NsfwClassifier.__init__
```

````{py:method} load_model(device: str) -> torch.nn.Module
:canonical: image.classifiers.nsfw.NsfwClassifier.load_model

```{autodoc2-docstring} image.classifiers.nsfw.NsfwClassifier.load_model
```

````

````{py:method} postprocess(series: cudf.Series) -> cudf.Series
:canonical: image.classifiers.nsfw.NsfwClassifier.postprocess

```{autodoc2-docstring} image.classifiers.nsfw.NsfwClassifier.postprocess
```

````

`````
