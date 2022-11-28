import numpy as np

from findroots.functions import MathFunc, func1
from findroots.types import NumPair, Real


def findroot(_f: MathFunc, /, *, on: NumPair, tol: Real) -> tuple[Real, int]:
    """Use the binary search method to (try) find a root of the function.

    :param _f: Function to find root of
    :param on: Interval to search on
    :param tol: Maximum truncation error of root
    :return: approximate root & number of iterations used
    """
    a, b = np.sort(on)

    # our approximate root
    x = (a + b) / 2.0
    f_a, f_x, f_b = _f((a, x, b))

    n_iters = 0
    while b - a > tol:
        if f_a * f_x < 0:
            b = x
        elif f_x * f_b < 0:
            a = x
        elif f_x == 0:
            return x
        else:
            # root not found in interval, or serious logic/math flaw if n_iters > 0
            return np.nan, n_iters

        x = (a + b) / 2
        f_a, f_x, f_b = _f((a, x, b))
        n_iters += 1

    return x, n_iters


def _main() -> None:
    root, n_iters = findroot(func1, on=(-4, 1), tol=1e-5)
    print(f"{root=}, {n_iters=}")
    print("expect -2.8832... and n~20")


if __name__ == "__main__":
    _main()
