# {py:mod}`modifiers.unicode_reformatter`

```{py:module} modifiers.unicode_reformatter
```

```{autodoc2-docstring} modifiers.unicode_reformatter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`UnicodeReformatter <modifiers.unicode_reformatter.UnicodeReformatter>`
  - ```{autodoc2-docstring} modifiers.unicode_reformatter.UnicodeReformatter
    :summary:
    ```
````

### API

`````{py:class} UnicodeReformatter(config: ftfy.TextFixerConfig | None = None, unescape_html: str | bool = 'auto', remove_terminal_escapes: bool = True, fix_encoding: bool = True, restore_byte_a0: bool = True, replace_lossy_sequences: bool = True, decode_inconsistent_utf8: bool = True, fix_c1_controls: bool = True, fix_latin_ligatures: bool = False, fix_character_width: bool = False, uncurl_quotes: bool = False, fix_line_breaks: bool = False, fix_surrogates: bool = True, remove_control_chars: bool = True, normalization: typing.Literal[NFC, NFD, NFKC, NFKD] | None = None, max_decode_length: int = 1000000, explain: bool = True)
:canonical: modifiers.unicode_reformatter.UnicodeReformatter

Bases: {py:obj}`nemo_curator.modifiers.DocumentModifier`

```{autodoc2-docstring} modifiers.unicode_reformatter.UnicodeReformatter
```

```{rubric} Initialization
```

```{autodoc2-docstring} modifiers.unicode_reformatter.UnicodeReformatter.__init__
```

````{py:method} modify_document(text: str) -> str
:canonical: modifiers.unicode_reformatter.UnicodeReformatter.modify_document

```{autodoc2-docstring} modifiers.unicode_reformatter.UnicodeReformatter.modify_document
```

````

`````
