from typing import Any, Union

import numpy as np
from numpy.typing import NDArray

Float = float | np.floating[Any]
Int = int | np.integer[Any]
Real = Union[Float, Int]

FloatArray = NDArray[np.floating[Any]]
IntArray = NDArray[np.integer[Any]]

# Anything that can be converted to `FloatArray` with `np.array(..., type=float)`
# NOTE: Far from a complete list - just the ones I use
FloatArrayLike = (
    FloatArray
    | Real
    | IntArray
    | list[Real]
    | tuple[Real, ...]
    | tuple[tuple[Real, ...], ...]
    | tuple[FloatArray, ...]
)

# newer `|` syntax for Union fails here :/
RealPair = Union[
    tuple[float, float],
    tuple[np.floating[Any], np.floating[Any]],
    tuple[np.integer[Any], np.integer[Any]],
]
