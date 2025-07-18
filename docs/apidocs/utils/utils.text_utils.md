# {py:mod}`utils.text_utils`

```{py:module} utils.text_utils
```

```{autodoc2-docstring} utils.text_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_comments <utils.text_utils.get_comments>`
  - ```{autodoc2-docstring} utils.text_utils.get_comments
    :summary:
    ```
* - {py:obj}`get_comments_and_docstring <utils.text_utils.get_comments_and_docstring>`
  - ```{autodoc2-docstring} utils.text_utils.get_comments_and_docstring
    :summary:
    ```
* - {py:obj}`get_docstrings <utils.text_utils.get_docstrings>`
  - ```{autodoc2-docstring} utils.text_utils.get_docstrings
    :summary:
    ```
* - {py:obj}`get_ngrams <utils.text_utils.get_ngrams>`
  - ```{autodoc2-docstring} utils.text_utils.get_ngrams
    :summary:
    ```
* - {py:obj}`get_paragraphs <utils.text_utils.get_paragraphs>`
  - ```{autodoc2-docstring} utils.text_utils.get_paragraphs
    :summary:
    ```
* - {py:obj}`get_sentences <utils.text_utils.get_sentences>`
  - ```{autodoc2-docstring} utils.text_utils.get_sentences
    :summary:
    ```
* - {py:obj}`get_word_splitter <utils.text_utils.get_word_splitter>`
  - ```{autodoc2-docstring} utils.text_utils.get_word_splitter
    :summary:
    ```
* - {py:obj}`get_words <utils.text_utils.get_words>`
  - ```{autodoc2-docstring} utils.text_utils.get_words
    :summary:
    ```
* - {py:obj}`is_paragraph_indices_in_top_or_bottom_only <utils.text_utils.is_paragraph_indices_in_top_or_bottom_only>`
  - ```{autodoc2-docstring} utils.text_utils.is_paragraph_indices_in_top_or_bottom_only
    :summary:
    ```
* - {py:obj}`parse_docstrings <utils.text_utils.parse_docstrings>`
  - ```{autodoc2-docstring} utils.text_utils.parse_docstrings
    :summary:
    ```
* - {py:obj}`remove_punctuation <utils.text_utils.remove_punctuation>`
  - ```{autodoc2-docstring} utils.text_utils.remove_punctuation
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NODE_TYPES <utils.text_utils.NODE_TYPES>`
  - ```{autodoc2-docstring} utils.text_utils.NODE_TYPES
    :summary:
    ```
````

### API

````{py:data} NODE_TYPES
:canonical: utils.text_utils.NODE_TYPES
:value: >
   None

```{autodoc2-docstring} utils.text_utils.NODE_TYPES
```

````

````{py:function} get_comments(s: str, clean: bool = False) -> str
:canonical: utils.text_utils.get_comments

```{autodoc2-docstring} utils.text_utils.get_comments
```
````

````{py:function} get_comments_and_docstring(source: str, comments: bool = True, clean_comments: bool = False) -> tuple[str, str]
:canonical: utils.text_utils.get_comments_and_docstring

```{autodoc2-docstring} utils.text_utils.get_comments_and_docstring
```
````

````{py:function} get_docstrings(source: str, module: str = '<string>') -> list[str]
:canonical: utils.text_utils.get_docstrings

```{autodoc2-docstring} utils.text_utils.get_docstrings
```
````

````{py:function} get_ngrams(input_list: list[str], n: int) -> list[tuple[str, ...]]
:canonical: utils.text_utils.get_ngrams

```{autodoc2-docstring} utils.text_utils.get_ngrams
```
````

````{py:function} get_paragraphs(document: str) -> list[str]
:canonical: utils.text_utils.get_paragraphs

```{autodoc2-docstring} utils.text_utils.get_paragraphs
```
````

````{py:function} get_sentences(document: str) -> list[str]
:canonical: utils.text_utils.get_sentences

```{autodoc2-docstring} utils.text_utils.get_sentences
```
````

````{py:function} get_word_splitter(language: str) -> collections.abc.Callable[[str], list[str]]
:canonical: utils.text_utils.get_word_splitter

```{autodoc2-docstring} utils.text_utils.get_word_splitter
```
````

````{py:function} get_words(text: str) -> tuple[list[str], list[int]]
:canonical: utils.text_utils.get_words

```{autodoc2-docstring} utils.text_utils.get_words
```
````

````{py:function} is_paragraph_indices_in_top_or_bottom_only(boilerplate_paragraph_indices: list[int], num_paragraphs: int) -> bool
:canonical: utils.text_utils.is_paragraph_indices_in_top_or_bottom_only

```{autodoc2-docstring} utils.text_utils.is_paragraph_indices_in_top_or_bottom_only
```
````

````{py:function} parse_docstrings(source: str) -> list[tuple[ast.AST, str | None, str]]
:canonical: utils.text_utils.parse_docstrings

```{autodoc2-docstring} utils.text_utils.parse_docstrings
```
````

````{py:function} remove_punctuation(str_in: str) -> str
:canonical: utils.text_utils.remove_punctuation

```{autodoc2-docstring} utils.text_utils.remove_punctuation
```
````
