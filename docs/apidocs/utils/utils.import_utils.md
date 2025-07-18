# {py:mod}`utils.import_utils`

```{py:module} utils.import_utils
```

```{autodoc2-docstring} utils.import_utils
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`UnavailableMeta <utils.import_utils.UnavailableMeta>`
  - ```{autodoc2-docstring} utils.import_utils.UnavailableMeta
    :summary:
    ```
* - {py:obj}`UnavailableNullContext <utils.import_utils.UnavailableNullContext>`
  - ```{autodoc2-docstring} utils.import_utils.UnavailableNullContext
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`image_only_import_from <utils.import_utils.image_only_import_from>`
  - ```{autodoc2-docstring} utils.import_utils.image_only_import_from
    :summary:
    ```
* - {py:obj}`is_unavailable <utils.import_utils.is_unavailable>`
  - ```{autodoc2-docstring} utils.import_utils.is_unavailable
    :summary:
    ```
* - {py:obj}`null_decorator <utils.import_utils.null_decorator>`
  - ```{autodoc2-docstring} utils.import_utils.null_decorator
    :summary:
    ```
* - {py:obj}`safe_import <utils.import_utils.safe_import>`
  - ```{autodoc2-docstring} utils.import_utils.safe_import
    :summary:
    ```
* - {py:obj}`safe_import_from <utils.import_utils.safe_import_from>`
  - ```{autodoc2-docstring} utils.import_utils.safe_import_from
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IMAGE_INSTALL_STRING <utils.import_utils.IMAGE_INSTALL_STRING>`
  - ```{autodoc2-docstring} utils.import_utils.IMAGE_INSTALL_STRING
    :summary:
    ```
* - {py:obj}`logger <utils.import_utils.logger>`
  - ```{autodoc2-docstring} utils.import_utils.logger
    :summary:
    ```
````

### API

````{py:data} IMAGE_INSTALL_STRING
:canonical: utils.import_utils.IMAGE_INSTALL_STRING
:value: <Multiline-String>

```{autodoc2-docstring} utils.import_utils.IMAGE_INSTALL_STRING
```

````

````{py:exception} UnavailableError()
:canonical: utils.import_utils.UnavailableError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} utils.import_utils.UnavailableError
```

```{rubric} Initialization
```

```{autodoc2-docstring} utils.import_utils.UnavailableError.__init__
```

````

````{py:class} UnavailableMeta
:canonical: utils.import_utils.UnavailableMeta

Bases: {py:obj}`type`

```{autodoc2-docstring} utils.import_utils.UnavailableMeta
```

````

````{py:class} UnavailableNullContext(*args, **kwargs)
:canonical: utils.import_utils.UnavailableNullContext

```{autodoc2-docstring} utils.import_utils.UnavailableNullContext
```

```{rubric} Initialization
```

```{autodoc2-docstring} utils.import_utils.UnavailableNullContext.__init__
```

````

````{py:function} image_only_import_from(module: str, symbol: str, *, alt: object | None = None) -> object
:canonical: utils.import_utils.image_only_import_from

```{autodoc2-docstring} utils.import_utils.image_only_import_from
```
````

````{py:function} is_unavailable(obj: object) -> bool
:canonical: utils.import_utils.is_unavailable

```{autodoc2-docstring} utils.import_utils.is_unavailable
```
````

````{py:data} logger
:canonical: utils.import_utils.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} utils.import_utils.logger
```

````

````{py:function} null_decorator(*args, **kwargs)
:canonical: utils.import_utils.null_decorator

```{autodoc2-docstring} utils.import_utils.null_decorator
```
````

````{py:function} safe_import(module: str, *, msg: str | None = None, alt: object | None = None) -> object
:canonical: utils.import_utils.safe_import

```{autodoc2-docstring} utils.import_utils.safe_import
```
````

````{py:function} safe_import_from(module: str, symbol: str, *, msg: str | None = None, alt: object | None = None) -> object
:canonical: utils.import_utils.safe_import_from

```{autodoc2-docstring} utils.import_utils.safe_import_from
```
````
