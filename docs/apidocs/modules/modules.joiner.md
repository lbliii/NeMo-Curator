# {py:mod}`modules.joiner`

```{py:module} modules.joiner
```

```{autodoc2-docstring} modules.joiner
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DocumentJoiner <modules.joiner.DocumentJoiner>`
  - ```{autodoc2-docstring} modules.joiner.DocumentJoiner
    :summary:
    ```
````

### API

`````{py:class} DocumentJoiner(separator: str, text_field: str = 'text', segment_id_field: str = 'segment_id', document_id_field: str = 'id', drop_segment_id_field: bool = True, max_length: int | None = None, length_field: str | None = None)
:canonical: modules.joiner.DocumentJoiner

Bases: {py:obj}`nemo_curator.modules.base.BaseModule`

```{autodoc2-docstring} modules.joiner.DocumentJoiner
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.joiner.DocumentJoiner.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.joiner.DocumentJoiner.call

```{autodoc2-docstring} modules.joiner.DocumentJoiner.call
```

````

`````
