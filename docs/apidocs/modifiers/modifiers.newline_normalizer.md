# {py:mod}`modifiers.newline_normalizer`

```{py:module} modifiers.newline_normalizer
```

```{autodoc2-docstring} modifiers.newline_normalizer
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NewlineNormalizer <modifiers.newline_normalizer.NewlineNormalizer>`
  - ```{autodoc2-docstring} modifiers.newline_normalizer.NewlineNormalizer
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`THREE_OR_MORE_NEWLINES_REGEX <modifiers.newline_normalizer.THREE_OR_MORE_NEWLINES_REGEX>`
  - ```{autodoc2-docstring} modifiers.newline_normalizer.THREE_OR_MORE_NEWLINES_REGEX
    :summary:
    ```
* - {py:obj}`THREE_OR_MORE_WINDOWS_NEWLINES_REGEX <modifiers.newline_normalizer.THREE_OR_MORE_WINDOWS_NEWLINES_REGEX>`
  - ```{autodoc2-docstring} modifiers.newline_normalizer.THREE_OR_MORE_WINDOWS_NEWLINES_REGEX
    :summary:
    ```
````

### API

`````{py:class} NewlineNormalizer()
:canonical: modifiers.newline_normalizer.NewlineNormalizer

Bases: {py:obj}`nemo_curator.modifiers.DocumentModifier`

```{autodoc2-docstring} modifiers.newline_normalizer.NewlineNormalizer
```

```{rubric} Initialization
```

```{autodoc2-docstring} modifiers.newline_normalizer.NewlineNormalizer.__init__
```

````{py:method} modify_document(text: str) -> str
:canonical: modifiers.newline_normalizer.NewlineNormalizer.modify_document

```{autodoc2-docstring} modifiers.newline_normalizer.NewlineNormalizer.modify_document
```

````

`````

````{py:data} THREE_OR_MORE_NEWLINES_REGEX
:canonical: modifiers.newline_normalizer.THREE_OR_MORE_NEWLINES_REGEX
:value: >
   'compile(...)'

```{autodoc2-docstring} modifiers.newline_normalizer.THREE_OR_MORE_NEWLINES_REGEX
```

````

````{py:data} THREE_OR_MORE_WINDOWS_NEWLINES_REGEX
:canonical: modifiers.newline_normalizer.THREE_OR_MORE_WINDOWS_NEWLINES_REGEX
:value: >
   'compile(...)'

```{autodoc2-docstring} modifiers.newline_normalizer.THREE_OR_MORE_WINDOWS_NEWLINES_REGEX
```

````
