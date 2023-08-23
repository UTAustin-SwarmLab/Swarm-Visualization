import os
import matplotlib.pyplot as plt


def save_fig(fig, save_loc: str = None, dpi: int = 600) -> None:
    """
    Save figure
    :param fig: figure
    :param save_loc: location to save the figure
    :param dpi: dpi
    :return: None
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
    ylabel: int = None,
    xlim=None,
    ylim=None,
    legend=None,
    title: str = None,
    xticks=None,
    yticks=None,
) -> None:
    """
    Set axis information
    :param ax: axis
    :param xlabel: x-axis label
    :param ylabel: y-axis label
    :param xlim: x-axis limits
    :param ylim: y-axis limits
    :param legend: legend
    :param title: title
    :return: None
    """
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if xlim:
        ax.set_xlim(xlim[0], xlim[1])
    if ylim:
        ax.set_ylim(ylim[0], ylim[1])
    if xticks:
        ax.set_xticks(xticks)
    if yticks:
        ax.set_yticks(yticks)
    if legend:
        ax.legend(legend)
    if title:
        ax.set_title(title)
