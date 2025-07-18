# {py:mod}`tasks.metrics`

```{py:module} tasks.metrics
```

```{autodoc2-docstring} tasks.metrics
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ANLI <tasks.metrics.ANLI>`
  - ```{autodoc2-docstring} tasks.metrics.ANLI
    :summary:
    ```
* - {py:obj}`ArcChallenge <tasks.metrics.ArcChallenge>`
  - ```{autodoc2-docstring} tasks.metrics.ArcChallenge
    :summary:
    ```
* - {py:obj}`ArcEasy <tasks.metrics.ArcEasy>`
  - ```{autodoc2-docstring} tasks.metrics.ArcEasy
    :summary:
    ```
* - {py:obj}`BigBenchHard <tasks.metrics.BigBenchHard>`
  - ```{autodoc2-docstring} tasks.metrics.BigBenchHard
    :summary:
    ```
* - {py:obj}`BigBenchLight <tasks.metrics.BigBenchLight>`
  - ```{autodoc2-docstring} tasks.metrics.BigBenchLight
    :summary:
    ```
* - {py:obj}`BoolQ <tasks.metrics.BoolQ>`
  - ```{autodoc2-docstring} tasks.metrics.BoolQ
    :summary:
    ```
* - {py:obj}`CB <tasks.metrics.CB>`
  - ```{autodoc2-docstring} tasks.metrics.CB
    :summary:
    ```
* - {py:obj}`COQA <tasks.metrics.COQA>`
  - ```{autodoc2-docstring} tasks.metrics.COQA
    :summary:
    ```
* - {py:obj}`Copa <tasks.metrics.Copa>`
  - ```{autodoc2-docstring} tasks.metrics.Copa
    :summary:
    ```
* - {py:obj}`Drop <tasks.metrics.Drop>`
  - ```{autodoc2-docstring} tasks.metrics.Drop
    :summary:
    ```
* - {py:obj}`Lambada <tasks.metrics.Lambada>`
  - ```{autodoc2-docstring} tasks.metrics.Lambada
    :summary:
    ```
* - {py:obj}`MMLU <tasks.metrics.MMLU>`
  - ```{autodoc2-docstring} tasks.metrics.MMLU
    :summary:
    ```
* - {py:obj}`MultiRC <tasks.metrics.MultiRC>`
  - ```{autodoc2-docstring} tasks.metrics.MultiRC
    :summary:
    ```
* - {py:obj}`Multilingual <tasks.metrics.Multilingual>`
  - ```{autodoc2-docstring} tasks.metrics.Multilingual
    :summary:
    ```
* - {py:obj}`NumDasc <tasks.metrics.NumDasc>`
  - ```{autodoc2-docstring} tasks.metrics.NumDasc
    :summary:
    ```
* - {py:obj}`OpenBookQA <tasks.metrics.OpenBookQA>`
  - ```{autodoc2-docstring} tasks.metrics.OpenBookQA
    :summary:
    ```
* - {py:obj}`PIQA <tasks.metrics.PIQA>`
  - ```{autodoc2-docstring} tasks.metrics.PIQA
    :summary:
    ```
* - {py:obj}`Quac <tasks.metrics.Quac>`
  - ```{autodoc2-docstring} tasks.metrics.Quac
    :summary:
    ```
* - {py:obj}`RTE <tasks.metrics.RTE>`
  - ```{autodoc2-docstring} tasks.metrics.RTE
    :summary:
    ```
* - {py:obj}`Race <tasks.metrics.Race>`
  - ```{autodoc2-docstring} tasks.metrics.Race
    :summary:
    ```
* - {py:obj}`Record <tasks.metrics.Record>`
  - ```{autodoc2-docstring} tasks.metrics.Record
    :summary:
    ```
* - {py:obj}`Squad <tasks.metrics.Squad>`
  - ```{autodoc2-docstring} tasks.metrics.Squad
    :summary:
    ```
