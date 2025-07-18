# {py:mod}`filters.models.qe_models`

```{py:module} filters.models.qe_models
```

```{autodoc2-docstring} filters.models.qe_models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`COMETQEModel <filters.models.qe_models.COMETQEModel>`
  - ```{autodoc2-docstring} filters.models.qe_models.COMETQEModel
    :summary:
    ```
* - {py:obj}`PyMarianQEModel <filters.models.qe_models.PyMarianQEModel>`
  - ```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel
    :summary:
    ```
* - {py:obj}`QEModel <filters.models.qe_models.QEModel>`
  - ```{autodoc2-docstring} filters.models.qe_models.QEModel
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`COMET_IMPORT_MSG <filters.models.qe_models.COMET_IMPORT_MSG>`
  - ```{autodoc2-docstring} filters.models.qe_models.COMET_IMPORT_MSG
    :summary:
    ```
* - {py:obj}`PYMARIAN_IMPORT_MSG <filters.models.qe_models.PYMARIAN_IMPORT_MSG>`
  - ```{autodoc2-docstring} filters.models.qe_models.PYMARIAN_IMPORT_MSG
    :summary:
    ```
* - {py:obj}`comet <filters.models.qe_models.comet>`
  - ```{autodoc2-docstring} filters.models.qe_models.comet
    :summary:
    ```
* - {py:obj}`pymarian <filters.models.qe_models.pymarian>`
  - ```{autodoc2-docstring} filters.models.qe_models.pymarian
    :summary:
    ```
````

### API

`````{py:class} COMETQEModel(name: str, model: collections.abc.Callable, gpu: bool = False)
:canonical: filters.models.qe_models.COMETQEModel

Bases: {py:obj}`filters.models.qe_models.QEModel`

```{autodoc2-docstring} filters.models.qe_models.COMETQEModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.models.qe_models.COMETQEModel.__init__
```

````{py:attribute} MODEL_NAME_TO_HF_PATH
:canonical: filters.models.qe_models.COMETQEModel.MODEL_NAME_TO_HF_PATH
:type: typing.Final[dict[str, str]]
:value: >
   None

```{autodoc2-docstring} filters.models.qe_models.COMETQEModel.MODEL_NAME_TO_HF_PATH
```

````

````{py:method} load_model(model_name: str, gpu: bool = False) -> filters.models.qe_models.COMETQEModel
:canonical: filters.models.qe_models.COMETQEModel.load_model
:classmethod:

```{autodoc2-docstring} filters.models.qe_models.COMETQEModel.load_model
```

````

````{py:method} predict(input_list: list) -> list[float]
:canonical: filters.models.qe_models.COMETQEModel.predict

```{autodoc2-docstring} filters.models.qe_models.COMETQEModel.predict
```

````

````{py:method} wrap_qe_input(src: str, tgt: str, reverse: bool = False) -> dict[str, str]
:canonical: filters.models.qe_models.COMETQEModel.wrap_qe_input
:staticmethod:

```{autodoc2-docstring} filters.models.qe_models.COMETQEModel.wrap_qe_input
```

````

`````

````{py:data} COMET_IMPORT_MSG
:canonical: filters.models.qe_models.COMET_IMPORT_MSG
:value: >
   'To run QE filtering with COMET, you need to install from PyPI with: `pip install unbabel-comet`. Mor...'

```{autodoc2-docstring} filters.models.qe_models.COMET_IMPORT_MSG
```

````

````{py:data} PYMARIAN_IMPORT_MSG
:canonical: filters.models.qe_models.PYMARIAN_IMPORT_MSG
:value: >
   'To run QE filtering with Cometoid/PyMarian, you need to install PyMarian. More information at https:...'

```{autodoc2-docstring} filters.models.qe_models.PYMARIAN_IMPORT_MSG
```

````

`````{py:class} PyMarianQEModel(name: str, model: collections.abc.Callable, gpu: bool = False)
:canonical: filters.models.qe_models.PyMarianQEModel

Bases: {py:obj}`filters.models.qe_models.QEModel`

```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel.__init__
```

````{py:attribute} MARIAN_CPU_ARGS
:canonical: filters.models.qe_models.PyMarianQEModel.MARIAN_CPU_ARGS
:value: >
   ' --cpu-threads 1 -w 2000'

```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel.MARIAN_CPU_ARGS
```

````

````{py:attribute} MARIAN_GPU_ARGS
:canonical: filters.models.qe_models.PyMarianQEModel.MARIAN_GPU_ARGS
:value: >
   ' -w 8000 --mini-batch 32 -d 0'

```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel.MARIAN_GPU_ARGS
```

````

````{py:attribute} MODEL_NAME_TO_HF_PATH
:canonical: filters.models.qe_models.PyMarianQEModel.MODEL_NAME_TO_HF_PATH
:type: typing.Final[dict[str, str]]
:value: >
   None

```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel.MODEL_NAME_TO_HF_PATH
```

````

````{py:attribute} SHARD_SIZE
:canonical: filters.models.qe_models.PyMarianQEModel.SHARD_SIZE
:value: >
   5000

```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel.SHARD_SIZE
```

````

````{py:method} load_model(model_name: str, gpu: bool = False) -> filters.models.qe_models.PyMarianQEModel
:canonical: filters.models.qe_models.PyMarianQEModel.load_model
:classmethod:

```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel.load_model
```

````

````{py:method} predict(input_list: list) -> list[float]
:canonical: filters.models.qe_models.PyMarianQEModel.predict

```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel.predict
```

````

````{py:method} wrap_qe_input(src: str, tgt: str, reverse: bool = False) -> list[str]
:canonical: filters.models.qe_models.PyMarianQEModel.wrap_qe_input
:staticmethod:

```{autodoc2-docstring} filters.models.qe_models.PyMarianQEModel.wrap_qe_input
```

````

`````

`````{py:class} QEModel(name: str, model: collections.abc.Callable, gpu: bool = False)
:canonical: filters.models.qe_models.QEModel

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} filters.models.qe_models.QEModel
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.models.qe_models.QEModel.__init__
```

````{py:method} load_model(model_name: str) -> filters.models.qe_models.QEModel
:canonical: filters.models.qe_models.QEModel.load_model
:abstractmethod:
:classmethod:

```{autodoc2-docstring} filters.models.qe_models.QEModel.load_model
```

````

````{py:method} predict(**kwargs) -> list[float]
:canonical: filters.models.qe_models.QEModel.predict
:abstractmethod:

```{autodoc2-docstring} filters.models.qe_models.QEModel.predict
```

````

````{py:method} wrap_qe_input(src: str, tgt: str, reverse: bool = False) -> list[str]
:canonical: filters.models.qe_models.QEModel.wrap_qe_input
:abstractmethod:
:staticmethod:

```{autodoc2-docstring} filters.models.qe_models.QEModel.wrap_qe_input
```

````

`````

````{py:data} comet
:canonical: filters.models.qe_models.comet
:value: >
   'safe_import(...)'

```{autodoc2-docstring} filters.models.qe_models.comet
```

````

````{py:data} pymarian
:canonical: filters.models.qe_models.pymarian
:value: >
   'safe_import(...)'

```{autodoc2-docstring} filters.models.qe_models.pymarian
```

````
