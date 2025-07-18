# {py:mod}`synthetic.nemotron_cc`

```{py:module} synthetic.nemotron_cc
```

```{autodoc2-docstring} synthetic.nemotron_cc
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NemotronCCDiverseQAPostprocessor <synthetic.nemotron_cc.NemotronCCDiverseQAPostprocessor>`
  - ```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCDiverseQAPostprocessor
    :summary:
    ```
* - {py:obj}`NemotronCCGenerator <synthetic.nemotron_cc.NemotronCCGenerator>`
  - ```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCGenerator
    :summary:
    ```
* - {py:obj}`NemotronCCKnowledgeListPostprocessor <synthetic.nemotron_cc.NemotronCCKnowledgeListPostprocessor>`
  - ```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCKnowledgeListPostprocessor
    :summary:
    ```
````

### API

`````{py:class} NemotronCCDiverseQAPostprocessor(tokenizer: transformers.AutoTokenizer | None = None, text_field: str = 'text', response_field: str = 'response', max_num_pairs: int = 1, prefix: str = 'Here are the questions and answers based on the provided text:')
:canonical: synthetic.nemotron_cc.NemotronCCDiverseQAPostprocessor

Bases: {py:obj}`nemo_curator.BaseModule`

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCDiverseQAPostprocessor
```

```{rubric} Initialization
```

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCDiverseQAPostprocessor.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: synthetic.nemotron_cc.NemotronCCDiverseQAPostprocessor.call

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCDiverseQAPostprocessor.call
```

````

`````

`````{py:class} NemotronCCGenerator(llm_client: nemo_curator.services.LLMClient)
:canonical: synthetic.nemotron_cc.NemotronCCGenerator

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCGenerator.__init__
```

````{py:method} distill(document: str, model: str, prompt_template: str = DISTILL_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_DISTILL_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.nemotron_cc.NemotronCCGenerator.distill

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCGenerator.distill
```

````

````{py:method} extract_knowledge(document: str, model: str, prompt_template: str = EXTRACT_KNOWLEDGE_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.nemotron_cc.NemotronCCGenerator.extract_knowledge

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCGenerator.extract_knowledge
```

````

````{py:method} generate_diverse_qa(document: str, model: str, prompt_template: str = DIVERSE_QA_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.nemotron_cc.NemotronCCGenerator.generate_diverse_qa

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCGenerator.generate_diverse_qa
```

````

````{py:method} generate_knowledge_list(document: str, model: str, prompt_template: str = KNOWLEDGE_LIST_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.nemotron_cc.NemotronCCGenerator.generate_knowledge_list

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCGenerator.generate_knowledge_list
```

````

````{py:method} rewrite_to_wikipedia_style(document: str, model: str, prompt_template: str = WIKIPEDIA_REPHRASING_PROMPT_TEMPLATE, system_prompt: str = NEMOTRON_CC_SYSTEM_PROMPT, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.nemotron_cc.NemotronCCGenerator.rewrite_to_wikipedia_style

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCGenerator.rewrite_to_wikipedia_style
```

````

`````

`````{py:class} NemotronCCKnowledgeListPostprocessor(text_field: str = 'text')
:canonical: synthetic.nemotron_cc.NemotronCCKnowledgeListPostprocessor

Bases: {py:obj}`nemo_curator.BaseModule`

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCKnowledgeListPostprocessor
```

```{rubric} Initialization
```

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCKnowledgeListPostprocessor.__init__
```

````{py:method} call(dataset: nemo_curator.datasets.DocumentDataset) -> nemo_curator.datasets.DocumentDataset
:canonical: synthetic.nemotron_cc.NemotronCCKnowledgeListPostprocessor.call

```{autodoc2-docstring} synthetic.nemotron_cc.NemotronCCKnowledgeListPostprocessor.call
```

````

`````
