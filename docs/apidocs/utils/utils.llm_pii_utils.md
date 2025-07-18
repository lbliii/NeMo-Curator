# {py:mod}`utils.llm_pii_utils`

```{py:module} utils.llm_pii_utils
```

```{autodoc2-docstring} utils.llm_pii_utils
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EntitySpan <utils.llm_pii_utils.EntitySpan>`
  - ```{autodoc2-docstring} utils.llm_pii_utils.EntitySpan
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`find_entity_spans <utils.llm_pii_utils.find_entity_spans>`
  - ```{autodoc2-docstring} utils.llm_pii_utils.find_entity_spans
    :summary:
    ```
* - {py:obj}`fix_overlaps <utils.llm_pii_utils.fix_overlaps>`
  - ```{autodoc2-docstring} utils.llm_pii_utils.fix_overlaps
    :summary:
    ```
* - {py:obj}`get_system_prompt <utils.llm_pii_utils.get_system_prompt>`
  - ```{autodoc2-docstring} utils.llm_pii_utils.get_system_prompt
    :summary:
    ```
* - {py:obj}`redact <utils.llm_pii_utils.redact>`
  - ```{autodoc2-docstring} utils.llm_pii_utils.redact
    :summary:
    ```
* - {py:obj}`validate_entity <utils.llm_pii_utils.validate_entity>`
  - ```{autodoc2-docstring} utils.llm_pii_utils.validate_entity
    :summary:
    ```
* - {py:obj}`validate_keys <utils.llm_pii_utils.validate_keys>`
  - ```{autodoc2-docstring} utils.llm_pii_utils.validate_keys
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`JSON_SCHEMA <utils.llm_pii_utils.JSON_SCHEMA>`
  - ```{autodoc2-docstring} utils.llm_pii_utils.JSON_SCHEMA
    :summary:
    ```
* - {py:obj}`PII_LABELS <utils.llm_pii_utils.PII_LABELS>`
  - ```{autodoc2-docstring} utils.llm_pii_utils.PII_LABELS
    :summary:
    ```
````

### API

`````{py:class} EntitySpan
:canonical: utils.llm_pii_utils.EntitySpan

```{autodoc2-docstring} utils.llm_pii_utils.EntitySpan
```

````{py:attribute} end_position
:canonical: utils.llm_pii_utils.EntitySpan.end_position
:type: int
:value: >
   None

```{autodoc2-docstring} utils.llm_pii_utils.EntitySpan.end_position
```

````

````{py:attribute} entity_type
:canonical: utils.llm_pii_utils.EntitySpan.entity_type
:type: str
:value: >
   None

```{autodoc2-docstring} utils.llm_pii_utils.EntitySpan.entity_type
```

````

````{py:attribute} start_position
:canonical: utils.llm_pii_utils.EntitySpan.start_position
:type: int
:value: >
   None

```{autodoc2-docstring} utils.llm_pii_utils.EntitySpan.start_position
```

````

`````

````{py:data} JSON_SCHEMA
:canonical: utils.llm_pii_utils.JSON_SCHEMA
:value: >
   None

```{autodoc2-docstring} utils.llm_pii_utils.JSON_SCHEMA
```

````

````{py:data} PII_LABELS
:canonical: utils.llm_pii_utils.PII_LABELS
:value: >
   ['medical_record_number', 'location', 'address', 'ssn', 'date_of_birth', 'date_time', 'name', 'email...

```{autodoc2-docstring} utils.llm_pii_utils.PII_LABELS
```

````

````{py:function} find_entity_spans(text: str, entities: list[dict[str, str]]) -> list[utils.llm_pii_utils.EntitySpan]
:canonical: utils.llm_pii_utils.find_entity_spans

```{autodoc2-docstring} utils.llm_pii_utils.find_entity_spans
```
````

````{py:function} fix_overlaps(spans: list[utils.llm_pii_utils.EntitySpan]) -> list[utils.llm_pii_utils.EntitySpan]
:canonical: utils.llm_pii_utils.fix_overlaps

```{autodoc2-docstring} utils.llm_pii_utils.fix_overlaps
```
````

````{py:function} get_system_prompt(pii_labels: list[str] = PII_LABELS) -> str
:canonical: utils.llm_pii_utils.get_system_prompt

```{autodoc2-docstring} utils.llm_pii_utils.get_system_prompt
```
````

````{py:function} redact(full_text: str, pii_entities: list[dict[str, str]]) -> str
:canonical: utils.llm_pii_utils.redact

```{autodoc2-docstring} utils.llm_pii_utils.redact
```
````

````{py:function} validate_entity(entity: dict[str, str], text: str, min_length: int = 2) -> bool
:canonical: utils.llm_pii_utils.validate_entity

```{autodoc2-docstring} utils.llm_pii_utils.validate_entity
```
````

````{py:function} validate_keys(entity_dict: dict) -> bool
:canonical: utils.llm_pii_utils.validate_keys

```{autodoc2-docstring} utils.llm_pii_utils.validate_keys
```
````
