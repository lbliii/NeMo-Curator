# {py:mod}`synthetic.async_nemotron`

```{py:module} synthetic.async_nemotron
```

```{autodoc2-docstring} synthetic.async_nemotron
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AsyncNemotronGenerator <synthetic.async_nemotron.AsyncNemotronGenerator>`
  - ```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator
    :summary:
    ```
````

### API

`````{py:class} AsyncNemotronGenerator(llm_client: nemo_curator.services.model_client.AsyncLLMClient, logger: logging.LoggerAdapter | str = './', max_concurrent_requests: int | None = None)
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.__init__
```

````{py:method} classify_math_entity(entity: str, model: str, prompt_template: str = DEFAULT_MATH_CLASSIFICATION_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.classify_math_entity
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.classify_math_entity
```

````

````{py:method} classify_python_entity(entity: str, model: str, prompt_template: str = DEFAULT_PYTHON_CLASSIFICATION_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.classify_python_entity
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.classify_python_entity
```

````

````{py:method} convert_response_to_yaml_list(llm_response: str, model: str, prompt_template: str = DEFAULT_YAML_CONVERSION_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.convert_response_to_yaml_list
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.convert_response_to_yaml_list
```

````

````{py:method} generate_closed_qa_instructions(document: str, n_openlines: str | int, model: str, prompt_template: str = DEFAULT_CLOSED_QA_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_closed_qa_instructions
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_closed_qa_instructions
```

````

````{py:method} generate_dialogue(openline: str, user_model: str, assistant_model: str, n_user_turns: int = 3, prompt_template: str = DIALOGUE_NORMAL_USER_TURN_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, user_model_kwargs: dict | None = None, assistant_model_kwargs: dict | None = None) -> list[dict]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_dialogue
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_dialogue
```

````

````{py:method} generate_macro_topics(n_macro_topics: int | str, model: str, prompt_template: str = DEFAULT_MACRO_TOPICS_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_macro_topics
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_macro_topics
```

````

````{py:method} generate_math_macro_topics(n_macro_topics: int | str, school_level: str, model: str, prompt_template: str = DEFAULT_MATH_MACRO_TOPICS_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_math_macro_topics
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_math_macro_topics
```

````

````{py:method} generate_math_problem(topic: str, n_openlines: str | int, model: str, prompt_template: str = MATH_PROBLEM_GENERAL_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_math_problem
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_math_problem
```

````

````{py:method} generate_math_subtopics(macro_topic: str, n_subtopics: int | str, model: str, prompt_template: str = DEFAULT_MATH_SUBTOPICS_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_math_subtopics
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_math_subtopics
```

````

````{py:method} generate_open_qa_from_topic(topic: str, n_openlines: str | int, model: str, prompt_template: str = DEFAULT_OPEN_QA_FROM_TOPICS_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_open_qa_from_topic
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_open_qa_from_topic
```

````

````{py:method} generate_python_macro_topics(n_macro_topics: int | str, model: str, prompt_template: str = DEFAULT_PYTHON_MACRO_TOPICS_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_python_macro_topics
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_python_macro_topics
```

````

````{py:method} generate_python_problem(topic: str, n_openlines: str | int, model: str, language: str = 'Python', prompt_template: str = PYTHON_PROBLEM_BEGINNER_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_python_problem
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_python_problem
```

````

````{py:method} generate_python_subtopics(macro_topic: str, n_subtopics: int | str, model: str, prompt_template: str = DEFAULT_PYTHON_SUBTOPICS_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_python_subtopics
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_python_subtopics
```

````

````{py:method} generate_subtopics(macro_topic: str, n_subtopics: int | str, model: str, prompt_template: str = DEFAULT_SUBTOPICS_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_subtopics
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_subtopics
```

````

````{py:method} generate_two_turn_prompt(openline: str, user_model: str, assistant_model: str, prompt_template: str = DIALOGUE_NORMAL_USER_TURN_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, user_model_kwargs: dict | None = None, assistant_model_kwargs: dict | None = None) -> list[dict]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_two_turn_prompt
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_two_turn_prompt
```

````

````{py:method} generate_writing_tasks(topic: str, text_material_type: str, n_openlines: str | int, model: str, prompt_template: str = DEFAULT_WRITING_TASK_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.generate_writing_tasks
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.generate_writing_tasks
```

````

````{py:method} revise_open_qa(openline: str, n_revisions: str | int, model: str, prompt_template: str = DEFAULT_REVISE_OPEN_QA_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.revise_open_qa
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.revise_open_qa
```

````

````{py:method} revise_writing_tasks(openline: str, n_revisions: str | int, model: str, prompt_template: str = DEFAULT_REVISE_WRITING_TASK_PROMPT_TEMPLATE, prompt_kwargs: dict | None = None, model_kwargs: dict | None = None) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.revise_writing_tasks
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.revise_writing_tasks
```

````

````{py:method} run_closed_qa_pipeline(documents: list[str], n_openlines: str | int, model: str, closed_qa_prompt_template: str = DEFAULT_CLOSED_QA_PROMPT_TEMPLATE, yaml_conversion_prompt_template: str = DEFAULT_YAML_CONVERSION_PROMPT_TEMPLATE, base_model_kwargs: dict | None = None, conversion_model_kwargs: dict | None = None, ignore_conversion_failure: bool = False, trim_topics_list: bool = True) -> list[tuple[int, str]]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.run_closed_qa_pipeline
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.run_closed_qa_pipeline
```

````

````{py:method} run_math_pipeline(n_macro_topics: str | int, school_level: str, n_subtopics: str | int, n_openlines: str | int, model: str, macro_topic_prompt_template: str = DEFAULT_MATH_MACRO_TOPICS_PROMPT_TEMPLATE, subtopic_prompt_template: str = DEFAULT_MATH_SUBTOPICS_PROMPT_TEMPLATE, math_problem_prompt_template: str = MATH_PROBLEM_GENERAL_PROMPT_TEMPLATE, yaml_conversion_prompt_template: str = DEFAULT_YAML_CONVERSION_PROMPT_TEMPLATE, base_model_kwargs: dict | None = None, conversion_model_kwargs: dict | None = None, additional_macro_topics: list[str] | None = None, additional_subtopics: list[str] | None = None, ignore_conversion_failure: bool = False, trim_topics_list: bool = True, combine_topics: bool = True) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.run_math_pipeline
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.run_math_pipeline
```

````

````{py:method} run_open_qa_pipeline(n_macro_topics: str | int, n_subtopics: str | int, n_openlines: str | int, n_revisions: str | int, model: str, macro_topic_prompt_template: str = DEFAULT_MACRO_TOPICS_PROMPT_TEMPLATE, subtopic_prompt_template: str = DEFAULT_SUBTOPICS_PROMPT_TEMPLATE, open_qa_from_topics_prompt_template: str = DEFAULT_OPEN_QA_FROM_TOPICS_PROMPT_TEMPLATE, revise_open_qa_prompt_template: str = DEFAULT_REVISE_OPEN_QA_PROMPT_TEMPLATE, yaml_conversion_prompt_template: str = DEFAULT_YAML_CONVERSION_PROMPT_TEMPLATE, base_model_kwargs: dict | None = None, conversion_model_kwargs: dict | None = None, additional_macro_topics: list[str] | None = None, additional_subtopics: list[str] | None = None, ignore_conversion_failure: bool = False, trim_topics_list: bool = True, combine_topics: bool = True) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.run_open_qa_pipeline
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.run_open_qa_pipeline
```

````

````{py:method} run_python_pipeline(n_macro_topics: str | int, n_subtopics: str | int, n_openlines: str | int, model: str, macro_topic_prompt_template: str = DEFAULT_PYTHON_MACRO_TOPICS_PROMPT_TEMPLATE, subtopic_prompt_template: str = DEFAULT_PYTHON_SUBTOPICS_PROMPT_TEMPLATE, python_problem_prompt_template: str = PYTHON_PROBLEM_BEGINNER_PROMPT_TEMPLATE, yaml_conversion_prompt_template: str = DEFAULT_YAML_CONVERSION_PROMPT_TEMPLATE, base_model_kwargs: dict | None = None, conversion_model_kwargs: dict | None = None, additional_macro_topics: list[str] | None = None, additional_subtopics: list[str] | None = None, ignore_conversion_failure: bool = False, trim_topics_list: bool = True, combine_topics: bool = True) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.run_python_pipeline
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.run_python_pipeline
```

````

````{py:method} run_writing_pipeline(topics: list[str], text_material_types: list[str], n_openlines: str | int, n_revisions: str | int, model: str, writing_task_prompt_template: str = DEFAULT_WRITING_TASK_PROMPT_TEMPLATE, revise_writing_task_prompt_template: str = DEFAULT_REVISE_WRITING_TASK_PROMPT_TEMPLATE, yaml_conversion_prompt_template: str = DEFAULT_YAML_CONVERSION_PROMPT_TEMPLATE, base_model_kwargs: dict | None = None, conversion_model_kwargs: dict | None = None, ignore_conversion_failure: bool = False, trim_topics_list: bool = True) -> list[str]
:canonical: synthetic.async_nemotron.AsyncNemotronGenerator.run_writing_pipeline
:async:

```{autodoc2-docstring} synthetic.async_nemotron.AsyncNemotronGenerator.run_writing_pipeline
```

````

`````
