from typing import Dict

import seaborn as sns

from swarm_visualizer.utility.general_utils import set_axis_infos


def plot_basic_lineplot(
    y=None,
    title_str: str = None,
    ylabel: str = None,
    lw: float = 3.0,
    ylim=None,
    xlabel: str = "x",
    ax=None,
) -> None:
    """Basic lineplot.

    :param y: y data to plot
    :param title_str: title of the plot
    :param ylabel: y-axis label
    :param lw: line width
    :param ylim: y-axis limits
    :param xlabel: x-axis label
    :param ax: axis to plot on
    :return: None.
    """
    # Plot time series
    ax.plot(y, lw=lw)

    set_axis_infos(
        ax, xlabel=xlabel, ylabel=ylabel, ylim=ylim, title_str=title_str
    )


def plot_overlaid_lineplot(
    normalized_dict: Dict = None,
    title_str: str = None,
    ylabel: str = None,
    xlabel: str = "x",
    xticks=None,
    ylim=None,
    DEFAULT_ALPHA: float = 1.0,
    legend_present: bool = True,
    DEFAULT_MARKERSIZE: float = 15,
    delete_yticks: bool = False,
    ax=None,
) -> None:
    """Overlaid line plot.
    
    :param normalized_dict: dictionary with values to plot
    :param title_str: title of the plot
    :param ylabel: y-axis label
    :param xlabel: x-axis label
    :param xticks: x-axis ticks
    :param ylim: y-axis limits
    :param DEFAULT_ALPHA: default alpha value
    :param legend_present: whether to plot the legend
    :param DEFAULT_MARKERSIZE: default marker size
    :param delete_yticks: whether to delete the y-axis ticks
    :param ax: axis to plot on
    :return: None.
    """
    # dictionary:
    # key = name, value is a dict, value = {'x': , 'y', 'lw', 'linestyle', 'color'}

    # Colors used in plots
    colors = [
        "denim blue",
        "medium green",
        "pale red",
        "amber",
        "greyish",
        "dusty purple",
    ]

    # Plot time series
    i = 0
    for name, data_dict in normalized_dict.items():
        # Order of the line
        if "zorder" in data_dict.keys():
            zorder = data_dict["zorder"]
        else:
            zorder = None

        # Color of the line
        if "color" in data_dict.keys():
            color = data_dict["color"]
        else:
            color = sns.xkcd_rgb[colors[i]]

        # Alpha value of the line
        if "alpha" in data_dict.keys():
            alpha = data_dict["alpha"]
        else:
            alpha = DEFAULT_ALPHA

        # Plot with x-axis if x is specified
        if "x" in data_dict.keys():
            # Plot with markers if marker is specified
            if "marker" in data_dict.keys():
                ax.plot(
                    data_dict["x"],
                    data_dict["y"],
                    lw=data_dict["lw"],
                    label=name,
                    marker=data_dict["marker"],
                    ls=data_dict["linestyle"],
                    alpha=alpha,
                    ms=DEFAULT_MARKERSIZE,
                    color=color,
                    zorder=zorder,
                )
            else:
                ax.plot(
                    data_dict["x"],
                    data_dict["y"],
                    lw=data_dict["lw"],
                    label=name,
                    ls=data_dict["linestyle"],
                    alpha=alpha,
                    color=color,
                    zorder=zorder,
                )
        # Plot without x-axis if x is not specified
        else:
            if "marker" in data_dict.keys():
                ax.plot(
                    data_dict["y"],
                    lw=data_dict["lw"],
                    label=name,
                    marker=data_dict["marker"],
                    ls=data_dict["linestyle"],
                    alpha=alpha,
                    ms=DEFAULT_MARKERSIZE,
                    color=color,
                    zorder=zorder,
                )
            else:
                ax.plot(
                    data_dict["y"],
                    lw=data_dict["lw"],
                    label=name,
                    ls=data_dict["linestyle"],
                    alpha=alpha,
                    color=color,
                    zorder=zorder,
                )

        i += 1

    set_axis_infos(
        ax,
        xlabel=xlabel,
        ylabel=ylabel,
        ylim=ylim,
        xticks=xticks,
        title_str=title_str,
    )

    # Plot legend
    if legend_present:
        ax.legend(loc="best")

    # Delete y-axis ticks if specified
    if delete_yticks:
        ax.set_yticks([])
