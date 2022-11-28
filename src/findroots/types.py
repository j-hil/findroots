from typing import Any, Union

import numpy as np
from numpy.typing import NDArray

# Do not included parent class `np.number` as includes the (unordered) complex number
NpReal = np.floating[Any] | np.integer[Any]
Vec = NDArray[NpReal]

# These types could be expanded but they cover the cases I use.
# Note by using `float` we get `int` for free (see pep-0484).
Real = float | NpReal
VecLike = Vec | Real | tuple[float, ...] | list[float]

# newer `|` syntax for Union fails here :/
NumPair = Union[
    tuple[float, float],
    tuple[np.floating[Any], np.floating[Any]],
    tuple[np.integer[Any], np.integer[Any]],
]
