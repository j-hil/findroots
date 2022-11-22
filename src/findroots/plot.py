import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

from findroots.types import Num, Signature


def plot(_f: Signature, *, on: tuple[Num, Num], step: Num) -> Figure:
    xvals = np.arange(*on, step)
    yvals = _f(xvals)

    # TODO: look into mechanics of how subplots work
    fig, ax = plt.subplots()
    ax.plot(xvals, yvals)

    ax.grid(True, which="both")
    ax.axhline(y=0, color="k")
    ax.axvline(x=0, color="k")
    return fig
