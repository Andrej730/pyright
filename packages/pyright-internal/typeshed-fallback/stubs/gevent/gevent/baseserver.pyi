from collections.abc import Callable, Container
from types import TracebackType
from typing import Any, Generic, Literal, Protocol
from typing_extensions import ParamSpec, Self, TypeAlias

from gevent._types import _Loop
from gevent.pool import Pool
from gevent.socket import socket as _GeventSocket
from greenlet import greenlet

_P = ParamSpec("_P")

class _SpawnFunc(Protocol):
    def __call__(self, func: Callable[_P, object], /, *args: _P.args, **kwargs: _P.kwargs) -> greenlet: ...

_Spawner: TypeAlias = Pool | _SpawnFunc | int | Literal["default"] | None

class BaseServer(Generic[_P]):
    min_delay: float
    max_delay: float
    max_accept: int
    stop_timeout: float
    fatal_errors: Container[int]
    pool: Pool | None
    delay: float
    loop: _Loop
    family: int
    address: str | tuple[str, int]
    socket: _GeventSocket
    handle: Callable[..., object]
    def __init__(
        self,
        listener: _GeventSocket | tuple[str, int] | str,
        handle: Callable[_P, object] | None = None,
        spawn: _Spawner = "default",
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None, /) -> None: ...
    def set_listener(self, listener: _GeventSocket | tuple[str, int] | str) -> None: ...
    def set_spawn(self, spawn: _Spawner) -> None: ...
    def set_handle(self, handle: Callable[_P, object]) -> None: ...
    def start_accepting(self) -> None: ...
    def stop_accepting(self) -> None: ...
    # neither of these accept keyword arguments, but if we omit them, then ParamSpec
    # won't match the arguments correctly
    def do_handle(self, *args: _P.args, **_: _P.kwargs) -> None: ...
    def do_close(self, *args: _P.args, **_: _P.kwargs) -> None: ...
    # we would like to return _P.args here, however pyright will complain
    # mypy doesn't seem to mind
    def do_read(self) -> tuple[Any, ...] | None: ...
    def full(self) -> bool: ...
    @property
    def server_host(self) -> str | None: ...
    @property
    def server_port(self) -> int | None: ...
    def init_socket(self) -> None: ...
    @property
    def started(self) -> bool: ...
    def start(self) -> None: ...
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def stop(self, timeout: float | None = None) -> None: ...
    def serve_forever(self, stop_timeout: float | None = None) -> None: ...
    def is_fatal_error(self, ex: BaseException) -> bool: ...

__all__ = ["BaseServer"]
