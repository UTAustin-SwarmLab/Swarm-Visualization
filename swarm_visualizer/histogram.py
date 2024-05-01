import numpy as np
import seaborn as sns

from swarm_visualizer.utility import set_axis_infos


def plot_pdf(
    ax, data=None, xlabel: str = None, title_str: str = None, **kwargs
) -> None:
    """Plot PDF of a data.

    :param ax: axis to plot
    :param data: data to plot
    :param xlabel: x-axis label
    :param title_str: title of the plot
    :return: None.
    """
    # Convert data to numpy array
    np_data = np.array(data)

    # Remove NaNs
    clean_data = np_data[~np.isnan(np_data)]

    # Plot histogram with density
    sns.histplot(
        clean_data,
        kde=True,
        stat="density",
        kde_kws=dict(cut=3),
        alpha=0.4,
        edgecolor=(1, 1, 1, 0.4),
        ax=ax,
        **kwargs,
    )

    # Set axis infos
    set_axis_infos(ax, xlabel=xlabel, title_str=title_str)


def plot_several_pdf(
    ax,
    data_list: list[np.ndarray] = None,
    xlabel: str = None,
    title_str: str = None,
    legend=None,
    ylabel: str = None,
    xlim=None,
    kde: bool = False,
    bins="auto",
    binwidth=None,
    **kwargs,
) -> None:
    """Plot PDF of a data list.

    :param ax: axis to plot on
    :param data_list: data list
    :param xlabel: x-axis label
    :param title_str: title of the plot
    :param legend: legend of the plot
    :param ylabel: y-axis label
    :param xlim: x-axis limits
    :param kde: whether to plot kde
    :return: None.
    """
    # if binwidth is not None:
    #     bins = None
    for i, data in enumerate(data_list):
        sns.histplot(
            data,
            kde=kde,
            stat="density",
            kde_kws=dict(cut=3),
            alpha=0.4,
            edgecolor=(1, 1, 1, 0.4),
            ax=ax,
            bins=bins,
            binwidth=binwidth,
            **kwargs,
        )

    # Set axis infos
    set_axis_infos(
        ax,
        xlabel=xlabel,
        ylabel=ylabel,
        title_str=title_str,
        xlim=xlim,
        legend=legend,
    )
