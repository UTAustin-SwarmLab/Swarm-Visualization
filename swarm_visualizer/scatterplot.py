import matplotlib.pyplot as plt
import seaborn as sns

from swarm_visualizer.utility.general_utils import set_axis_infos


def plot_basic_scatterplot(
    ax,
    x=None,
    y=None,
    title_str: str = None,
    ylabel: str = None,
    lw: float = 3.0,
    ylim=None,
    xlabel: str = "time",
    xlim=None,
    ms: float = 4.0,
    color: str = "b",
) -> None:
    """Basic scatter plot.

    :param ax: axis to plot
    :param x: x-axis data
    :param y: y-axis data
    :param title_str: title of the plot
    :param ylabel: y-axis label
    :param lw: line width
    :param ylim: y-axis limits
    :param xlabel: x-axis label
    :param xlim: x-axis limits
    :param ms: marker size
    :param color: color of the markers
    :return: None.
    """
    if ax is None:
        fig, ax = plt.subplots()

    # Scatter plot
    ax.scatter(x, y, lw=lw, s=ms, color=color)

    # Set labels
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Set limits
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)

    return ax


# joint plot: scatterplot with the PDFs
def plot_scatter_pdf_plot(
    x=None,
    y=None,
    title_str: str = None,
    ylabel: str = None,
    ylim=None,
    xlabel: str = "time",
    xlim=None,
):
    """Scatter plot with the PDFs and saves the plot.
    
    :param x: x-axis data
    :param y: y-axis data
    :param title_str: title of the plot
    :param ylabel: y-axis label
    :param lw: line width
    :param ylim: y-axis limits
    :param xlabel: x-axis label
    :param xlim: x-axis limits
    :return: None.
    """
    # Joint plot
    fig = sns.jointplot(
        x=x,
        y=y,
    )

    # Set labels
    fig.set_axis_labels(xlabel, ylabel)

    # Set limits
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    # Set title
    fig.fig.suptitle(title_str, fontsize=20, va="top", y=1.03)

    return fig
