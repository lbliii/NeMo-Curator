# {py:mod}`synthetic.mixtral`

```{py:module} synthetic.mixtral
```

```{autodoc2-docstring} synthetic.mixtral
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Mixtral8x7BFormatter <synthetic.mixtral.Mixtral8x7BFormatter>`
  - ```{autodoc2-docstring} synthetic.mixtral.Mixtral8x7BFormatter
    :summary:
    ```
````

### API

`````{py:class} Mixtral8x7BFormatter
:canonical: synthetic.mixtral.Mixtral8x7BFormatter

Bases: {py:obj}`nemo_curator.services.conversation_formatter.ConversationFormatter`

```{autodoc2-docstring} synthetic.mixtral.Mixtral8x7BFormatter
```

````{py:attribute} PROMPT_PREFIX
:canonical: synthetic.mixtral.Mixtral8x7BFormatter.PROMPT_PREFIX
:value: >
   '<s> [INST] \n'

```{autodoc2-docstring} synthetic.mixtral.Mixtral8x7BFormatter.PROMPT_PREFIX
```

````

````{py:method} format_conversation(conv: list[dict]) -> str
:canonical: synthetic.mixtral.Mixtral8x7BFormatter.format_conversation
:staticmethod:

```{autodoc2-docstring} synthetic.mixtral.Mixtral8x7BFormatter.format_conversation
```

````

`````
