# {py:mod}`download.doc_builder`

```{py:module} download.doc_builder
```

```{autodoc2-docstring} download.doc_builder
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DocumentDownloader <download.doc_builder.DocumentDownloader>`
  - ```{autodoc2-docstring} download.doc_builder.DocumentDownloader
    :summary:
    ```
* - {py:obj}`DocumentExtractor <download.doc_builder.DocumentExtractor>`
  - ```{autodoc2-docstring} download.doc_builder.DocumentExtractor
    :summary:
    ```
* - {py:obj}`DocumentIterator <download.doc_builder.DocumentIterator>`
  - ```{autodoc2-docstring} download.doc_builder.DocumentIterator
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`batch_download <download.doc_builder.batch_download>`
  - ```{autodoc2-docstring} download.doc_builder.batch_download
    :summary:
    ```
* - {py:obj}`download_and_extract <download.doc_builder.download_and_extract>`
  - ```{autodoc2-docstring} download.doc_builder.download_and_extract
    :summary:
    ```
* - {py:obj}`import_downloader <download.doc_builder.import_downloader>`
  - ```{autodoc2-docstring} download.doc_builder.import_downloader
    :summary:
    ```
* - {py:obj}`import_extractor <download.doc_builder.import_extractor>`
  - ```{autodoc2-docstring} download.doc_builder.import_extractor
    :summary:
    ```
* - {py:obj}`import_iterator <download.doc_builder.import_iterator>`
  - ```{autodoc2-docstring} download.doc_builder.import_iterator
    :summary:
    ```
````

### API

`````{py:class} DocumentDownloader()
:canonical: download.doc_builder.DocumentDownloader

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} download.doc_builder.DocumentDownloader
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.doc_builder.DocumentDownloader.__init__
```

````{py:method} download(url: str) -> str
:canonical: download.doc_builder.DocumentDownloader.download
:abstractmethod:

```{autodoc2-docstring} download.doc_builder.DocumentDownloader.download
```

````

`````

`````{py:class} DocumentExtractor()
:canonical: download.doc_builder.DocumentExtractor

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} download.doc_builder.DocumentExtractor
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.doc_builder.DocumentExtractor.__init__
```

````{py:method} extract(content: str) -> dict[str, str]
:canonical: download.doc_builder.DocumentExtractor.extract
:abstractmethod:

```{autodoc2-docstring} download.doc_builder.DocumentExtractor.extract
```

````

`````

`````{py:class} DocumentIterator()
:canonical: download.doc_builder.DocumentIterator

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} download.doc_builder.DocumentIterator
```

```{rubric} Initialization
```

```{autodoc2-docstring} download.doc_builder.DocumentIterator.__init__
```

````{py:method} iterate(file_path: str) -> collections.abc.Iterator[tuple[dict[str, str], str]]
:canonical: download.doc_builder.DocumentIterator.iterate
:abstractmethod:

```{autodoc2-docstring} download.doc_builder.DocumentIterator.iterate
```

````

`````

````{py:function} batch_download(urls: list[str], downloader: download.doc_builder.DocumentDownloader) -> list[str]
:canonical: download.doc_builder.batch_download

```{autodoc2-docstring} download.doc_builder.batch_download
```
````

````{py:function} download_and_extract(urls: list[str], output_paths: list[str], downloader: download.doc_builder.DocumentDownloader, iterator: download.doc_builder.DocumentIterator, extractor: download.doc_builder.DocumentExtractor, output_format: dict, output_type: typing.Literal[jsonl, parquet] = 'jsonl', keep_raw_download: bool = False, force_download: bool = False, input_meta: str | dict | None = None, filename_col: str = 'file_name', record_limit: int | None = None) -> nemo_curator.datasets.DocumentDataset
:canonical: download.doc_builder.download_and_extract

```{autodoc2-docstring} download.doc_builder.download_and_extract
```
````

````{py:function} import_downloader(downloader_path: str) -> download.doc_builder.DocumentDownloader
:canonical: download.doc_builder.import_downloader

```{autodoc2-docstring} download.doc_builder.import_downloader
```
````

````{py:function} import_extractor(extractor_path: str) -> download.doc_builder.DocumentExtractor
:canonical: download.doc_builder.import_extractor

```{autodoc2-docstring} download.doc_builder.import_extractor
```
````

````{py:function} import_iterator(iterator_path: str) -> download.doc_builder.DocumentIterator
:canonical: download.doc_builder.import_iterator

```{autodoc2-docstring} download.doc_builder.import_iterator
```
````
