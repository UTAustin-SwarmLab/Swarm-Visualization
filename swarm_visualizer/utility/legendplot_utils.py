import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pylab as pylab

from typing import List, Dict
from swarm_visualizer.utility import save_fig


def create_seperate_legend(
    labels: List[str] = None,
    colors: List = None,
    linestyles: List = None,
    linewidth: float = None,
    markers: List = None,
    markersize: float = 3,
    legend_size: List[float] = None,
    save_loc: str = "legend.png",
    legend_n_col: int = 1,
    legend_prop: Dict = None,
) -> None:
    """Creates a seperate legend.

    :param names: names of the time series
    :param colors: colors of the time series
    :param linestyles: linestyles of the time series
    :param linewidth: linewidth of the time series
    :param labels: labels of the time series
    :param markers: markers of the time series
    :param markersize: markersize of the time series
    :param legend_size: size of the legend
    :param save_loc: location to save the legend
    :param legend_n_col: number of columns in the legend
    :param legend_prop: legend properties
    :return: None
    """
    fig = plt.figure(constrained_layout=False)
    fig.set_size_inches(18.5, 10.5)
    gs = fig.add_gridspec(1, 1)
    ax00 = fig.add_subplot(gs[0])

    # Creates a dummy plot to create the legend
    for i in range(len(labels)):
        if markers:
            if linestyles:
                sns.lineplot(
                    x=[1],
                    y=[2],
                    color=colors[i],
                    marker=markers[i],
                    markersize=markersize,
                    linestyle=linestyles[i],
                    ax=ax00,
                    linewidth=linewidth,
                    label=labels[i],
                )
            else:
                sns.lineplot(
                    x=[1],
                    y=[2],
                    color=colors[i],
                    marker=markers[i],
                    markersize=markersize,
                    ax=ax00,
                    linewidth=linewidth,
                    label=labels[i],
                )
        else:
            if linestyles:
                sns.lineplot(
                    x=[1],
                    y=[2],
                    color=colors[i],
                    linestyle=linestyles[i],
                    ax=ax00,
                    linewidth=linewidth,
                    label=labels[i],
                )
            else:
                sns.lineplot(
                    x=[1],
                    y=[2],
                    color=colors[i],
                    ax=ax00,
                    linewidth=linewidth,
                    label=labels[i],
                )

    # Sets legend figure size
    figLegend = pylab.figure(figsize=(legend_size[0], legend_size[1]))

    # Creates legend
    if legend_prop:
        pylab.figlegend(
            *ax00.get_legend_handles_labels(),
            loc="upper left",
            mode="expand",
            ncol=legend_n_col,
            prop=legend_prop,
            borderaxespad=0,
            frameon=False,
        )
    else:
        pylab.figlegend(
            *ax00.get_legend_handles_labels(),
            loc="upper left",
            mode="expand",
            ncol=legend_n_col,
            borderaxespad=0,
            frameon=False,
        )

    # Saves legend
    save_fig(figLegend, save_loc, dpi=600)
