# {py:mod}`utils.distributed_utils`

```{py:module} utils.distributed_utils
```

```{autodoc2-docstring} utils.distributed_utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`check_dask_cwd <utils.distributed_utils.check_dask_cwd>`
  - ```{autodoc2-docstring} utils.distributed_utils.check_dask_cwd
    :summary:
    ```
* - {py:obj}`get_client <utils.distributed_utils.get_client>`
  - ```{autodoc2-docstring} utils.distributed_utils.get_client
    :summary:
    ```
* - {py:obj}`get_current_client <utils.distributed_utils.get_current_client>`
  - ```{autodoc2-docstring} utils.distributed_utils.get_current_client
    :summary:
    ```
* - {py:obj}`get_filepath_without_extension <utils.distributed_utils.get_filepath_without_extension>`
  - ```{autodoc2-docstring} utils.distributed_utils.get_filepath_without_extension
    :summary:
    ```
* - {py:obj}`get_gpu_memory_info <utils.distributed_utils.get_gpu_memory_info>`
  - ```{autodoc2-docstring} utils.distributed_utils.get_gpu_memory_info
    :summary:
    ```
* - {py:obj}`get_network_interfaces <utils.distributed_utils.get_network_interfaces>`
  - ```{autodoc2-docstring} utils.distributed_utils.get_network_interfaces
    :summary:
    ```
* - {py:obj}`get_num_workers <utils.distributed_utils.get_num_workers>`
  - ```{autodoc2-docstring} utils.distributed_utils.get_num_workers
    :summary:
    ```
* - {py:obj}`load_object_on_worker <utils.distributed_utils.load_object_on_worker>`
  - ```{autodoc2-docstring} utils.distributed_utils.load_object_on_worker
    :summary:
    ```
* - {py:obj}`offload_object_on_worker <utils.distributed_utils.offload_object_on_worker>`
  - ```{autodoc2-docstring} utils.distributed_utils.offload_object_on_worker
    :summary:
    ```
* - {py:obj}`performance_report_if <utils.distributed_utils.performance_report_if>`
  - ```{autodoc2-docstring} utils.distributed_utils.performance_report_if
    :summary:
    ```
* - {py:obj}`performance_report_if_with_ts_suffix <utils.distributed_utils.performance_report_if_with_ts_suffix>`
  - ```{autodoc2-docstring} utils.distributed_utils.performance_report_if_with_ts_suffix
    :summary:
    ```
* - {py:obj}`process_all_batches <utils.distributed_utils.process_all_batches>`
  - ```{autodoc2-docstring} utils.distributed_utils.process_all_batches
    :summary:
    ```
* - {py:obj}`process_batch <utils.distributed_utils.process_batch>`
  - ```{autodoc2-docstring} utils.distributed_utils.process_batch
    :summary:
    ```
* - {py:obj}`read_data <utils.distributed_utils.read_data>`
  - ```{autodoc2-docstring} utils.distributed_utils.read_data
    :summary:
    ```
* - {py:obj}`read_data_blocksize <utils.distributed_utils.read_data_blocksize>`
  - ```{autodoc2-docstring} utils.distributed_utils.read_data_blocksize
    :summary:
    ```
* - {py:obj}`read_data_files_per_partition <utils.distributed_utils.read_data_files_per_partition>`
  - ```{autodoc2-docstring} utils.distributed_utils.read_data_files_per_partition
    :summary:
    ```
* - {py:obj}`read_pandas_pickle <utils.distributed_utils.read_pandas_pickle>`
  - ```{autodoc2-docstring} utils.distributed_utils.read_pandas_pickle
    :summary:
    ```
* - {py:obj}`read_single_partition <utils.distributed_utils.read_single_partition>`
  - ```{autodoc2-docstring} utils.distributed_utils.read_single_partition
    :summary:
    ```
* - {py:obj}`seed_all <utils.distributed_utils.seed_all>`
  - ```{autodoc2-docstring} utils.distributed_utils.seed_all
    :summary:
    ```
* - {py:obj}`select_columns <utils.distributed_utils.select_columns>`
  - ```{autodoc2-docstring} utils.distributed_utils.select_columns
    :summary:
    ```
* - {py:obj}`single_partition_write_with_filename <utils.distributed_utils.single_partition_write_with_filename>`
  - ```{autodoc2-docstring} utils.distributed_utils.single_partition_write_with_filename
    :summary:
    ```
* - {py:obj}`start_dask_cpu_local_cluster <utils.distributed_utils.start_dask_cpu_local_cluster>`
  - ```{autodoc2-docstring} utils.distributed_utils.start_dask_cpu_local_cluster
    :summary:
    ```
* - {py:obj}`start_dask_gpu_local_cluster <utils.distributed_utils.start_dask_gpu_local_cluster>`
  - ```{autodoc2-docstring} utils.distributed_utils.start_dask_gpu_local_cluster
    :summary:
    ```
* - {py:obj}`write_to_disk <utils.distributed_utils.write_to_disk>`
  - ```{autodoc2-docstring} utils.distributed_utils.write_to_disk
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LocalCUDACluster <utils.distributed_utils.LocalCUDACluster>`
  - ```{autodoc2-docstring} utils.distributed_utils.LocalCUDACluster
    :summary:
    ```
* - {py:obj}`SUPPORTED_JSONL_COMPRESSIONS <utils.distributed_utils.SUPPORTED_JSONL_COMPRESSIONS>`
  - ```{autodoc2-docstring} utils.distributed_utils.SUPPORTED_JSONL_COMPRESSIONS
    :summary:
    ```
* - {py:obj}`get_device_total_memory <utils.distributed_utils.get_device_total_memory>`
  - ```{autodoc2-docstring} utils.distributed_utils.get_device_total_memory
    :summary:
    ```
````

### API

````{py:data} LocalCUDACluster
:canonical: utils.distributed_utils.LocalCUDACluster
:value: >
   'gpu_only_import_from(...)'

```{autodoc2-docstring} utils.distributed_utils.LocalCUDACluster
```

````

````{py:exception} NoWorkerError()
:canonical: utils.distributed_utils.NoWorkerError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} utils.distributed_utils.NoWorkerError
```

