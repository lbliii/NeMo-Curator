# {py:mod}`filters.heuristic_filter`

```{py:module} filters.heuristic_filter
```

```{autodoc2-docstring} filters.heuristic_filter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BoilerPlateStringFilter <filters.heuristic_filter.BoilerPlateStringFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.BoilerPlateStringFilter
    :summary:
    ```
* - {py:obj}`BulletsFilter <filters.heuristic_filter.BulletsFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.BulletsFilter
    :summary:
    ```
* - {py:obj}`CommonEnglishWordsFilter <filters.heuristic_filter.CommonEnglishWordsFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.CommonEnglishWordsFilter
    :summary:
    ```
* - {py:obj}`EllipsisFilter <filters.heuristic_filter.EllipsisFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.EllipsisFilter
    :summary:
    ```
* - {py:obj}`HistogramFilter <filters.heuristic_filter.HistogramFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.HistogramFilter
    :summary:
    ```
* - {py:obj}`LengthRatioFilter <filters.heuristic_filter.LengthRatioFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.LengthRatioFilter
    :summary:
    ```
* - {py:obj}`LongWordFilter <filters.heuristic_filter.LongWordFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.LongWordFilter
    :summary:
    ```
* - {py:obj}`MeanWordLengthFilter <filters.heuristic_filter.MeanWordLengthFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.MeanWordLengthFilter
    :summary:
    ```
* - {py:obj}`NonAlphaNumericFilter <filters.heuristic_filter.NonAlphaNumericFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.NonAlphaNumericFilter
    :summary:
    ```
* - {py:obj}`NumbersFilter <filters.heuristic_filter.NumbersFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.NumbersFilter
    :summary:
    ```
* - {py:obj}`ParenthesesFilter <filters.heuristic_filter.ParenthesesFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.ParenthesesFilter
    :summary:
    ```
* - {py:obj}`PornographicUrlsFilter <filters.heuristic_filter.PornographicUrlsFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.PornographicUrlsFilter
    :summary:
    ```
* - {py:obj}`PunctuationFilter <filters.heuristic_filter.PunctuationFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.PunctuationFilter
    :summary:
    ```
* - {py:obj}`RepeatedLinesByCharFilter <filters.heuristic_filter.RepeatedLinesByCharFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesByCharFilter
    :summary:
    ```
* - {py:obj}`RepeatedLinesFilter <filters.heuristic_filter.RepeatedLinesFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesFilter
    :summary:
    ```
* - {py:obj}`RepeatedParagraphsByCharFilter <filters.heuristic_filter.RepeatedParagraphsByCharFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsByCharFilter
    :summary:
    ```
* - {py:obj}`RepeatedParagraphsFilter <filters.heuristic_filter.RepeatedParagraphsFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsFilter
    :summary:
    ```
* - {py:obj}`RepeatingDuplicateNGramsFilter <filters.heuristic_filter.RepeatingDuplicateNGramsFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.RepeatingDuplicateNGramsFilter
    :summary:
    ```
* - {py:obj}`RepeatingTopNGramsFilter <filters.heuristic_filter.RepeatingTopNGramsFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.RepeatingTopNGramsFilter
    :summary:
    ```
* - {py:obj}`SubstringFilter <filters.heuristic_filter.SubstringFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.SubstringFilter
    :summary:
    ```
* - {py:obj}`SymbolsToWordsFilter <filters.heuristic_filter.SymbolsToWordsFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.SymbolsToWordsFilter
    :summary:
    ```
* - {py:obj}`TokenCountFilter <filters.heuristic_filter.TokenCountFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.TokenCountFilter
    :summary:
    ```
* - {py:obj}`UrlsFilter <filters.heuristic_filter.UrlsFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.UrlsFilter
    :summary:
    ```
* - {py:obj}`WhiteSpaceFilter <filters.heuristic_filter.WhiteSpaceFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.WhiteSpaceFilter
    :summary:
    ```
