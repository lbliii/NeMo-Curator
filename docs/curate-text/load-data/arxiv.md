---
description: "Download and extract text from arXiv using Curator."
categories: ["how-to-guides"]
tags: ["arxiv", "academic-papers", "latex", "data-loading", "scientific-data"]
personas: ["data-scientist-focused", "mle-focused"]
difficulty: "intermediate"
content_type: "how-to"
modality: "text-only"
---

(text-load-data-arxiv)=

# ArXiv

Download and extract text from ArXiv LaTeX source bundles using Curator.

ArXiv hosts millions of scholarly papers, typically distributed as LaTeX source inside `.tar` archives under the `s3://arxiv/src/` requester-pays bucket.

## How it Works

The ArXiv pipeline in Curator consists of four stages:

1. **URL Generation**: Lists available ArXiv source tar files from the S3 bucket
2. **Download**: Downloads `.tar` archives via s5cmd (requester-pays)
3. **Iteration**: Extracts LaTeX projects and yields per-paper records
4. **Extraction**: Cleans LaTeX and produces plain text

## Before You Start

You must have:

- An AWS account with credentials configured (profile, environment, or instance role). Accessing `s3://arxiv/src/` uses S3 Requester Pays; you incur charges for listing and data transfer.
- [`s5cmd` installed](https://github.com/peak/s5cmd)

```{admonition} S3 Requester Pays
:class: tip

The ArXiv bucket `s3://arxiv/src/` is Requester Pays. The examples on this page already pass the Requester Pays option via `s5cmd`, so you can run them as-is. If you use other tools (for example, `aws s3`), include the equivalent flag (AWS CLI: `--request-payer requester`) and ensure your AWS credentials are active.
```

---

## Usage

Create and run an ArXiv processing pipeline and write outputs to JSONL:

```python
from ray_curator.pipeline import Pipeline
from ray_curator.backends.xenna.executor import XennaExecutor
from ray_curator.stages.download.text import ArxivDownloadExtractStage
from ray_curator.stages.io.writer import JsonlWriter

def main():
    pipeline = Pipeline(
        name="arxiv_pipeline",
        description="Download and process ArXiv LaTeX sources"
    )

    # Add ArXiv stage
    arxiv_stage = ArxivDownloadExtractStage(
        download_dir="./arxiv_downloads",
        url_limit=5,        # optional: number of tar files to process
        record_limit=1000,  # optional: max papers per tar
        add_filename_column=True,
        verbose=True,
    )
    pipeline.add_stage(arxiv_stage)

    # Add writer stage
    writer = JsonlWriter(output_dir="./arxiv_output")
    pipeline.add_stage(writer)

    # Execute
    executor = XennaExecutor()
    results = pipeline.run(executor)
    print(f"Completed with {len(results) if results else 0} output files")

if __name__ == "__main__":
    main()
```

### Parameters

```{list-table} ArxivDownloadExtractStage Parameters
:header-rows: 1
:widths: 25 20 35 20

* - Parameter
  - Type
  - Description
  - Default
* - `download_dir`
  - str
  - Directory to store downloaded `.tar` files
  - "./arxiv_downloads"
* - `url_limit`
  - int | None
  - Maximum number of ArXiv tar files to download (useful for testing)
  - None
* - `record_limit`
  - int | None
  - Maximum number of papers to extract per tar file
  - None
* - `add_filename_column`
  - bool | str
  - Whether to add a source filename column to output; if str, use it as the column name
  - True (column name defaults to `file_name`)
* - `log_frequency`
  - int
  - How often to log progress while iterating papers
  - 1000
* - `verbose`
  - bool
  - Enable verbose logging during download
  - False
```

## Output Format

The extractor returns per-paper text; the filename column is optionally added by the pipeline:

```json
{
  "text": "Main body text extracted from LaTeX after cleaning...",
  "file_name": "arXiv_src_2024_01.tar"  
}
```

```{list-table} Output Fields
:header-rows: 1
:widths: 20 80

* - Field
  - Description
* - `text`
  - Extracted and cleaned paper text (LaTeX macros inlined where supported, comments and references removed)
* - `file_name`
  - Optional. Name of the source tar file (enabled by `add_filename_column`)
```

```{admonition} Intermediate Fields
:class: note

During iteration the pipeline yields `id` (ArXiv identifier), `source_id` (tar basename), and `content` (list of LaTeX files). The final extractor stage emits only `text` plus the optional filename column.
```
