import numpy as np
import seaborn as sns

from .general_utils import set_axis_infos


def plot_pdf(
    data_vector=None, xlabel: str = None, title_str: str = None, ax=None
) -> None:
    """
    Plot PDF of a data vector
    :param data_vector: data vector
    :param xlabel: x-axis label
    :param title_str: title of the plot
    :param ax: axis to plot on
    :return: None
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
    """
    Plot PDF of a data vector
    :param data_vector: data vector
    :param xlabel: x-axis label
    :param title_str: title of the plot
    :param legend: legend of the plot
    :param ylabel: y-axis label
    :param xlim: x-axis limits
    :param kde: whether to plot kde
    :param ax: axis to plot on
    :return: None
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
        ax, xlabel=xlabel, ylabel=ylabel, title_str=title_str, xlim=xlim, legend=legend
    )


def plot_stacked_histogram(
    df=None,
    x_var=None,
    y_var=None,
    ylim=None,
    title_str=None,
    pal=None,
    ax=None,
    y_label=None,
) -> None:
    """
    Plots a grouped boxplot
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param pal: palette
    :param ax: axis to plot on
    :return: None
    """

    if not pal:
        df.plot(kind="bar", stacked=True, ax=ax, x=x_var, y=y_var)

    if pal:
        colors = [pal(i) for i in range(len(x_var))]
        df.plot(kind="bar", stacked=True, ax=ax, x=x_var, y=y_var, colors=colors)

    ### set y label
    if y_label:
        ax.set_ylabel(y_label)

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)
