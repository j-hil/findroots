from typing import Any, Callable

import numpy as np
from numpy.typing import NDArray

Vec = NDArray[np.number[Any]]
Num = np.number | float
Numerical = Num | Vec
Signature = Callable[[Vec], Vec]
