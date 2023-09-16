from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from swarm_visualizer.boxplot import plot_grouped_boxplot, plot_paired_boxplot
from swarm_visualizer.utility.general_utils import save_fig, set_plot_properties

# Example Plots location
_X1_DATA = np.arange(0, 5, 0.05) + np.random.normal(0, 0.1, 100)
_X2_DATA = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)

# Concatenate the data
_X_DATA = np.concatenate([_X1_DATA, _X2_DATA])
_X_LABEL = np.concatenate([np.repeat("$x_1$", 100), np.repeat("$x_2$", 100)])

# Additional Groupings in each x with _GROUPS of 50 as group a and group b
_GROUPS = np.concatenate(
    [
        np.repeat("a", 50),
        np.repeat("b", 50),
        np.repeat("a", 50),
        np.repeat("b", 50),
    ]
)

_DATA_FRAME = pd.DataFrame(
    {"$y$": _X_DATA, "$x$": _X_LABEL, "_GROUPS": _GROUPS}
)
_SAVE_LOC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "example_plots")
)


@pytest.mark.parametrize(
    ("df", "x_var", "y_var", "hue"), [(_DATA_FRAME, "$x$", "$y$", _GROUPS)]
)
def test_paired_boxplot(df, x_var, y_var, hue) -> None:
    """Tests paired boxplot.

    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :return: None.
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a paired boxplot
    plot_paired_boxplot(
        df=df,
        x_var=x_var,
        y_var=y_var,
        hue=hue,
        title_str="Paired Boxplot",
        ax=ax,
    )
    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "boxplots", "paired_boxplot.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(
    ("df", "x_var", "y_var"), [(_DATA_FRAME, "$x$", "$y$")]
)
def test_grouped_boxplot(df, x_var, y_var) -> None:
    """Tests grouped boxplot.

    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :return: None.
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a grouped boxplot
    plot_grouped_boxplot(
        df=df, x_var=x_var, y_var=y_var, title_str="Grouped Boxplot", ax=ax
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "boxplots", "grouped_boxplot.png")
    save_fig(fig, save_loc, dpi=600)
