# {py:mod}`modifiers.async_llm_pii_modifier`

```{py:module} modifiers.async_llm_pii_modifier
```

```{autodoc2-docstring} modifiers.async_llm_pii_modifier
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AsyncLLMInference <modifiers.async_llm_pii_modifier.AsyncLLMInference>`
  - ```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMInference
    :summary:
    ```
* - {py:obj}`AsyncLLMPiiModifier <modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier>`
  - ```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier
    :summary:
    ```
````

### API

`````{py:class} AsyncLLMInference(base_url: str, api_key: str | None, model: str, system_prompt: str)
:canonical: modifiers.async_llm_pii_modifier.AsyncLLMInference

```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMInference
```

```{rubric} Initialization
```

```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMInference.__init__
```

````{py:method} infer(text: str) -> list[dict[str, str]]
:canonical: modifiers.async_llm_pii_modifier.AsyncLLMInference.infer
:async:

```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMInference.infer
```

````

`````

`````{py:class} AsyncLLMPiiModifier(base_url: str, api_key: str | None = None, model: str = 'meta/llama-3.1-70b-instruct', system_prompt: str | None = None, pii_labels: list[str] | None = None, language: str = 'en', max_concurrent_requests: int | None = None)
:canonical: modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier

Bases: {py:obj}`nemo_curator.modifiers.DocumentModifier`

```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier.__init__
```

````{py:method} batch_redact(text: pandas.Series, pii_entities_lists: list[list[dict[str, str]]]) -> pandas.Series
:canonical: modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier.batch_redact

```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier.batch_redact
```

````

````{py:method} call_inferer(text: pandas.Series, inferer: modifiers.async_llm_pii_modifier.AsyncLLMInference) -> list[str]
:canonical: modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier.call_inferer
:async:

```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier.call_inferer
```

````

````{py:method} load_inferer() -> modifiers.async_llm_pii_modifier.AsyncLLMInference
:canonical: modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier.load_inferer

```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier.load_inferer
```

````

````{py:method} modify_document(text: pandas.Series) -> pandas.Series
:canonical: modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier.modify_document

```{autodoc2-docstring} modifiers.async_llm_pii_modifier.AsyncLLMPiiModifier.modify_document
```

````

`````