```{rubric} Initialization
```

```{autodoc2-docstring} utils.distributed_utils.NoWorkerError.__init__
```

````

````{py:data} SUPPORTED_JSONL_COMPRESSIONS
:canonical: utils.distributed_utils.SUPPORTED_JSONL_COMPRESSIONS
:value: >
   None

```{autodoc2-docstring} utils.distributed_utils.SUPPORTED_JSONL_COMPRESSIONS
```

````

````{py:function} check_dask_cwd(file_list: list[str]) -> None
:canonical: utils.distributed_utils.check_dask_cwd

```{autodoc2-docstring} utils.distributed_utils.check_dask_cwd
```
````

````{py:function} get_client(cluster_type: typing.Literal[cpu, gpu] = 'cpu', scheduler_address: str | None = None, scheduler_file: str | None = None, n_workers: int | None = os.cpu_count(), threads_per_worker: int = 1, nvlink_only: bool = False, protocol: typing.Literal[tcp, ucx] = 'tcp', rmm_pool_size: str | int | None = '1024M', enable_spilling: bool = True, set_torch_to_use_rmm: bool = False, rmm_async: bool = True, rmm_maximum_pool_size: str | int | None = None, rmm_managed_memory: bool = False, rmm_release_threshold: str | int | None = None, **cluster_kwargs) -> dask.distributed.Client
:canonical: utils.distributed_utils.get_client

```{autodoc2-docstring} utils.distributed_utils.get_client
```
````

````{py:function} get_current_client() -> dask.distributed.Client | None
:canonical: utils.distributed_utils.get_current_client

```{autodoc2-docstring} utils.distributed_utils.get_current_client
```
````

