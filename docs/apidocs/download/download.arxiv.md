# {py:mod}`download.arxiv`

```{py:module} download.arxiv
```

```{autodoc2-docstring} download.arxiv
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArxivDownloader <download.arxiv.ArxivDownloader>`
  - ```{autodoc2-docstring} download.arxiv.ArxivDownloader
    :summary:
    ```
* - {py:obj}`ArxivExtractor <download.arxiv.ArxivExtractor>`
  - ```{autodoc2-docstring} download.arxiv.ArxivExtractor
    :summary:
    ```
* - {py:obj}`ArxivIterator <download.arxiv.ArxivIterator>`
  - ```{autodoc2-docstring} download.arxiv.ArxivIterator
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`download_arxiv <download.arxiv.download_arxiv>`
  - ```{autodoc2-docstring} download.arxiv.download_arxiv
    :summary:
    ```
````

### API

`````{py:class} ArxivDownloader(download_dir: str, verbose: bool = False)
:canonical: download.arxiv.ArxivDownloader

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentDownloader`

```{autodoc2-docstring} download.arxiv.ArxivDownloader
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.arxiv.ArxivDownloader.__init__
```

````{py:method} download(tarfile: str) -> str
:canonical: download.arxiv.ArxivDownloader.download

```{autodoc2-docstring} download.arxiv.ArxivDownloader.download
```

````

`````

`````{py:class} ArxivExtractor()
:canonical: download.arxiv.ArxivExtractor

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentExtractor`

```{autodoc2-docstring} download.arxiv.ArxivExtractor
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.arxiv.ArxivExtractor.__init__
```

````{py:method} extract(content: list[str]) -> dict[str, str] | None
:canonical: download.arxiv.ArxivExtractor.extract

```{autodoc2-docstring} download.arxiv.ArxivExtractor.extract
```

````

`````

`````{py:class} ArxivIterator(log_frequency: int = 1000)
:canonical: download.arxiv.ArxivIterator

Bases: {py:obj}`nemo_curator.download.doc_builder.DocumentIterator`

```{autodoc2-docstring} download.arxiv.ArxivIterator
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.arxiv.ArxivIterator.__init__
```

````{py:method} iterate(file_path: str) -> collections.abc.Iterator[tuple[dict[str, str], list[str]]]
:canonical: download.arxiv.ArxivIterator.iterate

```{autodoc2-docstring} download.arxiv.ArxivIterator.iterate
```

````

`````

````{py:function} download_arxiv(output_path: str, output_type: typing.Literal[jsonl, parquet] = 'jsonl', raw_download_dir: str | None = None, keep_raw_download: bool = False, force_download: bool = False, url_limit: int | None = None, record_limit: int | None = None) -> nemo_curator.datasets.DocumentDataset
:canonical: download.arxiv.download_arxiv

```{autodoc2-docstring} download.arxiv.download_arxiv
```
````
