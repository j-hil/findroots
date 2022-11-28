from typing import Callable

import latexify
import numpy as np

from findroots.types import Vec, VecLike


class MathFunc:
    """A simple math function."""

    def __init__(self, _f: Callable[[Vec], Vec]) -> None:
        self._f = _f
        self._latex = str(latexify.expression(self._f))

    def __call__(self, x: VecLike) -> Vec:
        return self._f(np.array(x))

    def __str__(self) -> str:
        return self._latex


def math_func(_f: Callable[[Vec], Vec], /) -> MathFunc:
    """Expand typing and str of a math function.

    For simple mathematic functions this will expand the typing inputs from just `Vec`
    `VecLike` and replace the typical `str` with a latex representation of the function.
    """
    # implemented in `MathFunc`
    return MathFunc(_f)


@math_func
def func1(x: Vec) -> Vec:
    return 2 * x - 3 * np.sin(x) + 5


@math_func
def func2(x: Vec) -> Vec:
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
