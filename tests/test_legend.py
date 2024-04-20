from __future__ import annotations

import os
import pytest

from swarm_visualizer.utility import set_plot_properties
from swarm_visualizer.utility import create_seperate_legend

# Example Labels
_LABELS = ["OA", "PL", "RZ", "OB", "SA", "SSN", "SPC"]

# Example Colors
_COLORS = ["red", "blue", "green", "orange", "purple", "brown", "pink"]

# Example Linestyles
_LINESTYLES = ["-.", "-", "--", ":", "-.", "-", "--", ":", "-.", "-"]

# Example Markers
_MARKERS = ["P", "o", "s", "D", "^", "v", "X"]

# Example linewidth
_LINEWIDTH = 2

# Example markersize
_MARKERSIZE = 5

# Example legend size

_LEGEND_SIZE = [4, 0.5]

# Example legend number of columns
_LEGEND_N_COL = 4


_SAVE_LOC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "example_plots")
)


@pytest.mark.parametrize(
    (
        "labels",
        "colors",
        "linestyles",
        "markers",
        "linewidth",
        "legend_size",
        "legend_n_col",
        "markersize",
    ),
    [
        (
            _LABELS,
            _COLORS,
            _LINESTYLES,
            _MARKERS,
            _LINEWIDTH,
            _LEGEND_SIZE,
            _LEGEND_N_COL,
            _MARKERSIZE,
        )
    ],
)
def test_plot_legend(
    labels,
    colors,
    linestyles,
    markers,
    linewidth,
    legend_size,
    legend_n_col,
    markersize,
) -> None:
    """Tests legend plotting.

    :param labels: labels
    :param colors: colors
    :param linestyles: linestyles
    :param markers: markers
    :param linewidth: linewidth
    :param legend_size: size of the legend
    :param legend_n_col: number of columns in the legend
    :param markersize: markersize
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "legends", "legend.png")

    # Create seperate legend
    create_seperate_legend(
        labels=labels,
        colors=colors,
        linestyles=linestyles,
        linewidth=linewidth,
        markers=markers,
        legend_size=legend_size,
        save_loc=save_loc,
        legend_n_col=legend_n_col,
        markersize=markersize,
    )
