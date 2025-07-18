# {py:mod}`modules.fuzzy_dedup.minhash`

```{py:module} modules.fuzzy_dedup.minhash
```

```{autodoc2-docstring} modules.fuzzy_dedup.minhash
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MinHash <modules.fuzzy_dedup.minhash.MinHash>`
  - ```{autodoc2-docstring} modules.fuzzy_dedup.minhash.MinHash
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BIT_WIDTH_32 <modules.fuzzy_dedup.minhash.BIT_WIDTH_32>`
  - ```{autodoc2-docstring} modules.fuzzy_dedup.minhash.BIT_WIDTH_32
    :summary:
    ```
* - {py:obj}`BIT_WIDTH_64 <modules.fuzzy_dedup.minhash.BIT_WIDTH_64>`
  - ```{autodoc2-docstring} modules.fuzzy_dedup.minhash.BIT_WIDTH_64
    :summary:
    ```
````

### API

````{py:data} BIT_WIDTH_32
:canonical: modules.fuzzy_dedup.minhash.BIT_WIDTH_32
:value: >
   32

```{autodoc2-docstring} modules.fuzzy_dedup.minhash.BIT_WIDTH_32
```

````

````{py:data} BIT_WIDTH_64
:canonical: modules.fuzzy_dedup.minhash.BIT_WIDTH_64
:value: >
   64

```{autodoc2-docstring} modules.fuzzy_dedup.minhash.BIT_WIDTH_64
```

````

`````{py:class} MinHash(seed: int = 42, num_hashes: int = 260, char_ngrams: int = 24, use_64bit_hash: bool = False, logger: logging.LoggerAdapter | str = './', id_field: str = 'id', text_field: str = 'text', profile_dir: str | None = None, cache_dir: str | None = None)
:canonical: modules.fuzzy_dedup.minhash.MinHash

```{autodoc2-docstring} modules.fuzzy_dedup.minhash.MinHash
```

```{rubric} Initialization
```

```{autodoc2-docstring} modules.fuzzy_dedup.minhash.MinHash.__init__
```

````{py:method} generate_hash_permutation_seeds(bit_width: int, n_permutations: int = 260, seed: int = 0) -> numpy.ndarray
:canonical: modules.fuzzy_dedup.minhash.MinHash.generate_hash_permutation_seeds

```{autodoc2-docstring} modules.fuzzy_dedup.minhash.MinHash.generate_hash_permutation_seeds
```

````

````{py:method} minhash32(ser: cudf.Series, seeds: numpy.ndarray, char_ngram: int) -> cudf.Series
:canonical: modules.fuzzy_dedup.minhash.MinHash.minhash32

```{autodoc2-docstring} modules.fuzzy_dedup.minhash.MinHash.minhash32
```

````

````{py:method} minhash64(ser: cudf.Series, seeds: numpy.ndarray, char_ngram: int) -> cudf.Series
:canonical: modules.fuzzy_dedup.minhash.MinHash.minhash64

```{autodoc2-docstring} modules.fuzzy_dedup.minhash.MinHash.minhash64
```

````

`````
