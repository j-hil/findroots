from typing import Callable, ParamSpec, TypeVar

_RetType = TypeVar("_RetType")
_Params = ParamSpec("_Params")

def expression(f: Callable[_Params, _RetType]) -> Callable[_Params, _RetType]: ...
