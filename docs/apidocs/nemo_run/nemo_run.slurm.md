# {py:mod}`nemo_run.slurm`

```{py:module} nemo_run.slurm
```

```{autodoc2-docstring} nemo_run.slurm
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SlurmJobConfig <nemo_run.slurm.SlurmJobConfig>`
  - ```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`run <nemo_run.slurm.run>`
  - ```{autodoc2-docstring} nemo_run.slurm.run
    :summary:
    ```
````

### API

`````{py:class} SlurmJobConfig
:canonical: nemo_run.slurm.SlurmJobConfig

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig
```

````{py:attribute} container_entrypoint
:canonical: nemo_run.slurm.SlurmJobConfig.container_entrypoint
:type: str
:value: >
   None

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.container_entrypoint
```

````

````{py:attribute} cpu_worker_memory_limit
:canonical: nemo_run.slurm.SlurmJobConfig.cpu_worker_memory_limit
:type: str
:value: >
   '0'

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.cpu_worker_memory_limit
```

````

````{py:attribute} cudf_spill
:canonical: nemo_run.slurm.SlurmJobConfig.cudf_spill
:type: str
:value: >
   '1'

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.cudf_spill
```

````

````{py:attribute} device
:canonical: nemo_run.slurm.SlurmJobConfig.device
:type: str
:value: >
   'cpu'

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.device
```

````

````{py:attribute} interface
:canonical: nemo_run.slurm.SlurmJobConfig.interface
:type: str
:value: >
   'eth0'

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.interface
```

````

````{py:attribute} job_dir
:canonical: nemo_run.slurm.SlurmJobConfig.job_dir
:type: str
:value: >
   None

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.job_dir
```

````

````{py:attribute} libcudf_cufile_policy
:canonical: nemo_run.slurm.SlurmJobConfig.libcudf_cufile_policy
:type: str
:value: >
   'OFF'

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.libcudf_cufile_policy
```

````

````{py:attribute} protocol
:canonical: nemo_run.slurm.SlurmJobConfig.protocol
:type: str
:value: >
   'tcp'

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.protocol
```

````

````{py:attribute} rapids_no_initialize
:canonical: nemo_run.slurm.SlurmJobConfig.rapids_no_initialize
:type: str
:value: >
   '1'

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.rapids_no_initialize
```

````

````{py:attribute} rmm_scheduler_pool_size
:canonical: nemo_run.slurm.SlurmJobConfig.rmm_scheduler_pool_size
:type: str
:value: >
   '1GB'

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.rmm_scheduler_pool_size
```

````

````{py:attribute} rmm_worker_pool_size
:canonical: nemo_run.slurm.SlurmJobConfig.rmm_worker_pool_size
:type: str
:value: >
   '72GiB'

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.rmm_worker_pool_size
```

````

````{py:attribute} script_command
:canonical: nemo_run.slurm.SlurmJobConfig.script_command
:type: str
:value: >
   None

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.script_command
```

````

````{py:method} to_script(add_scheduler_file: bool = True, add_device: bool = True) -> nemo_run.slurm.run
:canonical: nemo_run.slurm.SlurmJobConfig.to_script

```{autodoc2-docstring} nemo_run.slurm.SlurmJobConfig.to_script
```

````

`````

````{py:data} run
:canonical: nemo_run.slurm.run
:value: >
   'safe_import(...)'

```{autodoc2-docstring} nemo_run.slurm.run
```

````
