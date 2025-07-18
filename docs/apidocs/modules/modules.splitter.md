# {py:mod}`modules.splitter`

```{py:module} modules.splitter
```

```{autodoc2-docstring} modules.splitter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DocumentSplitter <modules.splitter.DocumentSplitter>`
  - ```{autodoc2-docstring} modules.splitter.DocumentSplitter
    :summary:
    ```
````

### API

`````{py:class} DocumentSplitter(separator: str, text_field: str = 'text', segment_id_field: str = 'segment_id')
:canonical: modules.splitter.DocumentSplitter

Bases: {py:obj}`nemo_curator.modules.base.BaseModule`

```{autodoc2-docstring} modules.splitter.DocumentSplitter
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.splitter.DocumentSplitter.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.splitter.DocumentSplitter.call

```{autodoc2-docstring} modules.splitter.DocumentSplitter.call
```

````

`````
