from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from swarm_visualizer.histogram import (
    plot_pdf,
    plot_several_pdf,
)
from swarm_visualizer.utility import save_fig, set_plot_properties

# Example Plots location
_X1_DATA = np.arange(0, 5, 0.05) + np.random.normal(0, 0.1, 100)
_X2_DATA = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)

# Concatenate the data
_X_DATA = [_X1_DATA, _X2_DATA]
_X_LABEL = ["$x_%d$" % i for i in range(5)]
_DATA_FRAME = pd.DataFrame(
    {"$y_1$": _X1_DATA[:5], "$y_2$": _X1_DATA[:5] + 0.02, "$x$": _X_LABEL}
)

_SAVE_LOC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "example_plots")
)


@pytest.mark.parametrize(("data"), [(_X1_DATA)])
def test_plot_pdf(data) -> None:
    """Tests plot pdf.

    :param data: data 
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot PDF
    plot_pdf(data=data, xlabel="$x$", title_str="PDF", ax=ax)

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "histograms", "pdf.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(("data_list"), [(_X_DATA)])
def test_plot_several_pdf(data_list) -> None:
    """Tests plotting several pdf in the same plot.

    :param data_list: list of data 
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot PDF
    plot_several_pdf(
        data_list=data_list, xlabel="$x$", title_str="PDF", ax=ax
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "histograms", "several_pdf.png")
    save_fig(fig, save_loc, dpi=600)