* - {py:obj}`WordCountFilter <filters.heuristic_filter.WordCountFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.WordCountFilter
    :summary:
    ```
* - {py:obj}`WordsWithoutAlphabetsFilter <filters.heuristic_filter.WordsWithoutAlphabetsFilter>`
  - ```{autodoc2-docstring} filters.heuristic_filter.WordsWithoutAlphabetsFilter
    :summary:
    ```
````

### API

`````{py:class} BoilerPlateStringFilter(remove_if_at_top_or_bottom: bool = True, max_boilerplate_string_ratio: float = 0.4)
:canonical: filters.heuristic_filter.BoilerPlateStringFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.BoilerPlateStringFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.BoilerPlateStringFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.BoilerPlateStringFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.BoilerPlateStringFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.BoilerPlateStringFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.BoilerPlateStringFilter.score_document
```

````

`````

`````{py:class} BulletsFilter(max_bullet_lines_ratio: float = 0.9)
:canonical: filters.heuristic_filter.BulletsFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.BulletsFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.BulletsFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.BulletsFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.BulletsFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.BulletsFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.BulletsFilter.score_document
```

````

`````

`````{py:class} CommonEnglishWordsFilter(min_num_common_words: int = 2, stop_at_false: bool = True)
:canonical: filters.heuristic_filter.CommonEnglishWordsFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.CommonEnglishWordsFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.CommonEnglishWordsFilter.__init__
```

````{py:method} keep_document(score: int) -> bool
:canonical: filters.heuristic_filter.CommonEnglishWordsFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.CommonEnglishWordsFilter.keep_document
```

````

````{py:method} score_document(text: str) -> int
:canonical: filters.heuristic_filter.CommonEnglishWordsFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.CommonEnglishWordsFilter.score_document
```

````

`````

`````{py:class} EllipsisFilter(max_num_lines_ending_with_ellipsis_ratio: float = 0.3)
:canonical: filters.heuristic_filter.EllipsisFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.EllipsisFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.EllipsisFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.EllipsisFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.EllipsisFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.EllipsisFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.EllipsisFilter.score_document
```

````

`````

`````{py:class} HistogramFilter(lang: str | None = 'en', threshold: float | None = 0.8, cache_dir: str | None = '', threshold_char: str | None = ']')
:canonical: filters.heuristic_filter.HistogramFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.HistogramFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.HistogramFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.HistogramFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.HistogramFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.HistogramFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.HistogramFilter.score_document
```

````

`````

`````{py:class} LengthRatioFilter(max_ratio: float = 3.0, src_lang: str = 'en', tgt_lang: str = 'en', **kwargs)
:canonical: filters.heuristic_filter.LengthRatioFilter

Bases: {py:obj}`nemo_curator.filters.bitext_filter.BitextFilter`

```{autodoc2-docstring} filters.heuristic_filter.LengthRatioFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.LengthRatioFilter.__init__
```

````{py:method} keep_bitext(score: float) -> bool
:canonical: filters.heuristic_filter.LengthRatioFilter.keep_bitext

```{autodoc2-docstring} filters.heuristic_filter.LengthRatioFilter.keep_bitext
```

````

````{py:method} score_bitext(src: str, tgt: str) -> float
:canonical: filters.heuristic_filter.LengthRatioFilter.score_bitext

```{autodoc2-docstring} filters.heuristic_filter.LengthRatioFilter.score_bitext
```

````

`````

`````{py:class} LongWordFilter(max_word_length: int = 1000, lang: str = 'en')
:canonical: filters.heuristic_filter.LongWordFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.LongWordFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.LongWordFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.LongWordFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.LongWordFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.LongWordFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.LongWordFilter.score_document
```

````

`````

`````{py:class} MeanWordLengthFilter(min_mean_word_length: int = 3, max_mean_word_length: int = 10, lang: str = 'en')
:canonical: filters.heuristic_filter.MeanWordLengthFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.MeanWordLengthFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.MeanWordLengthFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.MeanWordLengthFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.MeanWordLengthFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.MeanWordLengthFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.MeanWordLengthFilter.score_document
```