* - {py:obj}`StoryCloze <tasks.metrics.StoryCloze>`
  - ```{autodoc2-docstring} tasks.metrics.StoryCloze
    :summary:
    ```
* - {py:obj}`TriviaQA <tasks.metrics.TriviaQA>`
  - ```{autodoc2-docstring} tasks.metrics.TriviaQA
    :summary:
    ```
* - {py:obj}`WSC <tasks.metrics.WSC>`
  - ```{autodoc2-docstring} tasks.metrics.WSC
    :summary:
    ```
* - {py:obj}`WebQA <tasks.metrics.WebQA>`
  - ```{autodoc2-docstring} tasks.metrics.WebQA
    :summary:
    ```
* - {py:obj}`WiC <tasks.metrics.WiC>`
  - ```{autodoc2-docstring} tasks.metrics.WiC
    :summary:
    ```
* - {py:obj}`Winogrande <tasks.metrics.Winogrande>`
  - ```{autodoc2-docstring} tasks.metrics.Winogrande
    :summary:
    ```
````

### API

`````{py:class} ANLI(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.ANLI

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.ANLI
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.ANLI.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.ANLI.generate_ngrams

```{autodoc2-docstring} tasks.metrics.ANLI.generate_ngrams
```

````

`````

`````{py:class} ArcChallenge(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.ArcChallenge

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.ArcChallenge
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.ArcChallenge.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.ArcChallenge.generate_ngrams

```{autodoc2-docstring} tasks.metrics.ArcChallenge.generate_ngrams
```

````

`````

`````{py:class} ArcEasy(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.ArcEasy

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.ArcEasy
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.ArcEasy.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.ArcEasy.generate_ngrams

```{autodoc2-docstring} tasks.metrics.ArcEasy.generate_ngrams
```

````

`````

`````{py:class} BigBenchHard(path: str | None = None, min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.BigBenchHard

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.BigBenchHard
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.BigBenchHard.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.BigBenchHard.generate_ngrams

```{autodoc2-docstring} tasks.metrics.BigBenchHard.generate_ngrams
```

````

`````

`````{py:class} BigBenchLight(path: str | None = None, min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.BigBenchLight

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.BigBenchLight
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.BigBenchLight.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.BigBenchLight.generate_ngrams

```{autodoc2-docstring} tasks.metrics.BigBenchLight.generate_ngrams
```

````

`````

`````{py:class} BoolQ(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.BoolQ

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.BoolQ
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.BoolQ.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.BoolQ.generate_ngrams

```{autodoc2-docstring} tasks.metrics.BoolQ.generate_ngrams
```

````

`````

`````{py:class} CB(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.CB

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.CB
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.CB.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.CB.generate_ngrams

```{autodoc2-docstring} tasks.metrics.CB.generate_ngrams
```

````

`````

`````{py:class} COQA(file_path: str | None = None, min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.COQA

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.COQA
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.COQA.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.COQA.generate_ngrams

```{autodoc2-docstring} tasks.metrics.COQA.generate_ngrams
```

````

`````

`````{py:class} Copa(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.Copa

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.Copa
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.Copa.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.Copa.generate_ngrams

```{autodoc2-docstring} tasks.metrics.Copa.generate_ngrams
```

````

`````

`````{py:class} Drop(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.Drop

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.Drop
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.Drop.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.Drop.generate_ngrams

```{autodoc2-docstring} tasks.metrics.Drop.generate_ngrams
```

````

`````

`````{py:class} Lambada(file_path: str, min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.Lambada

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.Lambada
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.Lambada.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.Lambada.generate_ngrams

```{autodoc2-docstring} tasks.metrics.Lambada.generate_ngrams
```

````

`````

`````{py:class} MMLU(path: str | None = None, min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.MMLU

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.MMLU
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.MMLU.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.MMLU.generate_ngrams

```{autodoc2-docstring} tasks.metrics.MMLU.generate_ngrams
```

````

`````

