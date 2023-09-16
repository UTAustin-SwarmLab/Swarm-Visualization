import numpy as np
import seaborn as sns

from swarm_visualizer.utility.general_utils import set_axis_infos


def plot_pdf(
    data_vector=None, xlabel: str = None, title_str: str = None, ax=None
) -> None:
    """Plot PDF of a data vector.

    :param data_vector: data vector
    :param xlabel: x-axis label
    :param title_str: title of the plot
    :param ax: axis to plot on
    :return: None.
    """
    # Convert data vector to numpy array
    np_data = np.array(data_vector)

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
    )

    # Set axis infos
    set_axis_infos(ax, xlabel=xlabel, title_str=title_str)


def plot_several_pdf(
    data_vector_list=None,
    xlabel: str = None,
    title_str: str = None,
    legend=None,
    ylabel: str = None,
    xlim=None,
    kde: bool = False,
    ax=None,
) -> None:
    """Plot PDF of a data vector.

    :param data_vector: data vector
    :param xlabel: x-axis label
    :param title_str: title of the plot
    :param legend: legend of the plot
    :param ylabel: y-axis label
    :param xlim: x-axis limits
    :param kde: whether to plot kde
    :param ax: axis to plot on
    :return: None.
    """
    for i, data_vector in enumerate(data_vector_list):
        # sns.distplot(data_vector, norm_hist = norm, kde=kde)
        sns.histplot(
            data_vector,
            kde=kde,
            stat="density",
            kde_kws=dict(cut=3),
            alpha=0.4,
            edgecolor=(1, 1, 1, 0.4),
            ax=ax,
        )
        # sns.histplot(data_vector, norm_hist = norm)
        # plt.hold(True)

    # Set axis infos
    set_axis_infos(
        ax,
        xlabel=xlabel,
        ylabel=ylabel,
        title_str=title_str,
        xlim=xlim,
        legend=legend,
    )
