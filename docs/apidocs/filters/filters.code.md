# {py:mod}`filters.code`

```{py:module} filters.code
```

```{autodoc2-docstring} filters.code
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AlphaFilter <filters.code.AlphaFilter>`
  - ```{autodoc2-docstring} filters.code.AlphaFilter
    :summary:
    ```
* - {py:obj}`GeneralCommentToCodeFilter <filters.code.GeneralCommentToCodeFilter>`
  - ```{autodoc2-docstring} filters.code.GeneralCommentToCodeFilter
    :summary:
    ```
* - {py:obj}`HTMLBoilerplateFilter <filters.code.HTMLBoilerplateFilter>`
  - ```{autodoc2-docstring} filters.code.HTMLBoilerplateFilter
    :summary:
    ```
* - {py:obj}`NumberOfLinesOfCodeFilter <filters.code.NumberOfLinesOfCodeFilter>`
  - ```{autodoc2-docstring} filters.code.NumberOfLinesOfCodeFilter
    :summary:
    ```
* - {py:obj}`PerExtensionFilter <filters.code.PerExtensionFilter>`
  - ```{autodoc2-docstring} filters.code.PerExtensionFilter
    :summary:
    ```
* - {py:obj}`PythonCommentToCodeFilter <filters.code.PythonCommentToCodeFilter>`
  - ```{autodoc2-docstring} filters.code.PythonCommentToCodeFilter
    :summary:
    ```
* - {py:obj}`TokenizerFertilityFilter <filters.code.TokenizerFertilityFilter>`
  - ```{autodoc2-docstring} filters.code.TokenizerFertilityFilter
    :summary:
    ```
* - {py:obj}`XMLHeaderFilter <filters.code.XMLHeaderFilter>`
  - ```{autodoc2-docstring} filters.code.XMLHeaderFilter
    :summary:
    ```
````

### API

`````{py:class} AlphaFilter(min_alpha_ratio: float = 0.25)
:canonical: filters.code.AlphaFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.code.AlphaFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.code.AlphaFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.code.AlphaFilter.keep_document

```{autodoc2-docstring} filters.code.AlphaFilter.keep_document
```

````

````{py:method} score_document(source: str) -> float
:canonical: filters.code.AlphaFilter.score_document

```{autodoc2-docstring} filters.code.AlphaFilter.score_document
```

````

`````

`````{py:class} GeneralCommentToCodeFilter(language: str, min_comment_to_code_ratio: float = 0.01, max_comment_to_code_ratio: float = 0.85)
:canonical: filters.code.GeneralCommentToCodeFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.code.GeneralCommentToCodeFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.code.GeneralCommentToCodeFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.code.GeneralCommentToCodeFilter.keep_document

```{autodoc2-docstring} filters.code.GeneralCommentToCodeFilter.keep_document
```

````

````{py:method} score_document(source: str) -> float
:canonical: filters.code.GeneralCommentToCodeFilter.score_document

```{autodoc2-docstring} filters.code.GeneralCommentToCodeFilter.score_document
```

````

`````

`````{py:class} HTMLBoilerplateFilter(min_lang_content_ratio: float = 0.2, min_lang_content_num_chars: int = 100)
:canonical: filters.code.HTMLBoilerplateFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.code.HTMLBoilerplateFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.code.HTMLBoilerplateFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.code.HTMLBoilerplateFilter.keep_document

```{autodoc2-docstring} filters.code.HTMLBoilerplateFilter.keep_document
```

````

````{py:method} score_document(source: str) -> float | None
:canonical: filters.code.HTMLBoilerplateFilter.score_document

```{autodoc2-docstring} filters.code.HTMLBoilerplateFilter.score_document
```

````

`````

`````{py:class} NumberOfLinesOfCodeFilter(min_lines: int = 10, max_lines: int = 20000)
:canonical: filters.code.NumberOfLinesOfCodeFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.code.NumberOfLinesOfCodeFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.code.NumberOfLinesOfCodeFilter.__init__
```

````{py:method} keep_document(score: int) -> bool
:canonical: filters.code.NumberOfLinesOfCodeFilter.keep_document

```{autodoc2-docstring} filters.code.NumberOfLinesOfCodeFilter.keep_document
```

````

````{py:method} score_document(source: str) -> int
:canonical: filters.code.NumberOfLinesOfCodeFilter.score_document

```{autodoc2-docstring} filters.code.NumberOfLinesOfCodeFilter.score_document
```

````

`````

`````{py:class} PerExtensionFilter(lang: str, extension: str, metadata_file: str = 'code_meta.csv')
:canonical: filters.code.PerExtensionFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.code.PerExtensionFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.code.PerExtensionFilter.__init__
```

````{py:method} keep_document(score: float | None) -> bool
:canonical: filters.code.PerExtensionFilter.keep_document

```{autodoc2-docstring} filters.code.PerExtensionFilter.keep_document
```

````

````{py:method} score_document(source: str) -> float
:canonical: filters.code.PerExtensionFilter.score_document

```{autodoc2-docstring} filters.code.PerExtensionFilter.score_document
```

````

`````

`````{py:class} PythonCommentToCodeFilter(min_comment_to_code_ratio: float = 0.01, max_comment_to_code_ratio: float = 0.85)
:canonical: filters.code.PythonCommentToCodeFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.code.PythonCommentToCodeFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.code.PythonCommentToCodeFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.code.PythonCommentToCodeFilter.keep_document

```{autodoc2-docstring} filters.code.PythonCommentToCodeFilter.keep_document
```

````

````{py:method} score_document(source: str) -> float
:canonical: filters.code.PythonCommentToCodeFilter.score_document

```{autodoc2-docstring} filters.code.PythonCommentToCodeFilter.score_document
```

````

`````

`````{py:class} TokenizerFertilityFilter(path_to_tokenizer: str | None = None, min_char_to_token_ratio: float = 2.5)
:canonical: filters.code.TokenizerFertilityFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.code.TokenizerFertilityFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.code.TokenizerFertilityFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.code.TokenizerFertilityFilter.keep_document

```{autodoc2-docstring} filters.code.TokenizerFertilityFilter.keep_document
```

````

````{py:method} score_document(source: str) -> float
:canonical: filters.code.TokenizerFertilityFilter.score_document

```{autodoc2-docstring} filters.code.TokenizerFertilityFilter.score_document
```

````

`````

`````{py:class} XMLHeaderFilter(char_prefix_search_length: int = 100)
:canonical: filters.code.XMLHeaderFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.code.XMLHeaderFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.code.XMLHeaderFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.code.XMLHeaderFilter.keep_document

```{autodoc2-docstring} filters.code.XMLHeaderFilter.keep_document
```

````

````{py:method} score_document(source: str) -> float
:canonical: filters.code.XMLHeaderFilter.score_document

```{autodoc2-docstring} filters.code.XMLHeaderFilter.score_document
```

````

`````
