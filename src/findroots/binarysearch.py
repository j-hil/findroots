import numpy as np

from findroots.functions import MathFunc
from findroots.types import FloatArray, FloatArrayLike, IntArray


def findroot(
    _f: MathFunc, /, *, on: FloatArrayLike, tol: FloatArrayLike
) -> tuple[FloatArray, IntArray]:
    """Use the binary search method to (try) find a root of the function.

    :param _f: Function to find root(s) of.
    :param on: Interval to search on. Must be a Nx2 array(like). If a 1x2 array
        is passed instead it will be treated as a Nx2 where all rows are identical.
    :param tol: Maximum truncation error of root. Must be Nx1 array(like). If 1x1 array
        passed instead, it will be treated as a Nx1 array with all values identical.
    :return: 1d array of roots found, and 1d array of corresponding number of iterations
        used in computation. When a root is not in the given interval `nan` is returned
        for the root, and `-1` for the number of iterations.
    """

    # ensure `intervals` is a Nx2 array
    intervals = np.array(on, dtype=float, ndmin=2)

    # number of input/output rows (called N in docs/comments)
    n = len(intervals)

    # ensure `tol` is Nx1 arrays
    tol = tol * np.ones((n,), dtype=float)

    # we permit the 'interval' (c, d) where c > d by replacing it with (d, c).
    intervals.sort()
    a, b = intervals.T

    # check a root is in the interval then do first step
    f_a, f_b = _f((a, b))
    root_exists = f_a * f_b < 0
    x = np.where(root_exists, (a + b) / 2, np.nan)
    f_x = _f(x)
    n_iters = np.where(root_exists, 0, -1)

    while True:

        # get info from arrays
        tol_not_met = b - a > tol
        continue_lower = tol_not_met & (f_a * f_x < 0)
        continue_upper = tol_not_met & (f_x * f_b < 0)

        # replace upper/lower bounds as appropriate
        b = np.where(continue_lower, x, b)
        a = np.where(continue_upper, x, a)
        # TODO: handle == case

        # increment iteration count & exit if done
        n_iters += np.where(tol_not_met & root_exists, 1, 0)
        if not np.any(tol_not_met * root_exists):
            break

        # perform next step
        x = (a + b) / 2
        f_a, f_x, f_b = _f((a, x, b))

        if any(n_iters > 1000):
            pass

    return x, n_iters


# TODO: investigate
# roots, _ = findroot(func2, on=((0,1), (3, 5)), tol=5e-10)