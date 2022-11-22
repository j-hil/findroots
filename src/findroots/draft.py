from typing import Any, overload

import numpy as np
from numpy.typing import NDArray

Vector = NDArray[np.number[Any]]
Number = np.number[Any] | int | float
Numerical = Number | Vector


@overload
def func1(x: Number) -> Number:
    ...


@overload
def func1(x: Vector) -> Vector:
    ...


def func1(x: Numerical) -> Numerical:
    """Compute 2x - 2sin(x) + 5 as defined in (4)."""
    return 2 * x - 3 * np.sin(x) + 5


@overload
def func2(x: Number) -> Number:
    ...


@overload
def func2(x: Vector) -> Vector:
    ...


def func2(x: Numerical) -> Numerical:
    """Compute x^3 - 8.5x^2 + 20x - 8 = (x - .5)(x - 4)^2 as defined in (5)."""
    return x**3 - 8.5 * x**2 + 20 * x - 8
