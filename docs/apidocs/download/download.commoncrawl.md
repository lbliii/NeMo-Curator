# {py:mod}`download.commoncrawl`

```{py:module} download.commoncrawl
```

```{autodoc2-docstring} download.commoncrawl
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CommonCrawlWARCDownloader <download.commoncrawl.CommonCrawlWARCDownloader>`
  - ```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCDownloader
    :summary:
    ```
* - {py:obj}`CommonCrawlWARCDownloaderExtractOnly <download.commoncrawl.CommonCrawlWARCDownloaderExtractOnly>`
  - ```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCDownloaderExtractOnly
    :summary:
    ```
* - {py:obj}`CommonCrawlWARCExtractor <download.commoncrawl.CommonCrawlWARCExtractor>`
  - ```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCExtractor
    :summary:
    ```
* - {py:obj}`CommonCrawlWARCIterator <download.commoncrawl.CommonCrawlWARCIterator>`
  - ```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCIterator
    :summary:
    ```
* - {py:obj}`HTMLExtractorAlgorithm <download.commoncrawl.HTMLExtractorAlgorithm>`
  - ```{autodoc2-docstring} download.commoncrawl.HTMLExtractorAlgorithm
    :summary:
    ```
* - {py:obj}`JusTextExtractor <download.commoncrawl.JusTextExtractor>`
  - ```{autodoc2-docstring} download.commoncrawl.JusTextExtractor
    :summary:
    ```
* - {py:obj}`ResiliparseExtractor <download.commoncrawl.ResiliparseExtractor>`
  - ```{autodoc2-docstring} download.commoncrawl.ResiliparseExtractor
    :summary:
    ```
* - {py:obj}`TrafilaturaExtractor <download.commoncrawl.TrafilaturaExtractor>`
  - ```{autodoc2-docstring} download.commoncrawl.TrafilaturaExtractor
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`decode_html <download.commoncrawl.decode_html>`
  - ```{autodoc2-docstring} download.commoncrawl.decode_html
    :summary:
    ```
* - {py:obj}`download_common_crawl <download.commoncrawl.download_common_crawl>`
  - ```{autodoc2-docstring} download.commoncrawl.download_common_crawl
    :summary:
    ```
* - {py:obj}`get_all_stop_words <download.commoncrawl.get_all_stop_words>`
  - ```{autodoc2-docstring} download.commoncrawl.get_all_stop_words
    :summary:
    ```
* - {py:obj}`get_stop_list_dict <download.commoncrawl.get_stop_list_dict>`
  - ```{autodoc2-docstring} download.commoncrawl.get_stop_list_dict
    :summary:
    ```
* - {py:obj}`lang_detect <download.commoncrawl.lang_detect>`
  - ```{autodoc2-docstring} download.commoncrawl.lang_detect
    :summary:
    ```
* - {py:obj}`try_decode_with_detected_encoding <download.commoncrawl.try_decode_with_detected_encoding>`
  - ```{autodoc2-docstring} download.commoncrawl.try_decode_with_detected_encoding
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NON_SPACED_LANGUAGES <download.commoncrawl.NON_SPACED_LANGUAGES>`
  - ```{autodoc2-docstring} download.commoncrawl.NON_SPACED_LANGUAGES
    :summary:
    ```
````

### API

`````{py:class} CommonCrawlWARCDownloader(download_dir: str, aws: bool = False, verbose: bool = False)
:canonical: download.commoncrawl.CommonCrawlWARCDownloader

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentDownloader`

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCDownloader
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCDownloader.__init__
```

````{py:method} download(url: str) -> str
:canonical: download.commoncrawl.CommonCrawlWARCDownloader.download

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCDownloader.download
```

````

`````

`````{py:class} CommonCrawlWARCDownloaderExtractOnly(aws: bool = False, verbose: bool = False)
:canonical: download.commoncrawl.CommonCrawlWARCDownloaderExtractOnly

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentDownloader`

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCDownloaderExtractOnly
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCDownloaderExtractOnly.__init__
```

````{py:method} download(url: str) -> str
:canonical: download.commoncrawl.CommonCrawlWARCDownloaderExtractOnly.download

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCDownloaderExtractOnly.download
```

````

`````

`````{py:class} CommonCrawlWARCExtractor(algorithm: download.commoncrawl.HTMLExtractorAlgorithm | None = None, stop_lists: dict[str, frozenset[str]] | None = None)
:canonical: download.commoncrawl.CommonCrawlWARCExtractor

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentExtractor`

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCExtractor
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCExtractor.__init__
```

````{py:method} extract(content: str) -> dict[str, str] | None
:canonical: download.commoncrawl.CommonCrawlWARCExtractor.extract

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCExtractor.extract
```

````

`````

`````{py:class} CommonCrawlWARCIterator(log_frequency: int = 1000)
:canonical: download.commoncrawl.CommonCrawlWARCIterator

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentIterator`

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCIterator
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCIterator.__init__
```

````{py:method} iterate(file_path: str) -> collections.abc.Iterator[tuple[dict[str, str], str]]
:canonical: download.commoncrawl.CommonCrawlWARCIterator.iterate

```{autodoc2-docstring} download.commoncrawl.CommonCrawlWARCIterator.iterate
```

````

`````

