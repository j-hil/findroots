from typing import Any, Callable

import numpy as np
from numpy.typing import NDArray

Vec = NDArray[np.number[Any]]
Num = np.number[Any] | int | float
Numerical = Num | Vec
Signature = Callable[[Vec], Vec]
