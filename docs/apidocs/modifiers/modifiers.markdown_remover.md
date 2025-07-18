# {py:mod}`modifiers.markdown_remover`

```{py:module} modifiers.markdown_remover
```

```{autodoc2-docstring} modifiers.markdown_remover
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MarkdownRemover <modifiers.markdown_remover.MarkdownRemover>`
  - ```{autodoc2-docstring} modifiers.markdown_remover.MarkdownRemover
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MARKDOWN_BOLD_REGEX <modifiers.markdown_remover.MARKDOWN_BOLD_REGEX>`
  - ```{autodoc2-docstring} modifiers.markdown_remover.MARKDOWN_BOLD_REGEX
    :summary:
    ```
* - {py:obj}`MARKDOWN_ITALIC_REGEX <modifiers.markdown_remover.MARKDOWN_ITALIC_REGEX>`
  - ```{autodoc2-docstring} modifiers.markdown_remover.MARKDOWN_ITALIC_REGEX
    :summary:
    ```
* - {py:obj}`MARKDOWN_LINK_REGEX <modifiers.markdown_remover.MARKDOWN_LINK_REGEX>`
  - ```{autodoc2-docstring} modifiers.markdown_remover.MARKDOWN_LINK_REGEX
    :summary:
    ```
* - {py:obj}`MARKDOWN_UNDERLINE_REGEX <modifiers.markdown_remover.MARKDOWN_UNDERLINE_REGEX>`
  - ```{autodoc2-docstring} modifiers.markdown_remover.MARKDOWN_UNDERLINE_REGEX
    :summary:
    ```
````

### API

````{py:data} MARKDOWN_BOLD_REGEX
:canonical: modifiers.markdown_remover.MARKDOWN_BOLD_REGEX
:value: >
   '\\*\\*(.*?)\\*\\*'

```{autodoc2-docstring} modifiers.markdown_remover.MARKDOWN_BOLD_REGEX
```

````

````{py:data} MARKDOWN_ITALIC_REGEX
:canonical: modifiers.markdown_remover.MARKDOWN_ITALIC_REGEX
:value: >
   '\\*(.*?)\\*'

```{autodoc2-docstring} modifiers.markdown_remover.MARKDOWN_ITALIC_REGEX
```

````

````{py:data} MARKDOWN_LINK_REGEX
:canonical: modifiers.markdown_remover.MARKDOWN_LINK_REGEX
:value: >
   '\\[.*?\\]\\((.*?)\\)'

```{autodoc2-docstring} modifiers.markdown_remover.MARKDOWN_LINK_REGEX
```

````

````{py:data} MARKDOWN_UNDERLINE_REGEX
:canonical: modifiers.markdown_remover.MARKDOWN_UNDERLINE_REGEX
:value: >
   '_(.*?)_'

```{autodoc2-docstring} modifiers.markdown_remover.MARKDOWN_UNDERLINE_REGEX
```

````

`````{py:class} MarkdownRemover()
:canonical: modifiers.markdown_remover.MarkdownRemover

Bases: {py:obj}`nemo_curator.modifiers.DocumentModifier`

```{autodoc2-docstring} modifiers.markdown_remover.MarkdownRemover
```

```{rubric} Initialization
```

```{autodoc2-docstring} modifiers.markdown_remover.MarkdownRemover.__init__
```

````{py:method} modify_document(text: str) -> str
:canonical: modifiers.markdown_remover.MarkdownRemover.modify_document

```{autodoc2-docstring} modifiers.markdown_remover.MarkdownRemover.modify_document
```

````

`````