`````{py:class} HTMLExtractorAlgorithm
:canonical: download.commoncrawl.HTMLExtractorAlgorithm

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} download.commoncrawl.HTMLExtractorAlgorithm
```

````{py:method} extract_text(html: str, stop_words: frozenset[str], language: str) -> list[str] | None
:canonical: download.commoncrawl.HTMLExtractorAlgorithm.extract_text
:abstractmethod:

```{autodoc2-docstring} download.commoncrawl.HTMLExtractorAlgorithm.extract_text
```

````

`````

`````{py:class} JusTextExtractor(length_low: int = 70, length_high: int = 200, stopwords_low: float = 0.3, stopwords_high: float = 0.32, max_link_density: float = 0.2, max_heading_distance: int = 200, no_headings: bool = False, is_boilerplate: bool | None = None, logger: logging.Logger | None = None)
:canonical: download.commoncrawl.JusTextExtractor

Bases: {py:obj}`download.commoncrawl.HTMLExtractorAlgorithm`

```{autodoc2-docstring} download.commoncrawl.JusTextExtractor
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.commoncrawl.JusTextExtractor.__init__
```

````{py:method} extract_text(html: str, stop_words: frozenset[str], language: str) -> list[str] | None
:canonical: download.commoncrawl.JusTextExtractor.extract_text

```{autodoc2-docstring} download.commoncrawl.JusTextExtractor.extract_text
```

````

`````

````{py:data} NON_SPACED_LANGUAGES
:canonical: download.commoncrawl.NON_SPACED_LANGUAGES
:value: >
   ['THAI', 'CHINESE', 'JAPANESE', 'KOREAN']

```{autodoc2-docstring} download.commoncrawl.NON_SPACED_LANGUAGES
```

````

`````{py:class} ResiliparseExtractor(required_stopword_density: float = 0.32, main_content: bool = True, alt_texts: bool = False)
:canonical: download.commoncrawl.ResiliparseExtractor

Bases: {py:obj}`download.commoncrawl.HTMLExtractorAlgorithm`

```{autodoc2-docstring} download.commoncrawl.ResiliparseExtractor
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.commoncrawl.ResiliparseExtractor.__init__
```

````{py:method} extract_text(html: str, stop_words: frozenset[str], language: str) -> list[str] | None
:canonical: download.commoncrawl.ResiliparseExtractor.extract_text

```{autodoc2-docstring} download.commoncrawl.ResiliparseExtractor.extract_text
```

````

`````

`````{py:class} TrafilaturaExtractor(required_stopword_density: float = 0.32, min_extracted_size: int = 250, min_extracted_comm_size: int = 1, min_output_size: int = 1, min_output_comm_size: int = 1, max_tree_size: int | None = None, min_duplcheck_size: int = 100, max_repetitions: int = 2, **extract_kwargs)
:canonical: download.commoncrawl.TrafilaturaExtractor

Bases: {py:obj}`download.commoncrawl.HTMLExtractorAlgorithm`

```{autodoc2-docstring} download.commoncrawl.TrafilaturaExtractor
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.commoncrawl.TrafilaturaExtractor.__init__
```

````{py:method} extract_text(html: str, stop_words: frozenset[str], language: str) -> list[str] | None
:canonical: download.commoncrawl.TrafilaturaExtractor.extract_text

```{autodoc2-docstring} download.commoncrawl.TrafilaturaExtractor.extract_text
```

````

`````

````{py:function} decode_html(html_bytes: bytes) -> str | None
:canonical: download.commoncrawl.decode_html

```{autodoc2-docstring} download.commoncrawl.decode_html
```
````

````{py:function} download_common_crawl(output_path: str, start_snapshot: str, end_snapshot: str, output_type: typing.Literal[jsonl, parquet] = 'jsonl', algorithm: download.commoncrawl.HTMLExtractorAlgorithm | None = None, stop_lists: dict[str, frozenset[str]] | None = None, news: bool = False, aws: bool = False, raw_download_dir: str | None = None, keep_raw_download: bool = False, force_download: bool = False, url_limit: int | None = None, record_limit: int | None = None) -> nemo_curator.datasets.DocumentDataset
:canonical: download.commoncrawl.download_common_crawl

```{autodoc2-docstring} download.commoncrawl.download_common_crawl
```
````

````{py:function} get_all_stop_words() -> frozenset[str]
:canonical: download.commoncrawl.get_all_stop_words

```{autodoc2-docstring} download.commoncrawl.get_all_stop_words
```
````

````{py:function} get_stop_list_dict(languages: list[str] | None = None) -> dict[str, frozenset[str]]
:canonical: download.commoncrawl.get_stop_list_dict

```{autodoc2-docstring} download.commoncrawl.get_stop_list_dict
```
````

````{py:function} lang_detect(decoded_html: str) -> str
:canonical: download.commoncrawl.lang_detect

```{autodoc2-docstring} download.commoncrawl.lang_detect
```
````

````{py:function} try_decode_with_detected_encoding(html_bytes: bytes) -> str | None
:canonical: download.commoncrawl.try_decode_with_detected_encoding

```{autodoc2-docstring} download.commoncrawl.try_decode_with_detected_encoding
```
````
