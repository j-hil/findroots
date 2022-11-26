from typing import overload

import latexify
import numpy as np

from findroots.types import Num, Numerical, Vec


@overload
def func1(x: Num) -> Num:
    ...


@overload
def func1(x: Vec) -> Vec:
    ...


@latexify.expression
def func1(x: Numerical) -> Numerical:
    return 2 * x - 3 * np.sin(x) + 5


@overload
def func2(x: Num) -> Num:
    ...


@overload
def func2(x: Vec) -> Vec:
    ...


@latexify.expression
def func2(x: Numerical) -> Numerical:
    return x**3 - 8.5 * x**2 + 20 * x - 8


def _main() -> None:
    # TODO: get this working!

    # type hinter should hate this (and will warn if ignore is unnecessary)
    func1("")  # type: ignore
    # type hinter should accept both of these:
    func1(np.array((1, 2, 3)))
    func2(1)


if __name__ == "__name__":
    _main()
