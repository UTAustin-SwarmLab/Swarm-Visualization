from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from swarm_visualizer.violinplot import (
    plot_grouped_violinplot,
    plot_paired_violinplot,
)
from swarm_visualizer.utility.general_utils import save_fig, set_plot_properties

_X1_DATA = np.arange(0, 5, 0.05) + np.random.normal(0, 0.1, 100)
_X2_DATA = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)

_X_DATA = np.concatenate([_X1_DATA, _X2_DATA])
_X_LABEL = np.concatenate([np.repeat("$x_1$", 100), np.repeat("$x_2$", 100)])

_GROUPS = np.concatenate(
    [
        np.repeat("a", 50),
        np.repeat("b", 50),
        np.repeat("a", 50),
        np.repeat("b", 50),
    ]
)

_DATA_FRAME = pd.DataFrame(
    {r"$f_\theta(x)$": _X_DATA, "$x$": _X_LABEL, "Groups": _GROUPS}
)
_SAVE_LOC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "example_plots")
)


@pytest.mark.parametrize(
    ("df", "x_var", "y_var"), [(_DATA_FRAME, "$x$", r"$f_\theta(x)$")]
)
def test_grouped_violinplot(df, x_var, y_var) -> None:
    """
    Tests grouped violinplot
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :return: None
    """

    # Set plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a grouped violinplot
    plot_grouped_violinplot(
        df=df, x_var=x_var, y_var=y_var, title_str="Grouped Violinplot", ax=ax
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "violinplots", "grouped_violinplot.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(
    ("df", "x_var", "y_var", "hue"),
    [(_DATA_FRAME, "$x$", r"$f_\theta(x)$", "Groups")],
)
def test_paired_violinplot(df, x_var, y_var, hue) -> None:
    """
    Tests paired violinplot
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :return: None
    """

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a paired violinplot
    plot_paired_violinplot(
        df=df,
        x_var=x_var,
        y_var=y_var,
        hue=hue,
        title_str="Paired Violinplot",
        ax=ax,
    )

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "violinplots", "paired_violinplot.png")
    save_fig(fig, save_loc, dpi=600)
