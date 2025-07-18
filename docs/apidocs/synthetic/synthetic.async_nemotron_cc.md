# {py:mod}`synthetic.async_nemotron_cc`

```{py:module} synthetic.async_nemotron_cc
```

```{autodoc2-docstring} synthetic.async_nemotron_cc
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AsyncNemotronCCGenerator <synthetic.async_nemotron_cc.AsyncNemotronCCGenerator>`
  - ```{autodoc2-docstring} synthetic.async_nemotron_cc.AsyncNemotronCCGenerator
    :summary:
    ```
````

### API

`````{py:class} AsyncNemotronCCGenerator(llm_client: nemo_curator.services.AsyncLLMClient)
:canonical: synthetic.async_nemotron_cc.AsyncNemotronCCGenerator

```{autodoc2-docstring} synthetic.async_nemotron_cc.AsyncNemotronCCGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.__init__
```

````{py:method} distill(document: str, model: str, prompt_template: str = DISTILL_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_DISTILL_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.distill
:async:

```{autodoc2-docstring} synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.distill
```

````

````{py:method} extract_knowledge(document: str, model: str, prompt_template: str = EXTRACT_KNOWLEDGE_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.extract_knowledge
:async:

```{autodoc2-docstring} synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.extract_knowledge
```

````

````{py:method} generate_diverse_qa(document: str, model: str, prompt_template: str = DIVERSE_QA_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.generate_diverse_qa
:async:

```{autodoc2-docstring} synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.generate_diverse_qa
```

````

````{py:method} generate_knowledge_list(document: str, model: str, prompt_template: str = KNOWLEDGE_LIST_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.generate_knowledge_list
:async:

```{autodoc2-docstring} synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.generate_knowledge_list
```

````

````{py:method} rewrite_to_wikipedia_style(document: str, model: str, prompt_template: str = WIKIPEDIA_REPHRASING_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.rewrite_to_wikipedia_style
:async:

```{autodoc2-docstring} synthetic.async_nemotron_cc.AsyncNemotronCCGenerator.rewrite_to_wikipedia_style
```

````

`````
