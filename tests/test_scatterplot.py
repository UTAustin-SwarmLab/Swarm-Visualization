from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np
import pytest

from swarm_visualizer.scatterplot import (
    plot_basic_scatterplot,
    plot_scatter_pdf_plot,
)
from swarm_visualizer.utility.general_utils import save_fig, set_plot_properties

_X_DATA = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)
_Y_DATA = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)


_SAVE_LOC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "example_plots")
)


@pytest.mark.parametrize(("x_data", "y_data"), [(_X_DATA, _Y_DATA)])
def test_basic_scatterplot(x_data, y_data) -> None:
    """Tests basic scatterplot.

    :param x_data: x-axis data
    :param y_data: y-axis data
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))

    # Create a  basic scatter plot
    plot_basic_scatterplot(
        x=x_data,
        y=y_data,
        title_str="Basic Scatter Plot",
        ylabel="$y$",
        lw=3.0,
        ylim=None,
        xlabel="$x$",
        xlim=None,
        ms=10.0,
        color="b",
        ax=ax,
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "scatterplots", "basic_scatterplot.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(("x_data", "y_data"), [(_X_DATA, _Y_DATA)])
def test_scatter_pdf_plot(x_data, y_data) -> None:
    """Tests scatterplot with CDFs.

    :param x_data: x-axis data
    :param y_data: y-axis data
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    # Create a scatter plot with CDFs
    fig = plot_scatter_pdf_plot(
        x=x_data,
        y=y_data,
        title_str="Scatter Plot with CDFs",
        ylabel="$y$",
        ylim=None,
        xlabel="$x$",
        xlim=None,
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "scatterplots", "scatter_pdf_plot.png")
    save_fig(fig, save_loc, dpi=600)
