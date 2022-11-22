from typing import overload

import numpy as np

from findroots.types import Num, Numerical, Vec


@overload
def func1(x: Num) -> Num:
    ...


@overload
def func1(x: Vec) -> Vec:
    ...


def func1(x: Numerical) -> Numerical:
    """Compute F_1 = 2x - 2sin(x) + 5."""
    return 2 * x - 3 * np.sin(x) + 5


@overload
def func2(x: Num) -> Num:
    ...


@overload
def func2(x: Vec) -> Vec:
    ...


def func2(x: Numerical) -> Numerical:
    """Compute F_2 = x^3 - 8.5x^2 + 20x - 8."""
    return x**3 - 8.5 * x**2 + 20 * x - 8
