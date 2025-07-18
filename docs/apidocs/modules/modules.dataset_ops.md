# {py:mod}`modules.dataset_ops`

```{py:module} modules.dataset_ops
```

```{autodoc2-docstring} modules.dataset_ops
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Shuffle <modules.dataset_ops.Shuffle>`
  - ```{autodoc2-docstring} modules.dataset_ops.Shuffle
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`blend_datasets <modules.dataset_ops.blend_datasets>`
  - ```{autodoc2-docstring} modules.dataset_ops.blend_datasets
    :summary:
    ```
* - {py:obj}`default_filename <modules.dataset_ops.default_filename>`
  - ```{autodoc2-docstring} modules.dataset_ops.default_filename
    :summary:
    ```
````

### API

`````{py:class} Shuffle(seed: int | None = None, npartitions: int | None = None, partition_to_filename: collections.abc.Callable[[int], str] = default_filename, filename_col: str = 'file_name')
:canonical: modules.dataset_ops.Shuffle

Bases: {py:obj}`nemo_curator.modules.base.BaseModule`

```{autodoc2-docstring} modules.dataset_ops.Shuffle
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.dataset_ops.Shuffle.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.doc_dataset.DocumentDataset) -> nemo_curator.datasets.doc_dataset.DocumentDataset
:canonical: modules.dataset_ops.Shuffle.call

```{autodoc2-docstring} modules.dataset_ops.Shuffle.call
```

````

````{py:method} shuffle_deterministic(dataset: nemo_curator.datasets.doc_dataset.DocumentDataset) -> nemo_curator.datasets.doc_dataset.DocumentDataset
:canonical: modules.dataset_ops.Shuffle.shuffle_deterministic

```{autodoc2-docstring} modules.dataset_ops.Shuffle.shuffle_deterministic
```

````

````{py:method} shuffle_nondeterministic(dataset: nemo_curator.datasets.doc_dataset.DocumentDataset) -> nemo_curator.datasets.doc_dataset.DocumentDataset
:canonical: modules.dataset_ops.Shuffle.shuffle_nondeterministic

```{autodoc2-docstring} modules.dataset_ops.Shuffle.shuffle_nondeterministic
```

````

`````

````{py:function} blend_datasets(target_size: int, datasets: list[nemo_curator.datasets.doc_dataset.DocumentDataset], sampling_weights: list[float]) -> nemo_curator.datasets.doc_dataset.DocumentDataset
:canonical: modules.dataset_ops.blend_datasets

```{autodoc2-docstring} modules.dataset_ops.blend_datasets
```
````

````{py:function} default_filename(partition_num: int) -> str
:canonical: modules.dataset_ops.default_filename

```{autodoc2-docstring} modules.dataset_ops.default_filename
```
````
