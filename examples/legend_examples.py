import sys,os
import numpy as np

# Add path to plotting_utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plotting_utils import *

# Example Plots location
example_plot_folder_loc = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'example_plots'))


# Test legend plotting

def test_plot_legend() -> None:
    """
    Tests legend plotting
    :return: None
    """

    # Save the plot
    save_loc = os.path.join(example_plot_folder_loc,"legends", 'legend.png')

    labels = ["OA","PL","RZ","OB","SA","SSN","SPC"]
    colors = ["red","blue","green","orange","purple","brown","pink"]
    linestyles = ["-.","-","--",":","-.","-","--",":", "-.", "-"]
    markers =["P","o","s","D","^","v","X"]
    linewidth = 2
    legend_size = [4,0.5]
    legend_n_col = 4
    markersize = 5

    # Create seperate legend
    create_seperate_legend(labels = labels, colors = colors, 
                           linestyles = linestyles, linewidth = linewidth,
                             markers = markers, legend_size = legend_size, 
                             save_loc = save_loc, legend_n_col = legend_n_col,
                             markersize = markersize)

if __name__ == '__main__':

    # Set seed for reproducibility
    np.random.seed(0)

    # Test plot legend
    test_plot_legend()