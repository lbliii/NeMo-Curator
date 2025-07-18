# {py:mod}`image.classifiers.aesthetic`

```{py:module} image.classifiers.aesthetic
```

```{autodoc2-docstring} image.classifiers.aesthetic
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AestheticClassifier <image.classifiers.aesthetic.AestheticClassifier>`
  - ```{autodoc2-docstring} image.classifiers.aesthetic.AestheticClassifier
    :summary:
    ```
* - {py:obj}`MLP <image.classifiers.aesthetic.MLP>`
  - ```{autodoc2-docstring} image.classifiers.aesthetic.MLP
    :summary:
    ```
````

### API

`````{py:class} AestheticClassifier(embedding_column: str = 'image_embedding', pred_column: str = 'aesthetic_score', batch_size: int = -1, model_path: str | None = None)
:canonical: image.classifiers.aesthetic.AestheticClassifier

Bases: {py:obj}`nemo_curator.image.classifiers.base.ImageClassifier`

```{autodoc2-docstring} image.classifiers.aesthetic.AestheticClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} image.classifiers.aesthetic.AestheticClassifier.__init__
```

````{py:method} load_model(device: str) -> torch.nn.Module
:canonical: image.classifiers.aesthetic.AestheticClassifier.load_model

```{autodoc2-docstring} image.classifiers.aesthetic.AestheticClassifier.load_model
```

````

````{py:method} postprocess(series: cudf.Series) -> cudf.Series
:canonical: image.classifiers.aesthetic.AestheticClassifier.postprocess

```{autodoc2-docstring} image.classifiers.aesthetic.AestheticClassifier.postprocess
```

````

`````

`````{py:class} MLP(input_size: int, xcol: str = 'emb', ycol: str = 'avg_rating')
:canonical: image.classifiers.aesthetic.MLP

Bases: {py:obj}`torch.nn.Module`

```{autodoc2-docstring} image.classifiers.aesthetic.MLP
```

```{rubric} Initialization
```

```{autodoc2-docstring} image.classifiers.aesthetic.MLP.__init__
```

````{py:method} forward(x: torch.Tensor) -> torch.Tensor
:canonical: image.classifiers.aesthetic.MLP.forward

```{autodoc2-docstring} image.classifiers.aesthetic.MLP.forward
```

````

`````
