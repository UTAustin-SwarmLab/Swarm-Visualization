from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from swarm_visualizer.histogram import (
    plot_pdf,
    plot_several_pdf,
    plot_stacked_histogram,
)
from swarm_visualizer.utility.general_utils import save_fig, set_plot_properties

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


@pytest.mark.parametrize(("data_vector"), [(_X1_DATA)])
def test_plot_pdf(data_vector) -> None:
    """
    :param data_vector: data vector
    :return: None
    """

    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot PDF
    plot_pdf(data_vector=data_vector, xlabel="$x$", title_str="PDF", ax=ax)

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "histograms", "pdf.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(("data_vector_list"), [(_X_DATA)])
def test_plot_several_pdf(data_vector_list) -> None:
    """
    :param data_vector_list: list of data vectors
    :return: None
    """

    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot PDF
    plot_several_pdf(
        data_vector_list=data_vector_list, xlabel="$x$", title_str="PDF", ax=ax
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "histograms", "several_pdf.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(
    ("df", "x_var", "y_var", "y_label"),
    [(_DATA_FRAME, "$x$", ["$y_1$", "$y_2$"], "$y$")],
)
def test_stacked_histogram(df, x_var, y_var, y_label) -> None:
    """
    Tests grouped boxplot
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :return: None
    """

    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a grouped boxplot
    plot_stacked_histogram(
        df=df,
        x_var=x_var,
        y_var=y_var,
        title_str="Stacked Boxplot",
        ax=ax,
        y_label=y_label,
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "histograms", "stacked_histogram.png")
    save_fig(fig, save_loc, dpi=600)
