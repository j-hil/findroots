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
        np.nan,
    )
    expected_n_iters = (23, 23, 22, 23, 21, 22, 22, 23, 22, 22, -1)  # TODO: add 1

    # `func1` has simple root on (-4, 1) which intersects with some of these intervals
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
        (5, 6),
    )
    tolerance = 5e-6
    root_estimates, n_iters = findroot(func1, on=intervals, tol=tolerance)

    assert_allclose(root_estimates, expected_roots, atol=tolerance)
    assert_equal(n_iters, expected_n_iters)


def test_exact_root() -> None:
    # `func2` has a simple root at 0.5 and a double root at 4.
    # expect only the former to be found.
    # For former root is exactly halfway in the interval so expect 1 iteration
    tolerance = 1e-5
    roots, n_iters = findroot(func2, on=((0, 1), (3, 5)), tol=tolerance)

    assert_allclose(roots, (0.5, np.nan), atol=tolerance)
    assert_equal(n_iters, [1, -1])


def test_no_roots() -> None:
    # `func1` has no root on the interval (1, 2) so expect a nan
    root, n_iters = findroot(func1, on=(1, 2), tol=1e-5)

    assert_equal(root, np.array(np.nan))
    assert_equal(n_iters, -1)