````

`````

`````{py:class} NonAlphaNumericFilter(max_non_alpha_numeric_to_text_ratio: float = 0.25)
:canonical: filters.heuristic_filter.NonAlphaNumericFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.NonAlphaNumericFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.NonAlphaNumericFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.NonAlphaNumericFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.NonAlphaNumericFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.NonAlphaNumericFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.NonAlphaNumericFilter.score_document
```

````

`````

`````{py:class} NumbersFilter(max_number_to_text_ratio: float = 0.15)
:canonical: filters.heuristic_filter.NumbersFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.NumbersFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.NumbersFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.NumbersFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.NumbersFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.NumbersFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.NumbersFilter.score_document
```

````

`````

`````{py:class} ParenthesesFilter(max_parentheses_ratio: float = 0.1)
:canonical: filters.heuristic_filter.ParenthesesFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.ParenthesesFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.ParenthesesFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.ParenthesesFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.ParenthesesFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.ParenthesesFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.ParenthesesFilter.score_document
```

````

`````

`````{py:class} PornographicUrlsFilter()
:canonical: filters.heuristic_filter.PornographicUrlsFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.PornographicUrlsFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.PornographicUrlsFilter.__init__
```

````{py:method} keep_document(score: int) -> bool
:canonical: filters.heuristic_filter.PornographicUrlsFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.PornographicUrlsFilter.keep_document
```

````

````{py:method} score_document(text: str) -> int
:canonical: filters.heuristic_filter.PornographicUrlsFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.PornographicUrlsFilter.score_document
```

````

`````

`````{py:class} PunctuationFilter(max_num_sentences_without_endmark_ratio: float = 0.85)
:canonical: filters.heuristic_filter.PunctuationFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.PunctuationFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.PunctuationFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.PunctuationFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.PunctuationFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.PunctuationFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.PunctuationFilter.score_document
```

````

`````

`````{py:class} RepeatedLinesByCharFilter(max_repeated_lines_char_ratio: float = 0.8)
:canonical: filters.heuristic_filter.RepeatedLinesByCharFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesByCharFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesByCharFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.RepeatedLinesByCharFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesByCharFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.RepeatedLinesByCharFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesByCharFilter.score_document
```

````

`````

`````{py:class} RepeatedLinesFilter(max_repeated_line_fraction: float = 0.7)
:canonical: filters.heuristic_filter.RepeatedLinesFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.RepeatedLinesFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.RepeatedLinesFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatedLinesFilter.score_document
```

````

`````

`````{py:class} RepeatedParagraphsByCharFilter(max_repeated_paragraphs_char_ratio: float = 0.8)
:canonical: filters.heuristic_filter.RepeatedParagraphsByCharFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsByCharFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsByCharFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.RepeatedParagraphsByCharFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsByCharFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.RepeatedParagraphsByCharFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsByCharFilter.score_document
```

````

`````

`````{py:class} RepeatedParagraphsFilter(max_repeated_paragraphs_ratio: float = 0.7)
:canonical: filters.heuristic_filter.RepeatedParagraphsFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.RepeatedParagraphsFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.RepeatedParagraphsFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatedParagraphsFilter.score_document
```

````

`````

`````{py:class} RepeatingDuplicateNGramsFilter(n: int = 2, max_repeating_duplicate_ngram_ratio: float = 0.2, lang: str = 'en')
:canonical: filters.heuristic_filter.RepeatingDuplicateNGramsFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.RepeatingDuplicateNGramsFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.RepeatingDuplicateNGramsFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.RepeatingDuplicateNGramsFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatingDuplicateNGramsFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.RepeatingDuplicateNGramsFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatingDuplicateNGramsFilter.score_document
```

````

