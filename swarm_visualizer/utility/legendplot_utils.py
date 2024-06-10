import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pylab as pylab
import matplotlib as mpl
from matplotlib.cm import get_cmap
import numpy as np

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

def create_colorbar(ax, all_labels, title=None, visible_labels=None, colors=None, palette=None, discrete=False, orientation="vertical"):
    """Creates a custom colorbar.

    Args:
        ax: Axis to plot the colorbar
        all_labels: All labels in the dataset
        visible_labels: Labels that are visible in the plot
        colors: Colors of the labels
        palette: Palette of the colors
        discrete: If the colorbar is discrete
        orientation: Orientation of the colorbar
    """

    # If colors and palette is given at the same time raise an error
    if colors and palette:
        raise ValueError("Both colors and palette cannot be given at the same time.")

    # If discrete is False and colors are given raise an error
    if not discrete and colors:
        raise ValueError("Colors can only be given if discrete is True.")
    
    # If discrete and colors are not given, get the colors from the palette
    if discrete and not colors:
        colors = sns.color_palette(palette)

    if discrete:
        cmaplist = [colors[i] for i in range(len(all_labels))]
        cmap = mpl.colors.LinearSegmentedColormap.from_list(
            "Custom cmap", cmaplist, len(cmaplist)
        )
        bounds = np.arange(len(all_labels) + 1) - 0.5
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm, cax=ax, ticks=np.arange(len(all_labels)), orientation=orientation)
        
        if visible_labels:

            # Location of the visible labels
            visible_labels_location = [all_labels.index(label) for label in visible_labels]

            # Set the ticks and labels
            cbar.set_ticks(ticks=visible_labels_location, labels=visible_labels)
        else:
            cbar.set_ticks(ticks=np.arange(len(all_labels)), labels=all_labels)
    
    else:
        cmap = get_cmap(palette)
        norm = plt.Normalize(min(all_labels), max(all_labels))
        cbar = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation=orientation)
        if visible_labels:
            cbar.set_ticks(ticks=visible_labels)
    
    if title:
        cbar.set_label(title)