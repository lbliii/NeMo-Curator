# {py:mod}`services.model_client`

```{py:module} services.model_client
```

```{autodoc2-docstring} services.model_client
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AsyncLLMClient <services.model_client.AsyncLLMClient>`
  - ```{autodoc2-docstring} services.model_client.AsyncLLMClient
    :summary:
    ```
* - {py:obj}`LLMClient <services.model_client.LLMClient>`
  - ```{autodoc2-docstring} services.model_client.LLMClient
    :summary:
    ```
````

### API

`````{py:class} AsyncLLMClient
:canonical: services.model_client.AsyncLLMClient

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} services.model_client.AsyncLLMClient
```

````{py:method} query_model(*, messages: collections.abc.Iterable, model: str, conversation_formatter: nemo_curator.services.conversation_formatter.ConversationFormatter | None = None, max_tokens: int | None = None, n: int | None = 1, seed: int | None = None, stop: str | None | list[str] = None, stream: bool = False, temperature: float | None = None, top_k: int | None = None, top_p: float | None = None) -> list[str]
:canonical: services.model_client.AsyncLLMClient.query_model
:abstractmethod:
:async:

```{autodoc2-docstring} services.model_client.AsyncLLMClient.query_model
```

````

````{py:method} query_reward_model(*, messages: collections.abc.Iterable, model: str, conversation_formatter: nemo_curator.services.conversation_formatter.ConversationFormatter | None = None) -> dict
:canonical: services.model_client.AsyncLLMClient.query_reward_model
:abstractmethod:
:async:

```{autodoc2-docstring} services.model_client.AsyncLLMClient.query_reward_model
```

````

`````

`````{py:class} LLMClient
:canonical: services.model_client.LLMClient

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} services.model_client.LLMClient
```

````{py:method} query_model(*, messages: collections.abc.Iterable, model: str, conversation_formatter: nemo_curator.services.conversation_formatter.ConversationFormatter | None = None, max_tokens: int | None = None, n: int | None = 1, seed: int | None = None, stop: str | None | list[str] = None, stream: bool = False, temperature: float | None = None, top_k: int | None = None, top_p: float | None = None) -> list[str]
:canonical: services.model_client.LLMClient.query_model
:abstractmethod:

```{autodoc2-docstring} services.model_client.LLMClient.query_model
```

````

````{py:method} query_reward_model(*, messages: collections.abc.Iterable, model: str, conversation_formatter: nemo_curator.services.conversation_formatter.ConversationFormatter | None = None) -> dict
:canonical: services.model_client.LLMClient.query_reward_model
:abstractmethod:

```{autodoc2-docstring} services.model_client.LLMClient.query_reward_model
```

````

`````
