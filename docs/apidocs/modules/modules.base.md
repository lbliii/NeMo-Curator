# {py:mod}`modules.base`

```{py:module} modules.base
```

```{autodoc2-docstring} modules.base
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseDeduplicationModule <modules.base.BaseDeduplicationModule>`
  - ```{autodoc2-docstring} modules.base.BaseDeduplicationModule
    :summary:
    ```
* - {py:obj}`BaseModule <modules.base.BaseModule>`
  - ```{autodoc2-docstring} modules.base.BaseModule
    :summary:
    ```
````

### API

`````{py:class} BaseDeduplicationModule(id_field: str, text_field: str, perform_removal: bool = False, logger: logging.LoggerAdapter | str = './', profile_dir: str | None = None, cache_dir: str | None = None, input_backend: typing.Literal[pandas, cudf, any] = 'any', **kwargs)
:canonical: modules.base.BaseDeduplicationModule

Bases: {py:obj}`modules.base.BaseModule`

```{autodoc2-docstring} modules.base.BaseDeduplicationModule
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.base.BaseDeduplicationModule.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.base.BaseDeduplicationModule.call

```{autodoc2-docstring} modules.base.BaseDeduplicationModule.call
```

````

````{py:method} identify_duplicates(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.base.BaseDeduplicationModule.identify_duplicates
:abstractmethod:

```{autodoc2-docstring} modules.base.BaseDeduplicationModule.identify_duplicates
```

````

````{py:method} remove(dataset: nemo_curator.datasets.DocumentDataset, duplicates_to_remove: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.base.BaseDeduplicationModule.remove
:abstractmethod:

```{autodoc2-docstring} modules.base.BaseDeduplicationModule.remove
```

````

`````

`````{py:class} BaseModule(input_backend: typing.Literal[pandas, cudf, any], name: str | None = None)
:canonical: modules.base.BaseModule

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} modules.base.BaseModule
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.base.BaseModule.__init__
```

````{py:attribute} SUPPORTED_BACKENDS
:canonical: modules.base.BaseModule.SUPPORTED_BACKENDS
:value: >
   ('pandas', 'cudf', 'any')

```{autodoc2-docstring} modules.base.BaseModule.SUPPORTED_BACKENDS
```

````

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: modules.base.BaseModule.call
:abstractmethod:

```{autodoc2-docstring} modules.base.BaseModule.call
```

````

`````
