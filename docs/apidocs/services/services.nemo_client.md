# {py:mod}`services.nemo_client`

```{py:module} services.nemo_client
```

```{autodoc2-docstring} services.nemo_client
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NemoDeployClient <services.nemo_client.NemoDeployClient>`
  - ```{autodoc2-docstring} services.nemo_client.NemoDeployClient
    :summary:
    ```
````

### API

`````{py:class} NemoDeployClient(nemo_deploy: NemoQueryLLM)
:canonical: services.nemo_client.NemoDeployClient

Bases: {py:obj}`services.model_client.LLMClient`

```{autodoc2-docstring} services.nemo_client.NemoDeployClient
```

```{rubric} Initialization
```

```{autodoc2-docstring} services.nemo_client.NemoDeployClient.__init__
```

````{py:method} query_model(*, messages: collections.abc.Iterable, model: str, conversation_formatter: nemo_curator.services.conversation_formatter.ConversationFormatter | None = None, max_tokens: int | None = None, n: int | None = None, seed: int | None = None, stop: str | None | list[str] = [], stream: bool = False, temperature: float | None = None, top_k: int | None = None, top_p: float | None = None) -> list[str]
:canonical: services.nemo_client.NemoDeployClient.query_model

```{autodoc2-docstring} services.nemo_client.NemoDeployClient.query_model
```

````

````{py:method} query_reward_model(*, messages: collections.abc.Iterable, model: str) -> dict
:canonical: services.nemo_client.NemoDeployClient.query_reward_model

```{autodoc2-docstring} services.nemo_client.NemoDeployClient.query_reward_model
```

````

`````
