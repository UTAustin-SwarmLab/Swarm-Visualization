import sys, os
import numpy as np
import matplotlib.pyplot as plt

# Add path to plotting_utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plotting_utils import *

# Example Plots location
example_plot_folder_loc = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "example_plots")
)


def test_plot_pdf(data_vector=None) -> None:
    """
    :param data_vector: data vector
    :return: None
    """

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot PDF
    plot_pdf(data_vector=data_vector, xlabel="$x$", title_str="PDF", ax=ax)

    # Save the plot
    save_loc = os.path.join(example_plot_folder_loc, "histograms", "pdf.png")
    save_fig(fig, save_loc, dpi=600)


def test_plot_several_pdf(data_vector_list=None) -> None:
    """
    :param data_vector_list: list of data vectors
    :return: None
    """

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot PDF
    plot_several_pdf(
        data_vector_list=data_vector_list, xlabel="$x$", title_str="PDF", ax=ax
    )

    # Save the plot
    save_loc = os.path.join(example_plot_folder_loc, "histograms", "several_pdf.png")
    save_fig(fig, save_loc, dpi=600)


if __name__ == "__main__":
    # Set seed for reproducibility
    np.random.seed(0)

    # Generate a time series with a linear trend
    x1_data = np.arange(0, 5, 0.05) + np.random.normal(0, 0.1, 100)
    x2_data = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)

    set_plot_properties()

    # Test plot pdf
    test_plot_pdf(data_vector=x1_data)

    # Test plot several pdf
    test_plot_several_pdf(data_vector_list=[x1_data, x2_data])
