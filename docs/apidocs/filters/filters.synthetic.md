# {py:mod}`filters.synthetic`

```{py:module} filters.synthetic
```

```{autodoc2-docstring} filters.synthetic
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AnswerabilityFilter <filters.synthetic.AnswerabilityFilter>`
  - ```{autodoc2-docstring} filters.synthetic.AnswerabilityFilter
    :summary:
    ```
* - {py:obj}`EasinessFilter <filters.synthetic.EasinessFilter>`
  - ```{autodoc2-docstring} filters.synthetic.EasinessFilter
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`create_client <filters.synthetic.create_client>`
  - ```{autodoc2-docstring} filters.synthetic.create_client
    :summary:
    ```
````

### API

`````{py:class} AnswerabilityFilter(base_url: str, api_key: str, model: str, answerability_system_prompt: str, answerability_user_prompt_template: str, num_criteria: int, text_fields: list[str] | None = None)
:canonical: filters.synthetic.AnswerabilityFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.synthetic.AnswerabilityFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.synthetic.AnswerabilityFilter.__init__
```

````{py:method} keep_document(scores: pandas.Series) -> pandas.Series
:canonical: filters.synthetic.AnswerabilityFilter.keep_document

```{autodoc2-docstring} filters.synthetic.AnswerabilityFilter.keep_document
```

````

````{py:method} score_document(df: pandas.DataFrame) -> pandas.Series
:canonical: filters.synthetic.AnswerabilityFilter.score_document

```{autodoc2-docstring} filters.synthetic.AnswerabilityFilter.score_document
```

````

`````

`````{py:class} EasinessFilter(base_url: str, api_key: str, model: str, percentile: float = 0.7, truncate: str = 'NONE', batch_size: int = 1, text_fields: list[str] | None = None)
:canonical: filters.synthetic.EasinessFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.synthetic.EasinessFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.synthetic.EasinessFilter.__init__
```

````{py:method} keep_document(scores: pandas.Series) -> pandas.Series
:canonical: filters.synthetic.EasinessFilter.keep_document

```{autodoc2-docstring} filters.synthetic.EasinessFilter.keep_document
```

````

````{py:method} score_document(df: pandas.DataFrame) -> pandas.Series
:canonical: filters.synthetic.EasinessFilter.score_document

```{autodoc2-docstring} filters.synthetic.EasinessFilter.score_document
```

````

`````

````{py:function} create_client(base_url: str, api_key: str) -> openai.OpenAI
:canonical: filters.synthetic.create_client

```{autodoc2-docstring} filters.synthetic.create_client
```
````
