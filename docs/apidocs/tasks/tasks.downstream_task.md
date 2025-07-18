# {py:mod}`tasks.downstream_task`

```{py:module} tasks.downstream_task
```

```{autodoc2-docstring} tasks.downstream_task
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DownstreamTask <tasks.downstream_task.DownstreamTask>`
  - ```{autodoc2-docstring} tasks.downstream_task.DownstreamTask
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`import_task <tasks.downstream_task.import_task>`
  - ```{autodoc2-docstring} tasks.downstream_task.import_task
    :summary:
    ```
````

### API

`````{py:class} DownstreamTask()
:canonical: tasks.downstream_task.DownstreamTask

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} tasks.downstream_task.DownstreamTask
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.downstream_task.DownstreamTask.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.downstream_task.DownstreamTask.generate_ngrams
:abstractmethod:

```{autodoc2-docstring} tasks.downstream_task.DownstreamTask.generate_ngrams
```

````

````{py:property} ngrams
:canonical: tasks.downstream_task.DownstreamTask.ngrams
:type: dict[str, int]

```{autodoc2-docstring} tasks.downstream_task.DownstreamTask.ngrams
```

````

`````

````{py:function} import_task(task_path: str) -> tasks.downstream_task.DownstreamTask
:canonical: tasks.downstream_task.import_task

```{autodoc2-docstring} tasks.downstream_task.import_task
```
````
