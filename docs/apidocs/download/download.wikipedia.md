# {py:mod}`download.wikipedia`

```{py:module} download.wikipedia
```

```{autodoc2-docstring} download.wikipedia
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`WikipediaDownloader <download.wikipedia.WikipediaDownloader>`
  - ```{autodoc2-docstring} download.wikipedia.WikipediaDownloader
    :summary:
    ```
* - {py:obj}`WikipediaExtractor <download.wikipedia.WikipediaExtractor>`
  - ```{autodoc2-docstring} download.wikipedia.WikipediaExtractor
    :summary:
    ```
* - {py:obj}`WikipediaIterator <download.wikipedia.WikipediaIterator>`
  - ```{autodoc2-docstring} download.wikipedia.WikipediaIterator
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`download_wikipedia <download.wikipedia.download_wikipedia>`
  - ```{autodoc2-docstring} download.wikipedia.download_wikipedia
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CAT_ALIASES <download.wikipedia.CAT_ALIASES>`
  - ```{autodoc2-docstring} download.wikipedia.CAT_ALIASES
    :summary:
    ```
* - {py:obj}`MEDIA_ALIASES <download.wikipedia.MEDIA_ALIASES>`
  - ```{autodoc2-docstring} download.wikipedia.MEDIA_ALIASES
    :summary:
    ```
````

### API

````{py:data} CAT_ALIASES
:canonical: download.wikipedia.CAT_ALIASES
:value: >
   None

```{autodoc2-docstring} download.wikipedia.CAT_ALIASES
```

````

````{py:data} MEDIA_ALIASES
:canonical: download.wikipedia.MEDIA_ALIASES
:value: >
   None

```{autodoc2-docstring} download.wikipedia.MEDIA_ALIASES
```

````

`````{py:class} WikipediaDownloader(download_dir: str, verbose: bool = False)
:canonical: download.wikipedia.WikipediaDownloader

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentDownloader`

```{autodoc2-docstring} download.wikipedia.WikipediaDownloader
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.wikipedia.WikipediaDownloader.__init__
```

````{py:method} download(url: str) -> str
:canonical: download.wikipedia.WikipediaDownloader.download

```{autodoc2-docstring} download.wikipedia.WikipediaDownloader.download
```

````

`````

`````{py:class} WikipediaExtractor(language: str = 'en', parser=mwparserfromhell)
:canonical: download.wikipedia.WikipediaExtractor

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentExtractor`

```{autodoc2-docstring} download.wikipedia.WikipediaExtractor
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.wikipedia.WikipediaExtractor.__init__
```

````{py:method} extract(content) -> dict[str, str]
:canonical: download.wikipedia.WikipediaExtractor.extract

```{autodoc2-docstring} download.wikipedia.WikipediaExtractor.extract
```

````

`````

`````{py:class} WikipediaIterator(language: str = 'en', log_frequency: int = 1000)
:canonical: download.wikipedia.WikipediaIterator

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentIterator`

```{autodoc2-docstring} download.wikipedia.WikipediaIterator
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.wikipedia.WikipediaIterator.__init__
```

````{py:method} iterate(file_path: str) -> collections.abc.Iterator[tuple[dict[str, str], str]]
:canonical: download.wikipedia.WikipediaIterator.iterate

```{autodoc2-docstring} download.wikipedia.WikipediaIterator.iterate
```

````

`````

````{py:function} download_wikipedia(output_path: str, language: str = 'en', dump_date: str | None = None, output_type: typing.Literal[jsonl, parquet] = 'jsonl', raw_download_dir: str | None = None, keep_raw_download: bool = False, force_download: bool = False, url_limit: int | None = None, record_limit: int | None = None) -> nemo_curator.datasets.DocumentDataset
:canonical: download.wikipedia.download_wikipedia

```{autodoc2-docstring} download.wikipedia.download_wikipedia
```
````
