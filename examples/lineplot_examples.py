import sys, os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pylab as pylab

# Add path to plotting_utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import plotting utils
from plotting_utils import *

# Example Plots location

example_plot_folder_loc = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "example_plots")
)

# Time Series Data Generation For Testing


def test_basic_ts_plot(ts_vector=None) -> None:
    """
    Tests basic time series plot
    :param ts_vector: time series
    :return: None
    """

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot time series
    basic_plot_ts(
        ts_vector=ts_vector,
        title_str="Basic Time Series Plot",
        ylabel="$y$",
        lw=3.0,
        ylim=None,
        xlabel="$x$",
        ax=ax,
    )

    # Save the plot
    save_loc = os.path.join(example_plot_folder_loc, "lineplots", "basic_ts_plot.png")
    save_fig(fig, save_loc, dpi=600)


def test_overlaid_ts_plot(normalized_ts_dict=None) -> None:
    """
    Tests overlaid time series plot
    :param normalized_ts_dict: dictionary with time series to plot
    :return: None
    """

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot overlaid time series
    overlaid_ts(
        normalized_ts_dict=normalized_ts_dict,
        title_str="Overlaid Time Series Plot",
        ylabel="$y$",
        xlabel="$x$",
        fontsize=30,
        xticks=None,
        ylim=None,
        DEFAULT_ALPHA=1.0,
        legend_present=True,
        DEFAULT_MARKERSIZE=15,
        delete_yticks=False,
        ax=ax,
    )

    # Save the plot
    save_loc = os.path.join(
        example_plot_folder_loc, "lineplots", "overlaid_ts_plot.png"
    )
    save_fig(fig, save_loc, dpi=600)


if __name__ == "__main__":
    # Set seed for reproducibility
    np.random.seed(0)

    # Generate a time series with a linear trend
    x_data = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)
    y_data = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)

    sin_data = np.sin(x_data)
    cos_data = np.cos(y_data)

    set_plot_properties()

    # Test basic time series plot
    test_basic_ts_plot(ts_vector=x_data)

    # Normalized time series dictionary
    normalized_ts_dict = {
        "$x$": {
            "xvec": np.arange(0, 10, 0.1),
            "ts_vector": x_data,
            "lw": 3.0,
            "linestyle": "-",
            "color": "b",
        },
        "$y$": {
            "xvec": np.arange(0, 10, 0.1),
            "ts_vector": y_data,
            "lw": 3.0,
            "linestyle": "-",
            "color": "r",
        },
        "$\sin$": {
            "xvec": np.arange(0, 10, 0.1),
            "ts_vector": sin_data,
            "lw": 3.0,
            "linestyle": "-",
            "color": "g",
            "zorder": 2,
        },
        "$\cos$": {
            "xvec": np.arange(0, 10, 0.1),
            "ts_vector": cos_data,
            "lw": 3.0,
            "linestyle": "-",
            "color": "k",
            "zorder": 10,
        },
    }

    # Test overlaid time series plot

    test_overlaid_ts_plot(normalized_ts_dict=normalized_ts_dict)
