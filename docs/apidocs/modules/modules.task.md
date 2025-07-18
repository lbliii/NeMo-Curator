# {py:mod}`modules.task`

```{py:module} modules.task
```

```{autodoc2-docstring} modules.task
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TaskDecontamination <modules.task.TaskDecontamination>`
  - ```{autodoc2-docstring} modules.task.TaskDecontamination
    :summary:
    ```
````

### API

`````{py:class} TaskDecontamination(tasks: nemo_curator.tasks.downstream_task.DownstreamTask | collections.abc.Iterable[nemo_curator.tasks.downstream_task.DownstreamTask], text_field: str = 'text', max_ngram_size: int = 13, max_matches: int = 10, min_document_length: int = 200, remove_char_each_side: int = 200, max_splits: int = 10, removed_dir: str | None = None)
:canonical: modules.task.TaskDecontamination

Bases: {py:obj}`nemo_curator.modules.base.BaseModule`

```{autodoc2-docstring} modules.task.TaskDecontamination
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.task.TaskDecontamination.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.task.TaskDecontamination.call

```{autodoc2-docstring} modules.task.TaskDecontamination.call
```

````

````{py:method} find_matching_ngrams(task_ngrams: dict, dataset: nemo_curator.datasets.DocumentDataset) -> dict
:canonical: modules.task.TaskDecontamination.find_matching_ngrams

```{autodoc2-docstring} modules.task.TaskDecontamination.find_matching_ngrams
```

````

````{py:method} prepare_task_ngram_count() -> dict
:canonical: modules.task.TaskDecontamination.prepare_task_ngram_count

```{autodoc2-docstring} modules.task.TaskDecontamination.prepare_task_ngram_count
```

````

````{py:method} remove_matching_ngrams(matched_ngrams: dict, ngram_freq: list[tuple], dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.task.TaskDecontamination.remove_matching_ngrams

```{autodoc2-docstring} modules.task.TaskDecontamination.remove_matching_ngrams
```

````

`````
