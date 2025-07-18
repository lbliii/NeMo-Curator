# {py:mod}`synthetic.generator`

```{py:module} synthetic.generator
```

```{autodoc2-docstring} synthetic.generator
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SyntheticDataGenerator <synthetic.generator.SyntheticDataGenerator>`
  - ```{autodoc2-docstring} synthetic.generator.SyntheticDataGenerator
    :summary:
    ```
````

### API

`````{py:class} SyntheticDataGenerator()
:canonical: synthetic.generator.SyntheticDataGenerator

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} synthetic.generator.SyntheticDataGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} synthetic.generator.SyntheticDataGenerator.__init__
```

````{py:method} generate(llm_prompt: str | list[str]) -> str | list[str]
:canonical: synthetic.generator.SyntheticDataGenerator.generate
:abstractmethod:

```{autodoc2-docstring} synthetic.generator.SyntheticDataGenerator.generate
```

````

````{py:method} parse_response(llm_response: str | list[str]) -> Any
:canonical: synthetic.generator.SyntheticDataGenerator.parse_response
:abstractmethod:

```{autodoc2-docstring} synthetic.generator.SyntheticDataGenerator.parse_response
```

````

`````
