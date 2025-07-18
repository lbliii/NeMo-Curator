# {py:mod}`modules.filter`

```{py:module} modules.filter
```

```{autodoc2-docstring} modules.filter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Filter <modules.filter.Filter>`
  - ```{autodoc2-docstring} modules.filter.Filter
    :summary:
    ```
* - {py:obj}`ParallelScoreFilter <modules.filter.ParallelScoreFilter>`
  - ```{autodoc2-docstring} modules.filter.ParallelScoreFilter
    :summary:
    ```
* - {py:obj}`Score <modules.filter.Score>`
  - ```{autodoc2-docstring} modules.filter.Score
    :summary:
    ```
* - {py:obj}`ScoreFilter <modules.filter.ScoreFilter>`
  - ```{autodoc2-docstring} modules.filter.ScoreFilter
    :summary:
    ```
````

### API

`````{py:class} Filter(filter_fn: collections.abc.Callable | nemo_curator.filters.DocumentFilter, filter_field: str, invert: bool = False)
:canonical: modules.filter.Filter

Bases: {py:obj}`nemo_curator.modules.base.BaseModule`

```{autodoc2-docstring} modules.filter.Filter
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.filter.Filter.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.filter.Filter.call

```{autodoc2-docstring} modules.filter.Filter.call
```

````

````{py:method} compute_filter_mask(dataset: nemo_curator.datasets.DocumentDataset) -> pandas.Series | pandas.DataFrame
:canonical: modules.filter.Filter.compute_filter_mask

```{autodoc2-docstring} modules.filter.Filter.compute_filter_mask
```

````

`````

`````{py:class} ParallelScoreFilter(src_filter_obj: nemo_curator.filters.DocumentFilter, tgt_filter_obj: nemo_curator.filters.DocumentFilter, src_field: str = 'src', tgt_field: str = 'tgt', src_score: str | None = None, tgt_score: str | None = None, score_type: str | None = None, invert: bool = False)
:canonical: modules.filter.ParallelScoreFilter

Bases: {py:obj}`nemo_curator.modules.base.BaseModule`

```{autodoc2-docstring} modules.filter.ParallelScoreFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.filter.ParallelScoreFilter.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.parallel_dataset.ParallelDataset) -> nemo_curator.datasets.parallel_dataset.ParallelDataset
:canonical: modules.filter.ParallelScoreFilter.call

```{autodoc2-docstring} modules.filter.ParallelScoreFilter.call
```

````

`````

`````{py:class} Score(score_fn: collections.abc.Callable | nemo_curator.filters.DocumentFilter, score_field: str, text_field: str = 'text', score_type: type | str | None = None)
:canonical: modules.filter.Score

Bases: {py:obj}`nemo_curator.modules.base.BaseModule`

```{autodoc2-docstring} modules.filter.Score
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.filter.Score.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.filter.Score.call

```{autodoc2-docstring} modules.filter.Score.call
```

````

`````

`````{py:class} ScoreFilter(filter_obj: nemo_curator.filters.DocumentFilter, text_field: str = 'text', score_field: str | None = None, score_type: type | str | None = None, invert: bool = False)
:canonical: modules.filter.ScoreFilter

Bases: {py:obj}`nemo_curator.modules.base.BaseModule`

```{autodoc2-docstring} modules.filter.ScoreFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.filter.ScoreFilter.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.filter.ScoreFilter.call

```{autodoc2-docstring} modules.filter.ScoreFilter.call
```

````

````{py:method} compute_filter_mask(dataset: nemo_curator.datasets.DocumentDataset) -> pandas.Series | pandas.DataFrame
:canonical: modules.filter.ScoreFilter.compute_filter_mask

```{autodoc2-docstring} modules.filter.ScoreFilter.compute_filter_mask
```

````

`````