`````{py:class} MultiRC(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.MultiRC

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.MultiRC
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.MultiRC.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.MultiRC.generate_ngrams

```{autodoc2-docstring} tasks.metrics.MultiRC.generate_ngrams
```

````

`````

`````{py:class} Multilingual(path: str | None = None, min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.Multilingual

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.Multilingual
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.Multilingual.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.Multilingual.generate_ngrams

```{autodoc2-docstring} tasks.metrics.Multilingual.generate_ngrams
```

````

`````

`````{py:class} NumDasc(n: int, file_path: str, min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.NumDasc

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.NumDasc
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.NumDasc.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.NumDasc.generate_ngrams

```{autodoc2-docstring} tasks.metrics.NumDasc.generate_ngrams
```

````

`````

`````{py:class} OpenBookQA(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.OpenBookQA

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.OpenBookQA
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.OpenBookQA.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.OpenBookQA.generate_ngrams

```{autodoc2-docstring} tasks.metrics.OpenBookQA.generate_ngrams
```

````

`````

`````{py:class} PIQA(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.PIQA

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.PIQA
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.PIQA.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.PIQA.generate_ngrams

```{autodoc2-docstring} tasks.metrics.PIQA.generate_ngrams
```

````

`````

`````{py:class} Quac(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.Quac

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.Quac
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.Quac.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.Quac.generate_ngrams

```{autodoc2-docstring} tasks.metrics.Quac.generate_ngrams
```

````

`````

`````{py:class} RTE(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.RTE

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.RTE
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.RTE.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.RTE.generate_ngrams

```{autodoc2-docstring} tasks.metrics.RTE.generate_ngrams
```

````

`````

`````{py:class} Race(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.Race

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.Race
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.Race.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.Race.generate_ngrams

```{autodoc2-docstring} tasks.metrics.Race.generate_ngrams
```

````

`````

`````{py:class} Record(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.Record

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.Record
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.Record.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.Record.generate_ngrams

```{autodoc2-docstring} tasks.metrics.Record.generate_ngrams
```

````

`````

`````{py:class} Squad(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.Squad

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.Squad
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.Squad.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.Squad.generate_ngrams

```{autodoc2-docstring} tasks.metrics.Squad.generate_ngrams
```

````

`````

`````{py:class} StoryCloze(file_path: str, min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.StoryCloze

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.StoryCloze
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.StoryCloze.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.StoryCloze.generate_ngrams

```{autodoc2-docstring} tasks.metrics.StoryCloze.generate_ngrams
```

````

`````

`````{py:class} TriviaQA(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.TriviaQA

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.TriviaQA
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.TriviaQA.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.TriviaQA.generate_ngrams

```{autodoc2-docstring} tasks.metrics.TriviaQA.generate_ngrams
```

````

`````

`````{py:class} WSC(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.WSC

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.WSC
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.WSC.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.WSC.generate_ngrams

```{autodoc2-docstring} tasks.metrics.WSC.generate_ngrams
```

````

`````

`````{py:class} WebQA(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.WebQA

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.WebQA
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.WebQA.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.WebQA.generate_ngrams

```{autodoc2-docstring} tasks.metrics.WebQA.generate_ngrams
```

````

`````

`````{py:class} WiC(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.WiC

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.WiC
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.WiC.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.WiC.generate_ngrams

```{autodoc2-docstring} tasks.metrics.WiC.generate_ngrams
```

````

`````

`````{py:class} Winogrande(min_ngram_size: int = 8, max_ngram_size: int = 13)
:canonical: tasks.metrics.Winogrande

Bases: {py:obj}`nemo_curator.tasks.downstream_task.DownstreamTask`

```{autodoc2-docstring} tasks.metrics.Winogrande
```

```{rubric} Initialization
```

```{autodoc2-docstring} tasks.metrics.Winogrande.__init__
```

````{py:method} generate_ngrams() -> dict[str, int]
:canonical: tasks.metrics.Winogrande.generate_ngrams

```{autodoc2-docstring} tasks.metrics.Winogrande.generate_ngrams
```

````

`````
