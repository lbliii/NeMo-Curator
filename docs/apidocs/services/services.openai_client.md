# {py:mod}`services.openai_client`

```{py:module} services.openai_client
```

```{autodoc2-docstring} services.openai_client
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AsyncOpenAIClient <services.openai_client.AsyncOpenAIClient>`
  - ```{autodoc2-docstring} services.openai_client.AsyncOpenAIClient
    :summary:
    ```
* - {py:obj}`OpenAIClient <services.openai_client.OpenAIClient>`
  - ```{autodoc2-docstring} services.openai_client.OpenAIClient
    :summary:
    ```
````

### API

`````{py:class} AsyncOpenAIClient(async_openai_client: openai.AsyncOpenAI)
:canonical: services.openai_client.AsyncOpenAIClient

Bases: {py:obj}`services.model_client.AsyncLLMClient`

```{autodoc2-docstring} services.openai_client.AsyncOpenAIClient
```

```{rubric} Initialization
```

```{autodoc2-docstring} services.openai_client.AsyncOpenAIClient.__init__
```

````{py:method} query_model(*, messages: collections.abc.Iterable, model: str, conversation_formatter: nemo_curator.services.conversation_formatter.ConversationFormatter | None = None, max_tokens: int | None | openai._types.NotGiven = NOT_GIVEN, n: int | None | openai._types.NotGiven = NOT_GIVEN, seed: int | None | openai._types.NotGiven = NOT_GIVEN, stop: str | None | list[str] | openai._types.NotGiven = NOT_GIVEN, stream: bool | None | openai._types.NotGiven = False, temperature: float | None | openai._types.NotGiven = NOT_GIVEN, top_k: int | None = None, top_p: float | None | openai._types.NotGiven = NOT_GIVEN) -> list[str]
:canonical: services.openai_client.AsyncOpenAIClient.query_model
:async:

```{autodoc2-docstring} services.openai_client.AsyncOpenAIClient.query_model
```

````

````{py:method} query_reward_model(*, messages: collections.abc.Iterable, model: str) -> dict
:canonical: services.openai_client.AsyncOpenAIClient.query_reward_model
:async:

```{autodoc2-docstring} services.openai_client.AsyncOpenAIClient.query_reward_model
```

````

`````

`````{py:class} OpenAIClient(openai_client: openai.OpenAI)
:canonical: services.openai_client.OpenAIClient

Bases: {py:obj}`services.model_client.LLMClient`

```{autodoc2-docstring} services.openai_client.OpenAIClient
```

```{rubric} Initialization
```

```{autodoc2-docstring} services.openai_client.OpenAIClient.__init__
```

````{py:method} query_model(*, messages: collections.abc.Iterable, model: str, conversation_formatter: nemo_curator.services.conversation_formatter.ConversationFormatter | None = None, max_tokens: int | None | openai._types.NotGiven = NOT_GIVEN, n: int | None | openai._types.NotGiven = NOT_GIVEN, seed: int | None | openai._types.NotGiven = NOT_GIVEN, stop: str | None | list[str] | openai._types.NotGiven = NOT_GIVEN, stream: bool | None | openai._types.NotGiven = False, temperature: float | None | openai._types.NotGiven = NOT_GIVEN, top_k: int | None = None, top_p: float | None | openai._types.NotGiven = NOT_GIVEN) -> list[str]
:canonical: services.openai_client.OpenAIClient.query_model

```{autodoc2-docstring} services.openai_client.OpenAIClient.query_model
```

````

````{py:method} query_reward_model(*, messages: collections.abc.Iterable, model: str) -> dict
:canonical: services.openai_client.OpenAIClient.query_reward_model

```{autodoc2-docstring} services.openai_client.OpenAIClient.query_reward_model
```

````

`````
