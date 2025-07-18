# {py:mod}`image.classifiers.base`

```{py:module} image.classifiers.base
```

```{autodoc2-docstring} image.classifiers.base
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ImageClassifier <image.classifiers.base.ImageClassifier>`
  - ```{autodoc2-docstring} image.classifiers.base.ImageClassifier
    :summary:
    ```
````

### API

`````{py:class} ImageClassifier(model_name: str, embedding_column: str, pred_column: str, pred_type: str | type, batch_size: int, embedding_size: int)
:canonical: image.classifiers.base.ImageClassifier

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} image.classifiers.base.ImageClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} image.classifiers.base.ImageClassifier.__init__
```

````{py:method} load_model(device: str) -> collections.abc.Callable
:canonical: image.classifiers.base.ImageClassifier.load_model
:abstractmethod:

```{autodoc2-docstring} image.classifiers.base.ImageClassifier.load_model
```

````

````{py:method} postprocess(series: cudf.Series) -> cudf.Series
:canonical: image.classifiers.base.ImageClassifier.postprocess

```{autodoc2-docstring} image.classifiers.base.ImageClassifier.postprocess
```

````

`````
