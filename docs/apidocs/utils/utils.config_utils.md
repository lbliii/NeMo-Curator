# {py:mod}`utils.config_utils`

```{py:module} utils.config_utils
```

```{autodoc2-docstring} utils.config_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`build_downloader <utils.config_utils.build_downloader>`
  - ```{autodoc2-docstring} utils.config_utils.build_downloader
    :summary:
    ```
* - {py:obj}`build_filter <utils.config_utils.build_filter>`
  - ```{autodoc2-docstring} utils.config_utils.build_filter
    :summary:
    ```
* - {py:obj}`build_filter_pipeline <utils.config_utils.build_filter_pipeline>`
  - ```{autodoc2-docstring} utils.config_utils.build_filter_pipeline
    :summary:
    ```
````

### API

````{py:function} build_downloader(downloader_config_file: str, default_download_dir: str | None = None) -> tuple[nemo_curator.download.DocumentDownloader, nemo_curator.download.DocumentIterator, nemo_curator.download.DocumentExtractor, dict]
:canonical: utils.config_utils.build_downloader

```{autodoc2-docstring} utils.config_utils.build_downloader
```
````

````{py:function} build_filter(filter_config: dict) -> nemo_curator.Filter | nemo_curator.ScoreFilter
:canonical: utils.config_utils.build_filter

```{autodoc2-docstring} utils.config_utils.build_filter
```
````

````{py:function} build_filter_pipeline(filter_config_file: str) -> nemo_curator.Sequential
:canonical: utils.config_utils.build_filter_pipeline

```{autodoc2-docstring} utils.config_utils.build_filter_pipeline
```
````
