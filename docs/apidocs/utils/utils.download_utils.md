# {py:mod}`utils.download_utils`

```{py:module} utils.download_utils
```

```{autodoc2-docstring} utils.download_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_arxiv_urls <utils.download_utils.get_arxiv_urls>`
  - ```{autodoc2-docstring} utils.download_utils.get_arxiv_urls
    :summary:
    ```
* - {py:obj}`get_common_crawl_snapshot_index <utils.download_utils.get_common_crawl_snapshot_index>`
  - ```{autodoc2-docstring} utils.download_utils.get_common_crawl_snapshot_index
    :summary:
    ```
* - {py:obj}`get_common_crawl_urls <utils.download_utils.get_common_crawl_urls>`
  - ```{autodoc2-docstring} utils.download_utils.get_common_crawl_urls
    :summary:
    ```
* - {py:obj}`get_main_warc_paths <utils.download_utils.get_main_warc_paths>`
  - ```{autodoc2-docstring} utils.download_utils.get_main_warc_paths
    :summary:
    ```
* - {py:obj}`get_news_warc_paths <utils.download_utils.get_news_warc_paths>`
  - ```{autodoc2-docstring} utils.download_utils.get_news_warc_paths
    :summary:
    ```
* - {py:obj}`get_wikipedia_urls <utils.download_utils.get_wikipedia_urls>`
  - ```{autodoc2-docstring} utils.download_utils.get_wikipedia_urls
    :summary:
    ```
````

### API

````{py:function} get_arxiv_urls() -> list[str]
:canonical: utils.download_utils.get_arxiv_urls

```{autodoc2-docstring} utils.download_utils.get_arxiv_urls
```
````

````{py:function} get_common_crawl_snapshot_index(index_prefix: str) -> list[dict]
:canonical: utils.download_utils.get_common_crawl_snapshot_index

```{autodoc2-docstring} utils.download_utils.get_common_crawl_snapshot_index
```
````

````{py:function} get_common_crawl_urls(starting_snapshot: str, ending_snapshot: str, data_domain_prefix: str = 'https://data.commoncrawl.org', index_prefix: str = 'https://index.commoncrawl.org', news: bool = False) -> list[str]
:canonical: utils.download_utils.get_common_crawl_urls

```{autodoc2-docstring} utils.download_utils.get_common_crawl_urls
```
````

````{py:function} get_main_warc_paths(snapshot_index: list[dict], start_snapshot: str, end_snapshot: str, prefix: str = 'https://data.commoncrawl.org') -> list[str]
:canonical: utils.download_utils.get_main_warc_paths

```{autodoc2-docstring} utils.download_utils.get_main_warc_paths
```
````

````{py:function} get_news_warc_paths(start_date: str, end_date: str, prefix: str = 'https://data.commoncrawl.org') -> list[str]
:canonical: utils.download_utils.get_news_warc_paths

```{autodoc2-docstring} utils.download_utils.get_news_warc_paths
```
````

````{py:function} get_wikipedia_urls(language: str = 'en', wikidumps_index_prefix: str = 'https://dumps.wikimedia.org', dump_date: str | None = None) -> list[str]
:canonical: utils.download_utils.get_wikipedia_urls

```{autodoc2-docstring} utils.download_utils.get_wikipedia_urls
```
````
