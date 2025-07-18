# {py:mod}`modifiers.doc_modifier`

```{py:module} modifiers.doc_modifier
```

```{autodoc2-docstring} modifiers.doc_modifier
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DocumentModifier <modifiers.doc_modifier.DocumentModifier>`
  - ```{autodoc2-docstring} modifiers.doc_modifier.DocumentModifier
    :summary:
    ```
````

### API

`````{py:class} DocumentModifier()
:canonical: modifiers.doc_modifier.DocumentModifier

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} modifiers.doc_modifier.DocumentModifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} modifiers.doc_modifier.DocumentModifier.__init__
```

````{py:property} backend
:canonical: modifiers.doc_modifier.DocumentModifier.backend
:type: typing.Literal[pandas, cudf, any]

```{autodoc2-docstring} modifiers.doc_modifier.DocumentModifier.backend
```

````

````{py:method} modify_document(text: str) -> str
:canonical: modifiers.doc_modifier.DocumentModifier.modify_document
:abstractmethod:

```{autodoc2-docstring} modifiers.doc_modifier.DocumentModifier.modify_document
```

````

`````
