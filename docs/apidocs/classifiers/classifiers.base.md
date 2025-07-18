# {py:mod}`classifiers.base`

```{py:module} classifiers.base
```

```{autodoc2-docstring} classifiers.base
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DistributedDataClassifier <classifiers.base.DistributedDataClassifier>`
  - ```{autodoc2-docstring} classifiers.base.DistributedDataClassifier
    :summary:
    ```
* - {py:obj}`HFDeberta <classifiers.base.HFDeberta>`
  - ```{autodoc2-docstring} classifiers.base.HFDeberta
    :summary:
    ```
````

### API

`````{py:class} DistributedDataClassifier(model: str, labels: list[str] | None, filter_by: list[str] | None, batch_size: int, out_dim: int | None, pred_column: str | list[str], max_chars: int, device_type: str, autocast: bool)
:canonical: classifiers.base.DistributedDataClassifier

Bases: {py:obj}`nemo_curator.modules.base.BaseModule`

```{autodoc2-docstring} classifiers.base.DistributedDataClassifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.base.DistributedDataClassifier.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: classifiers.base.DistributedDataClassifier.call

```{autodoc2-docstring} classifiers.base.DistributedDataClassifier.call
```

````

````{py:method} get_labels() -> list[str]
:canonical: classifiers.base.DistributedDataClassifier.get_labels

```{autodoc2-docstring} classifiers.base.DistributedDataClassifier.get_labels
```

````

`````

`````{py:class} HFDeberta(config: dataclasses.dataclass)
:canonical: classifiers.base.HFDeberta

Bases: {py:obj}`torch.nn.Module`, {py:obj}`huggingface_hub.PyTorchModelHubMixin`

```{autodoc2-docstring} classifiers.base.HFDeberta
```

```{rubric} Initialization
```

```{autodoc2-docstring} classifiers.base.HFDeberta.__init__
```

````{py:method} forward(batch: dict[str, torch.Tensor]) -> torch.Tensor
:canonical: classifiers.base.HFDeberta.forward

```{autodoc2-docstring} classifiers.base.HFDeberta.forward
```

````

````{py:method} set_autocast(autocast: bool) -> None
:canonical: classifiers.base.HFDeberta.set_autocast

```{autodoc2-docstring} classifiers.base.HFDeberta.set_autocast
```

````

`````
