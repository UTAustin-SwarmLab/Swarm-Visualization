from typing import Dict

import matplotlib.pyplot as plt


# plot grid KPI subfigures
def plot_grid(
    normalized_ts_dict: Dict = None,
    title_str: str = None,
    plot_file: str = None,
    lw: float = 3.0,
    xlabel: str = None,
) -> None:
    """Plot grid of time series.

    :param normalized_ts_dict: dictionary with time series to plot
    :param title_str: title of the plot
    :param plot_file: file to save the plot
    :param lw: line width
    :param xlabel: x-axis label
    :return: None
    """
    # Number of rows and columns in the grid
    nrow = len(normalized_ts_dict.keys())

    # Create figure with subplots
    plt.close("all")
    f, axarr = plt.subplots(nrow, 1, sharex=True)

    # Set title if not none
    if title_str:
        plt.title(title_str)
    # print(axarr)
    # print(axarr[0])

    # Plot time series data in each subplot starting from the top
    row = 0
    for ylabel_name, timeseries_dict in normalized_ts_dict.items():
        # Plot with x-axis if xvec is specified
        if "x" in timeseries_dict.keys():
            axarr[row].plot(
                timeseries_dict["x"], timeseries_dict["ts_vector"], lw=lw
            )
        else:
            axarr[row].plot(timeseries_dict["ts_vector"], lw=lw)

        # Set y-axis label
        axarr[row].set_ylabel(ylabel_name)

        # Set y-axis limits
        if "ylim" in timeseries_dict.keys():
            axarr[row].set_ylim(timeseries_dict["ylim"])

        # Set x-axis limits
        if "xlim" in timeseries_dict.keys():
            axarr[row].set_xlim(timeseries_dict["xlim"])

        # Set y-axis ticks
        if "yticks" in timeseries_dict.keys():
            if timeseries_dict["yticks"]:
                axarr[row].set_yticks(timeseries_dict["yticks"])

        row += 1

    # Set x-axis label
    if xlabel:
        plt.xlabel(xlabel)

    # Show and Save figure
    plt.show()
    plt.savefig(plot_file)
    plt.close()
