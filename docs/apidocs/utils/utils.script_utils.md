# {py:mod}`utils.script_utils`

```{py:module} utils.script_utils
```

```{autodoc2-docstring} utils.script_utils
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArgumentHelper <utils.script_utils.ArgumentHelper>`
  - ```{autodoc2-docstring} utils.script_utils.ArgumentHelper
    :summary:
    ```
````

### API

`````{py:class} ArgumentHelper(parser: argparse.ArgumentParser)
:canonical: utils.script_utils.ArgumentHelper

```{autodoc2-docstring} utils.script_utils.ArgumentHelper
```

```{rubric} Initialization
```

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.__init__
```

````{py:method} add_arg_autocast(help: str = 'Whether to use autocast or not') -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_autocast

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_autocast
```

````

````{py:method} add_arg_batch_size(default: int = 64, help: str = 'Number of files to read into memory at a time.') -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_batch_size

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_batch_size
```

````

````{py:method} add_arg_device() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_device

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_device
```

````

````{py:method} add_arg_enable_spilling() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_enable_spilling

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_enable_spilling
```

````

````{py:method} add_arg_id_column() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_id_column

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_id_column
```

````

````{py:method} add_arg_id_column_type() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_id_column_type

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_id_column_type
```

````

````{py:method} add_arg_input_data_dir(required: bool = False, help: str = 'Input directory consisting of .jsonl files that are accessible to all nodes. Use this for a distributed file system.') -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_input_data_dir

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_input_data_dir
```

````

````{py:method} add_arg_input_file_extension(help: str = 'The file extension of the input files. If not provided, the input file type will be used.') -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_input_file_extension

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_input_file_extension
```

````

````{py:method} add_arg_input_file_type(choices: list | None = None, required: bool = False, help: str = 'File type of the dataset to be read in. Supported file formats include "jsonl" (default), "pickle", or "parquet".') -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_input_file_type

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_input_file_type
```

````

````{py:method} add_arg_input_local_data_dir() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_input_local_data_dir

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_input_local_data_dir
```

````

````{py:method} add_arg_input_meta() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_input_meta

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_input_meta
```

````

````{py:method} add_arg_input_text_field() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_input_text_field

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_input_text_field
```

````

````{py:method} add_arg_language(help: str) -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_language

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_language
```

````

````{py:method} add_arg_log_dir(default: str) -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_log_dir

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_log_dir
```

````

````{py:method} add_arg_max_chars(default: int = 2000) -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_max_chars

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_max_chars
```

````

````{py:method} add_arg_max_mem_gb_classifier() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_max_mem_gb_classifier

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_max_mem_gb_classifier
```

````

````{py:method} add_arg_minhash_length() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_minhash_length

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_minhash_length
```

````

````{py:method} add_arg_model_path(help: str = 'The path to the model file') -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_model_path

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_model_path
```

````

````{py:method} add_arg_nvlink_only() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_nvlink_only

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_nvlink_only
```

````

````{py:method} add_arg_output_data_dir(help: str) -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_output_data_dir

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_output_data_dir
```

````

````{py:method} add_arg_output_dir(required: bool = False, help: str = 'The output directory to write results.') -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_output_dir

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_output_dir
```

````

````{py:method} add_arg_output_file_type(choices: list | None = None, help: str = 'File type the dataset will be written to. Supported file formats include "jsonl" (default), "pickle", or "parquet".') -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_output_file_type

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_output_file_type
```

````

````{py:method} add_arg_output_train_file(help: str, default: str | None = None) -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_output_train_file

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_output_train_file
```

````

````{py:method} add_arg_protocol() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_protocol

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_protocol
```

````

````{py:method} add_arg_rmm_pool_size() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_rmm_pool_size

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_rmm_pool_size
```

````

````{py:method} add_arg_scheduler_address() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_scheduler_address

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_scheduler_address
```

````

````{py:method} add_arg_scheduler_file() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_scheduler_file

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_scheduler_file
```

````

````{py:method} add_arg_seed(default: int = 42, help: str = 'If specified, the random seed used for shuffling.') -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_seed

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_seed
```

````

````{py:method} add_arg_set_torch_to_use_rmm() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_set_torch_to_use_rmm

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_set_torch_to_use_rmm
```

````

````{py:method} add_arg_shuffle(help: str) -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_shuffle

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_shuffle
```

````

````{py:method} add_arg_text_ddf_blocksize() -> None
:canonical: utils.script_utils.ArgumentHelper.add_arg_text_ddf_blocksize

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_arg_text_ddf_blocksize
```

````

````{py:method} add_distributed_args() -> argparse.ArgumentParser
:canonical: utils.script_utils.ArgumentHelper.add_distributed_args

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_distributed_args
```

````

````{py:method} add_distributed_classifier_cluster_args() -> None
:canonical: utils.script_utils.ArgumentHelper.add_distributed_classifier_cluster_args

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.add_distributed_classifier_cluster_args
```

````

````{py:method} attach_bool_arg(parser: argparse.ArgumentParser, flag_name: str, default: bool = False, help: str | None = None) -> None
:canonical: utils.script_utils.ArgumentHelper.attach_bool_arg
:staticmethod:

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.attach_bool_arg
```

````

````{py:method} attach_version_arg(version_string: str) -> None
:canonical: utils.script_utils.ArgumentHelper.attach_version_arg

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.attach_version_arg
```

````

````{py:method} parse_client_args(args: argparse.Namespace) -> dict
:canonical: utils.script_utils.ArgumentHelper.parse_client_args
:staticmethod:

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.parse_client_args
```

````

````{py:method} parse_distributed_classifier_args(description: str = 'Default distributed classifier argument parser.', max_chars_default: int = 2000) -> argparse.ArgumentParser
:canonical: utils.script_utils.ArgumentHelper.parse_distributed_classifier_args
:staticmethod:

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.parse_distributed_classifier_args
```

````

````{py:method} parse_gpu_dedup_args() -> argparse.ArgumentParser
:canonical: utils.script_utils.ArgumentHelper.parse_gpu_dedup_args

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.parse_gpu_dedup_args
```

````

````{py:method} parse_semdedup_args(description: str = 'Default argument parser for semantic deduplication.') -> argparse.ArgumentParser
:canonical: utils.script_utils.ArgumentHelper.parse_semdedup_args
:staticmethod:

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.parse_semdedup_args
```

````

````{py:method} set_default_n_workers(max_mem_gb_per_worker: float) -> None
:canonical: utils.script_utils.ArgumentHelper.set_default_n_workers

```{autodoc2-docstring} utils.script_utils.ArgumentHelper.set_default_n_workers
```

````

`````