````{py:data} get_device_total_memory
:canonical: utils.distributed_utils.get_device_total_memory
:value: >
   'gpu_only_import_from(...)'

```{autodoc2-docstring} utils.distributed_utils.get_device_total_memory
```

````

````{py:function} get_filepath_without_extension(path: str) -> str
:canonical: utils.distributed_utils.get_filepath_without_extension

```{autodoc2-docstring} utils.distributed_utils.get_filepath_without_extension
```
````

````{py:function} get_gpu_memory_info() -> dict[str, int]
:canonical: utils.distributed_utils.get_gpu_memory_info

```{autodoc2-docstring} utils.distributed_utils.get_gpu_memory_info
```
````

````{py:function} get_network_interfaces() -> list[str]
:canonical: utils.distributed_utils.get_network_interfaces

```{autodoc2-docstring} utils.distributed_utils.get_network_interfaces
```
````

````{py:function} get_num_workers(client: dask.distributed.Client | None) -> int | None
:canonical: utils.distributed_utils.get_num_workers

```{autodoc2-docstring} utils.distributed_utils.get_num_workers
```
````

````{py:function} load_object_on_worker(attr: str, load_object_function: collections.abc.Callable, load_object_kwargs: dict) -> Any
:canonical: utils.distributed_utils.load_object_on_worker

```{autodoc2-docstring} utils.distributed_utils.load_object_on_worker
```
````

````{py:function} offload_object_on_worker(attr: str) -> bool
:canonical: utils.distributed_utils.offload_object_on_worker

```{autodoc2-docstring} utils.distributed_utils.offload_object_on_worker
```
````

````{py:function} performance_report_if(path: str | None = None, report_name: str = 'dask-profile.html') -> contextlib.AbstractContextManager[Any]
:canonical: utils.distributed_utils.performance_report_if

```{autodoc2-docstring} utils.distributed_utils.performance_report_if
```
````

````{py:function} performance_report_if_with_ts_suffix(path: str | None = None, report_name: str = 'dask-profile') -> contextlib.AbstractContextManager[Any]
:canonical: utils.distributed_utils.performance_report_if_with_ts_suffix

```{autodoc2-docstring} utils.distributed_utils.performance_report_if_with_ts_suffix
```
````

````{py:function} process_all_batches(loader_valid, load_model_function, load_model_kwargs, run_inference_function, run_inference_kwargs)
:canonical: utils.distributed_utils.process_all_batches

```{autodoc2-docstring} utils.distributed_utils.process_all_batches
```
````

````{py:function} process_batch(load_model_function, load_model_kwargs, run_inference_function, run_inference_kwargs)
:canonical: utils.distributed_utils.process_batch

```{autodoc2-docstring} utils.distributed_utils.process_batch
```
````

````{py:function} read_data(input_files: str | list[str], file_type: str = 'pickle', backend: typing.Literal[utils.distributed_utils.cudf, pandas] = 'cudf', blocksize: str | None = None, files_per_partition: int | None = 1, add_filename: bool | str = False, input_meta: str | dict | None = None, columns: list[str] | None = None, read_func_single_partition: collections.abc.Callable[[list[str], str, bool, str | dict, dict], dask.dataframe.DataFrame | pandas.DataFrame] | None = None, **kwargs) -> dask.dataframe.DataFrame
:canonical: utils.distributed_utils.read_data

```{autodoc2-docstring} utils.distributed_utils.read_data
```
````

````{py:function} read_data_blocksize(input_files: list[str], backend: typing.Literal[utils.distributed_utils.cudf, pandas], file_type: typing.Literal[parquet, jsonl], blocksize: str, add_filename: bool | str = False, input_meta: str | dict | None = None, columns: list[str] | None = None, **kwargs) -> dask.dataframe.DataFrame
:canonical: utils.distributed_utils.read_data_blocksize

```{autodoc2-docstring} utils.distributed_utils.read_data_blocksize
```
````

