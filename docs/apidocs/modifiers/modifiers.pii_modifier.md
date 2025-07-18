# {py:mod}`modifiers.pii_modifier`

```{py:module} modifiers.pii_modifier
```

```{autodoc2-docstring} modifiers.pii_modifier
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PiiModifier <modifiers.pii_modifier.PiiModifier>`
  - ```{autodoc2-docstring} modifiers.pii_modifier.PiiModifier
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEFAULT_BATCH_SIZE <modifiers.pii_modifier.DEFAULT_BATCH_SIZE>`
  - ```{autodoc2-docstring} modifiers.pii_modifier.DEFAULT_BATCH_SIZE
    :summary:
    ```
````

### API

````{py:data} DEFAULT_BATCH_SIZE
:canonical: modifiers.pii_modifier.DEFAULT_BATCH_SIZE
:value: >
   2000

```{autodoc2-docstring} modifiers.pii_modifier.DEFAULT_BATCH_SIZE
```

````

`````{py:class} PiiModifier(language: str = DEFAULT_LANGUAGE, supported_entities: list[str] | None = None, anonymize_action: str = 'redact', batch_size: int = DEFAULT_BATCH_SIZE, device: str = 'gpu', **kwargs)
:canonical: modifiers.pii_modifier.PiiModifier

Bases: {py:obj}`nemo_curator.modifiers.DocumentModifier`

```{autodoc2-docstring} modifiers.pii_modifier.PiiModifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} modifiers.pii_modifier.PiiModifier.__init__
```

````{py:method} load_deidentifier() -> nemo_curator.pii.algorithm.PiiDeidentifier
:canonical: modifiers.pii_modifier.PiiModifier.load_deidentifier

```{autodoc2-docstring} modifiers.pii_modifier.PiiModifier.load_deidentifier
```

````

````{py:method} modify_document(text: pandas.Series, partition_info: dict | None = None) -> pandas.Series
:canonical: modifiers.pii_modifier.PiiModifier.modify_document

```{autodoc2-docstring} modifiers.pii_modifier.PiiModifier.modify_document
```

````

`````
