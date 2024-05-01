from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from swarm_visualizer import (
    plot_grouped_barplot,
    plot_stacked_barplot,
    plot_sns_grouped_barplot,
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

_HUE_DATA_FRAME = pd.DataFrame(
    {
        "$y_1$": _X1_DATA[:4],
        "$y_2$": _X1_DATA[:4] + 0.02,
        "$x$": ["x_1", "x_1", "x_2", "x_2"],
        "group": ["a", "b", "a", "b"],
    }
)

_SAVE_LOC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "example_plots")
)


@pytest.mark.parametrize(
    ("df", "x_var", "y_var", "y_label"),
    [(_DATA_FRAME, "$x$", ["$y_1$", "$y_2$"], "$y$")],
)
def test_stacked_barplot(df, x_var, y_var, y_label) -> None:
    """Tests stacked barplot.

    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a stacked boxplot
    plot_stacked_barplot(
        df=df,
        x_var=x_var,
        y_var=y_var,
        title_str="Stacked Boxplot",
        ax=ax,
        y_label=y_label,
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "barplot", "stacked_barplot.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(
    ("df", "x_var", "y_var", "y_label"),
    [(_DATA_FRAME, "$x$", ["$y_1$", "$y_2$"], "$y$")],
)
def test_grouped_barplot(df, x_var, y_var, y_label) -> None:
    """Tests grouped barplot.

    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param y_label: y-axis label
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a grouped boxplot
    plot_grouped_barplot(
        df=df,
        x_var=x_var,
        y_var=y_var,
        title_str="Grouped Boxplot",
        ax=ax,
        y_label=y_label,
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "barplot", "grouped_barplot.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(
    ("df", "x_var", "y_var", "y_label", "hue"),
    [(_HUE_DATA_FRAME, "$x$", "$y_1$", "$y$", "group")],
)
def test_sns_grouped_barplot(df, x_var, y_var, y_label, hue) -> None:
    """Tests grouped barplot with sns.

    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param y_label: y-axis label
    :param hue: hue variable
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a grouped boxplot
    plot_sns_grouped_barplot(
        df=df,
        x_var=x_var,
        y_var=y_var,
        hue=hue,
        title_str="Grouped Boxplot",
        ax=ax,
        y_label=y_label,
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "barplot", "hued_barplot.png")
    save_fig(fig, save_loc, dpi=600)
