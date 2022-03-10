from abc import abstractmethod
from collections import MutableMapping
from typing import Any

class SequenceGenerator:
    length: Any
    requested_entropy: str
    rng: Any
    @property
    @abstractmethod
    def symbol_count(self) -> int: ...
    def __init__(self, entropy: Any | None = ..., length: Any | None = ..., rng: Any | None = ..., **kwds) -> None: ...
    @property
    def entropy_per_symbol(self) -> float: ...
    @property
    def entropy(self) -> float: ...
    def __next__(self) -> None: ...
    def __call__(self, returns: Any | None = ...): ...
    def __iter__(self): ...

default_charsets: Any

class WordGenerator(SequenceGenerator):
    charset: str
    chars: Any
    def __init__(self, chars: Any | None = ..., charset: Any | None = ..., **kwds) -> None: ...
    @property
    def symbol_count(self): ...
    def __next__(self): ...

def genword(entropy: Any | None = ..., length: Any | None = ..., returns: Any | None = ..., **kwds): ...

class WordsetDict(MutableMapping[Any, Any]):
    paths: Any
    def __init__(self, *args, **kwds) -> None: ...
    def __getitem__(self, key): ...
    def set_path(self, key, path) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    def __contains__(self, key): ...

default_wordsets: Any

class PhraseGenerator(SequenceGenerator):
    wordset: str
    words: Any
    sep: str
    def __init__(self, wordset: Any | None = ..., words: Any | None = ..., sep: Any | None = ..., **kwds) -> None: ...
    @property
    def symbol_count(self): ...
    def __next__(self): ...

def genphrase(entropy: Any | None = ..., length: Any | None = ..., returns: Any | None = ..., **kwds): ...
