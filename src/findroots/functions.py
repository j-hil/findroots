from typing import Callable

import latexify
import numpy as np

from findroots.types import FloatArray, FloatArrayLike


class MathFunc:
    """A simple math function."""

    def __init__(self, _f: Callable[[FloatArray], FloatArrayLike]) -> None:
        self._f = _f
        self._latex = str(latexify.expression(self._f))

    def __call__(self, x: FloatArrayLike) -> FloatArray:
        return np.array(self._f(np.array(x, dtype=float)), dtype=float)

    def __str__(self) -> str:
        return self._latex


def math_func(_f: Callable[[FloatArray], FloatArrayLike], /) -> MathFunc:
    """Decorate a math function to expand typing add latex str.

    For simple math functions this will expand input types and narrow output types.
    Specifically
        `(FloatVec) -> FloatVecLike` becomes `(FloatVecLike) -> FloatVec`.
    Additionally the `__str__` will now return a latex representation of the function.
    """
    # implemented in `MathFunc`
    return MathFunc(_f)


@math_func
def func1(x: FloatArray) -> FloatArrayLike:
    return 2 * x - 3 * np.sin(x) + 5


@math_func
def func2(x: FloatArray) -> FloatArrayLike:
    return x**3 - 8.5 * x**2 + 20 * x - 8


def _main() -> None:
    # script to test the typing is working as expected

    # type hinter should hate this (and will warn if ignore is unnecessary)
    func1("")  # type: ignore
    # type hinter should accept both of these:
    func1(np.array((1, 2, 3)))
    func2(1)


if __name__ == "__name__":
    _main()
