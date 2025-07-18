# {py:mod}`modifiers.llm_pii_modifier`

```{py:module} modifiers.llm_pii_modifier
```

```{autodoc2-docstring} modifiers.llm_pii_modifier
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LLMInference <modifiers.llm_pii_modifier.LLMInference>`
  - ```{autodoc2-docstring} modifiers.llm_pii_modifier.LLMInference
    :summary:
    ```
* - {py:obj}`LLMPiiModifier <modifiers.llm_pii_modifier.LLMPiiModifier>`
  - ```{autodoc2-docstring} modifiers.llm_pii_modifier.LLMPiiModifier
    :summary:
    ```
````

### API

`````{py:class} LLMInference(base_url: str, api_key: str | None, model: str, system_prompt: str)
:canonical: modifiers.llm_pii_modifier.LLMInference

```{autodoc2-docstring} modifiers.llm_pii_modifier.LLMInference
```

```{rubric} Initialization
```

```{autodoc2-docstring} modifiers.llm_pii_modifier.LLMInference.__init__
```

````{py:method} infer(text: str) -> list[dict[str, str]]
:canonical: modifiers.llm_pii_modifier.LLMInference.infer

```{autodoc2-docstring} modifiers.llm_pii_modifier.LLMInference.infer
```

````

`````

`````{py:class} LLMPiiModifier(base_url: str, api_key: str | None = None, model: str = 'meta/llama-3.1-70b-instruct', system_prompt: str | None = None, pii_labels: list[str] | None = None, language: str = 'en')
:canonical: modifiers.llm_pii_modifier.LLMPiiModifier

Bases: {py:obj}`nemo_curator.modifiers.DocumentModifier`

```{autodoc2-docstring} modifiers.llm_pii_modifier.LLMPiiModifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} modifiers.llm_pii_modifier.LLMPiiModifier.__init__
```

````{py:method} load_inferer() -> modifiers.llm_pii_modifier.LLMInference
:canonical: modifiers.llm_pii_modifier.LLMPiiModifier.load_inferer

```{autodoc2-docstring} modifiers.llm_pii_modifier.LLMPiiModifier.load_inferer
```

````

````{py:method} modify_document(text: str) -> str
:canonical: modifiers.llm_pii_modifier.LLMPiiModifier.modify_document

```{autodoc2-docstring} modifiers.llm_pii_modifier.LLMPiiModifier.modify_document
```

````

`````
