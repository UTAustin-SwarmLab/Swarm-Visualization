from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np
import pytest

from swarm_visualizer.lineplot import plot_basic_lineplot, plot_overlaid_lineplot
from swarm_visualizer.utility.general_utils import save_fig, set_plot_properties

_X_DATA = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)
_Y_DATA = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)

_SIN_DATA = np.sin(_X_DATA)
_COS_DATA = np.cos(_Y_DATA)

# Normalized time series dictionary
_NORMALIZED_DICT = {
    "$x$": {
        "x": np.arange(0, 10, 0.1),
        "y": _X_DATA,
        "lw": 3.0,
        "linestyle": "-",
        "color": "b",
    },
    "$y$": {
        "x": np.arange(0, 10, 0.1),
        "y": _Y_DATA,
        "lw": 3.0,
        "linestyle": "-",
        "color": "r",
    },
    "$\\sin$": {
        "x": np.arange(0, 10, 0.1),
        "y": _SIN_DATA,
        "lw": 3.0,
        "linestyle": "-",
        "color": "g",
        "zorder": 2,
    },
    "$\\cos$": {
        "x": np.arange(0, 10, 0.1),
        "y": _COS_DATA,
        "lw": 3.0,
        "linestyle": "-",
        "color": "k",
        "zorder": 10,
    },
}


_SAVE_LOC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "example_plots")
)


@pytest.mark.parametrize(("y_data"), ([_Y_DATA]))
def test_basic_lineplot(y_data) -> None:
    """Tests basic time series plot.

    :param y_data: time series
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot time series
    plot_basic_lineplot(
        y=y_data,
        title_str="Basic Line Plot",
        ylabel="$y$",
        lw=3.0,
        ylim=None,
        xlabel="$x$",
        ax=ax,
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "lineplots", "basic_lineplot.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(("normalized_dict"), ([_NORMALIZED_DICT]))
def test_overlaid_lineplot(normalized_dict) -> None:
    """Tests overlaid time series plot.

    :param normalized_dict: dictionary with time series to plot
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot overlaid time series
    plot_overlaid_lineplot(
        normalized_dict=normalized_dict,
        title_str="Overlaid Line Plot",
        ylabel="$y$",
        xlabel="$x$",
        xticks=None,
        ylim=None,
        DEFAULT_ALPHA=1.0,
        legend_present=True,
        DEFAULT_MARKERSIZE=15,
        delete_yticks=False,
        ax=ax,
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "lineplots", "overlaid_lineplot.png")
    save_fig(fig, save_loc, dpi=600)