````{py:function} read_data_files_per_partition(input_files: list[str], file_type: typing.Literal[parquet, json, jsonl], backend: typing.Literal[utils.distributed_utils.cudf, pandas] = 'cudf', add_filename: bool | str = False, files_per_partition: int | None = None, input_meta: str | dict | None = None, columns: list[str] | None = None, read_func_single_partition: collections.abc.Callable[[list[str], str, bool, str | dict, dict], dask.dataframe.DataFrame | pandas.DataFrame] | None = None, **kwargs) -> dask.dataframe.DataFrame
:canonical: utils.distributed_utils.read_data_files_per_partition

```{autodoc2-docstring} utils.distributed_utils.read_data_files_per_partition
```
````

````{py:function} read_pandas_pickle(file: str, add_filename: bool | str = False, columns: list[str] | None = None, **kwargs) -> pandas.DataFrame
:canonical: utils.distributed_utils.read_pandas_pickle

```{autodoc2-docstring} utils.distributed_utils.read_pandas_pickle
```
````

````{py:function} read_single_partition(files: list[str], backend: typing.Literal[utils.distributed_utils.cudf, pandas] = 'cudf', file_type: str = 'jsonl', add_filename: bool | str = False, input_meta: str | dict | None = None, io_columns: list[str] | None = None, **kwargs) -> utils.distributed_utils.cudf | pandas.DataFrame
:canonical: utils.distributed_utils.read_single_partition

```{autodoc2-docstring} utils.distributed_utils.read_single_partition
```
````

````{py:function} seed_all(seed: int = 42) -> None
:canonical: utils.distributed_utils.seed_all

```{autodoc2-docstring} utils.distributed_utils.seed_all
```
````

````{py:function} select_columns(df: dask.dataframe.DataFrame | pandas.DataFrame | utils.distributed_utils.cudf, columns: list[str], file_type: typing.Literal[jsonl, json, parquet], add_filename: bool | str) -> dask.dataframe.DataFrame | pandas.DataFrame | utils.distributed_utils.cudf
:canonical: utils.distributed_utils.select_columns

```{autodoc2-docstring} utils.distributed_utils.select_columns
```
````

````{py:function} single_partition_write_with_filename(df: pandas.DataFrame | cudf.DataFrame, output_file_dir: str, keep_filename_column: bool = False, output_type: str = 'jsonl', filename_col: str = 'file_name', compression: str | None = None) -> cudf.Series | pandas.Series
:canonical: utils.distributed_utils.single_partition_write_with_filename

```{autodoc2-docstring} utils.distributed_utils.single_partition_write_with_filename
```
````

````{py:function} start_dask_cpu_local_cluster(n_workers: int | None = os.cpu_count(), threads_per_worker: int = 1, **cluster_kwargs) -> dask.distributed.Client
:canonical: utils.distributed_utils.start_dask_cpu_local_cluster

```{autodoc2-docstring} utils.distributed_utils.start_dask_cpu_local_cluster
```
````

````{py:function} start_dask_gpu_local_cluster(nvlink_only: bool = False, protocol: str = 'tcp', rmm_pool_size: int | str | None = '1024M', enable_spilling: bool = True, set_torch_to_use_rmm: bool = True, rmm_async: bool = True, rmm_maximum_pool_size: int | str | None = None, rmm_managed_memory: bool = False, rmm_release_threshold: int | str | None = None, **cluster_kwargs) -> dask.distributed.Client
:canonical: utils.distributed_utils.start_dask_gpu_local_cluster

```{autodoc2-docstring} utils.distributed_utils.start_dask_gpu_local_cluster
```
````

````{py:function} write_to_disk(df: dask.dataframe.DataFrame, output_path: str, write_to_filename: bool | str = False, keep_filename_column: bool = False, output_type: str = 'jsonl', partition_on: str | None = None, compression: str | None = None) -> None
:canonical: utils.distributed_utils.write_to_disk

```{autodoc2-docstring} utils.distributed_utils.write_to_disk
```
````
