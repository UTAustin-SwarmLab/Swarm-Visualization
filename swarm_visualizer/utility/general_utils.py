import os

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import seaborn as sns
import shutil


def set_plot_properties(
    font_size: float = 20,
    legend_font_size: float = 14,
    xtick_label_size: float = 14,
    ytick_label_size: float = 14,
    markersize: float = 10,
    usetex: bool = True,
    autolayout = True,
) -> None:
    """Sets plot properties.

    :param font_size: font size
    :param legend_font_size: legend font size
    :param xtick_label_size: xtick label size
    :param ytick_label_size: ytick label size
    :param markersize: marker size
    :param usetex: use tex
    :return: None.
    """
    sns.set_color_codes()
    sns.set()

    if shutil.which("latex"):
        plt.rc("text", usetex=usetex)
    else:
        plt.rc("text", usetex=False)
    font = {"family": "normal", "weight": "bold", "size": font_size}
    plt.rc("font", **font)
    plt.rcParams["text.latex.preamble"] = r"\boldmath"

    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["font.weight"] = "bold"

    params = {
        "legend.fontsize": legend_font_size,
        "axes.labelsize": font_size,
        "axes.titlesize": font_size,
        "xtick.labelsize": xtick_label_size,
        "ytick.labelsize": ytick_label_size,
        "lines.markersize": markersize,
        "figure.autolayout": autolayout,
    }

    pylab.rcParams.update(params)

    sns.set_style(style="darkgrid")


def save_fig(fig, save_loc: str = None, dpi: int = 600) -> None:
    """Save figure.

    :param fig: figure
    :param save_loc: location to save the figure
    :param dpi: dpi
    :return: None.
    """
    # If save location doesn't exist, create it
    if not os.path.exists(os.path.dirname(save_loc)):
        os.makedirs(os.path.dirname(save_loc))

    # Save the figure
    fig.savefig(save_loc, dpi=dpi)
    plt.close("all")


def set_axis_infos(
    ax,
    xlabel: str = None,
    ylabel: str = None,
    xlim=None,
    ylim=None,
    legend=None,
    title_str: str = None,
    xticks=None,
    yticks=None,
    xlabel_size: int = 20,
    ylabel_size: int = 20,
    title_size: int = 26,
    ticks_size: int = 18,
    legend_size: int = 20,
    legend_loc: str = "best",
    grid: bool = False,
) -> None:
    """Set axis information.

    :param ax: axis
    :param xlabel: x-axis label
    :param ylabel: y-axis label
    :param xlim: x-axis limits
    :param ylim: y-axis limits
    :param legend: legend
    :param title_str: title
    :param xticks: x-axis ticks
    :param yticks: y-axis ticks
    :param xlabel_size: x-axis label size
    :param ylabel_size: y-axis label size
    :param title_str: title
    :param xticks: x-axis ticks
    :param yticks: y-axis ticks
    :param xlabel_size: x-axis label size
    :param ylabel_size: y-axis label size
    :param title_size: title size
    :param ticks_size: ticks size
    :param legend_size: legend size
    :param legend_loc: legend location
    :return: None.
    """
    if xlabel:
        ax.set_xlabel(xlabel)
    if xlabel_size:
        ax.xaxis.label.set_size(xlabel_size)
    if ylabel:
        ax.set_ylabel(ylabel)
    if ylabel_size:
        ax.yaxis.label.set_size(ylabel_size)
    if xlim:
        ax.set_xlim(xlim[0], xlim[1])
    if ylim:
        ax.set_ylim(ylim[0], ylim[1])
    if xticks:
        ax.set_xticks(xticks)
    if yticks:
        ax.set_yticks(yticks)
    if ticks_size:
        ax.tick_params(axis="both", which="major", labelsize=ticks_size)
    if legend:
        ax.legend(legend, fontsize=legend_size, loc=legend_loc)
    if title_str:
        ax.set_title(title_str, fontsize=title_size)
    if grid:
        ax.grid()
