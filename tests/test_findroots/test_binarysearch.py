import numpy as np
from numpy.testing import assert_allclose, assert_equal

from findroots.binarysearch import findroot
from findroots.functions import func1, func2


def test_vectorization() -> None:
    # baseline results from a run I'm confident of
    expected_roots = (
        -2.88323617,
        -2.88323841,
        -2.88323783,
        -2.88323779,
        -2.88323583,
        -2.88323853,
        -2.88323827,
        -2.88323617,
        -2.88323858,
        -2.88323535,
    )
    expected_n_iters = (22, 22, 21, 22, 20, 21, 21, 22, 21, 21)

    # `func1` has simple root on (-4, 1) which intersects with each of these intervals
    intervals = (
        (1.1209, -12.3633),
        (-11.0574, 3.4692),
        (0.8966, -6.6580),
        (6.0044, -12.3111),
        (-4.0883, -0.0737),
        (-7.4795, 0.5941),
        (0.1020, -9.7478),
        (6.1949, -6.1923),
        (-1.2946, -8.5238),
        (2.0253, -7.8981),
    )
    tolerance = 5e-6
    root_estimates, n_iters = findroot(func1, on=intervals, tol=tolerance)

    assert_allclose(root_estimates, expected_roots, atol=tolerance)
    assert_equal(n_iters, expected_n_iters)


def test_distinct_roots() -> None:
    # `func2` has a simple root at 0.5 and a double root at 4.
    # expect only the former to be found
    tolerance = 1e-5
    roots, _ = findroot(func2, on=((0, 1), (3, 5)), tol=tolerance)

    assert_allclose(roots, (0.5, np.nan), atol=tolerance)


def test_no_roots() -> None:
    # `func1` has no root on the interval (1, 2) so expect a nan
    root, n_iters = findroot(func1, on=(1, 2), tol=1e-5)

    assert_equal(root, np.array(np.nan))
    assert_equal(n_iters, -1)
