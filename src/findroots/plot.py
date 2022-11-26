import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

from findroots.types import Num, Signature, Vec


def plot(_f: Signature, /, *, on: tuple[Num, Num], step: Num) -> Figure:

    xmin, xmax = sorted(on)  # TODO: pylance hates this
    xvals: Vec = np.arange(xmin, xmax, step)
    yvals = _f(xvals)
    ymin, ymax = yvals.min(), yvals.max()

    fig, ax = plt.subplots()
    ax.plot(xvals, yvals)

    # aesthetics
    ax.set_title(f"$y = {_f}$ on interval ${xmin, xmax}$")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_xbound(xmin, xmax)
    ax.set_ybound(ymin, ymax)
    ax.grid(True, which="both")
    if xmin < 0 < xmax:
        ax.axvline(x=0, color="k", lw=0.75)
    if ymin < 0 < ymax:
        ax.axhline(y=0, color="k", lw=0.75)

    return fig


def _main() -> None:
    # test plot
    from findroots.functions import func1

    plt.rcParams.update({"text.usetex": True})
    plot(func1, on=(-4, -1), step=1e-5)
    plt.show()


if __name__ == "__main__":
    _main()