`````

`````{py:class} RepeatingTopNGramsFilter(n: int = 2, max_repeating_ngram_ratio: float = 0.2, lang: str = 'en')
:canonical: filters.heuristic_filter.RepeatingTopNGramsFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.RepeatingTopNGramsFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.RepeatingTopNGramsFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.RepeatingTopNGramsFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatingTopNGramsFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.RepeatingTopNGramsFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.RepeatingTopNGramsFilter.score_document
```

````

`````

`````{py:class} SubstringFilter(substring: str, position: typing.Literal[prefix, suffix, any])
:canonical: filters.heuristic_filter.SubstringFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.SubstringFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.SubstringFilter.__init__
```

````{py:method} keep_document(score: int) -> bool
:canonical: filters.heuristic_filter.SubstringFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.SubstringFilter.keep_document
```

````

````{py:method} score_document(text: str) -> int
:canonical: filters.heuristic_filter.SubstringFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.SubstringFilter.score_document
```

````

`````

`````{py:class} SymbolsToWordsFilter(max_symbol_to_word_ratio: float = 0.1, lang: str = 'en')
:canonical: filters.heuristic_filter.SymbolsToWordsFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.SymbolsToWordsFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.SymbolsToWordsFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.SymbolsToWordsFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.SymbolsToWordsFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.SymbolsToWordsFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.SymbolsToWordsFilter.score_document
```

````

`````

`````{py:class} TokenCountFilter(tokenizer: transformers.AutoTokenizer, min_tokens: int = 0, max_tokens: int = float('inf'))
:canonical: filters.heuristic_filter.TokenCountFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.TokenCountFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.TokenCountFilter.__init__
```

````{py:method} keep_document(score: int) -> bool
:canonical: filters.heuristic_filter.TokenCountFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.TokenCountFilter.keep_document
```

````

````{py:method} score_document(text: str) -> int
:canonical: filters.heuristic_filter.TokenCountFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.TokenCountFilter.score_document
```

````

`````

`````{py:class} UrlsFilter(max_url_to_text_ratio: float = 0.2)
:canonical: filters.heuristic_filter.UrlsFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.UrlsFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.UrlsFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.UrlsFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.UrlsFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.UrlsFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.UrlsFilter.score_document
```

````

`````

`````{py:class} WhiteSpaceFilter(max_white_space_ratio: float = 0.25)
:canonical: filters.heuristic_filter.WhiteSpaceFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.WhiteSpaceFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.WhiteSpaceFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.WhiteSpaceFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.WhiteSpaceFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.WhiteSpaceFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.WhiteSpaceFilter.score_document
```

````

`````

`````{py:class} WordCountFilter(min_words: int = 50, max_words: int = 100000, lang: str = 'en')
:canonical: filters.heuristic_filter.WordCountFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.WordCountFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.WordCountFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.WordCountFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.WordCountFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.WordCountFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.WordCountFilter.score_document
```

````

`````

`````{py:class} WordsWithoutAlphabetsFilter(min_words_with_alphabets: float = 0.8, lang: str = 'en')
:canonical: filters.heuristic_filter.WordsWithoutAlphabetsFilter

Bases: {py:obj}`nemo_curator.filters.doc_filter.DocumentFilter`

```{autodoc2-docstring} filters.heuristic_filter.WordsWithoutAlphabetsFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} filters.heuristic_filter.WordsWithoutAlphabetsFilter.__init__
```

````{py:method} keep_document(score: float) -> bool
:canonical: filters.heuristic_filter.WordsWithoutAlphabetsFilter.keep_document

```{autodoc2-docstring} filters.heuristic_filter.WordsWithoutAlphabetsFilter.keep_document
```

````

````{py:method} score_document(text: str) -> float
:canonical: filters.heuristic_filter.WordsWithoutAlphabetsFilter.score_document

```{autodoc2-docstring} filters.heuristic_filter.WordsWithoutAlphabetsFilter.score_document
```

````

`````
