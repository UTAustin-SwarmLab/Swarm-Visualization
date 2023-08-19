import sys,os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pylab as pylab

from typing import Union, List, Dict, Tuple, Any, Optional

import numpy as np
from scipy.ndimage.interpolation import shift

from numpy import linalg as LA

# Add path to plotting_utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import plotting utils
from plotting_utils import *

# Example Plots location

example_plot_folder_loc = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'example_plots'))


FONT_SIZE = 20
sns.set_color_codes()

plt.rc('text', usetex=True)
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : FONT_SIZE}
plt.rc('font', **font)
plt.rcParams['text.latex.preamble'] = [r'\boldmath']

LEGEND_FONT_SIZE = 14
XTICK_LABEL_SIZE = 14
YTICK_LABEL_SIZE = 14

plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["font.weight"] = "bold"
#matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]


import matplotlib.pylab as pylab
params = {'legend.fontsize': LEGEND_FONT_SIZE,
         'axes.labelsize': FONT_SIZE,
         'axes.titlesize': FONT_SIZE,
         'xtick.labelsize': XTICK_LABEL_SIZE,
         'ytick.labelsize': YTICK_LABEL_SIZE,
         'figure.autolayout': True}
pylab.rcParams.update(params)
plt.rcParams["axes.labelweight"] = "bold"

# Time Series Data Generation For Testing



# Function that tests basic scatterplot
def test_basic_scatterplot(x_data,y_data) -> None:
    """
    Tests basic scatterplot
    :param x_data: x-axis data
    :param y_data: y-axis data
    :return: None
    """


    fig, ax = plt.subplots(figsize=(10, 10))

    # Create a  basic scatter plot
    basic_scatterplot(ts_x = x_data, ts_y = y_data, title_str = 'Basic Scatter Plot', ylabel = 'y', lw = 3.0, ylim = None, xlabel = 'x', xlim = None, ms = 4.0, color = 'b', ax = ax)

    # Save the plot
    save_loc = os.path.join(example_plot_folder_loc, 'basic_scatterplot.png')
    save_fig(fig,save_loc,dpi = 600)

# Function that tests scatterplot with CDFs
def test_scatter_pdf_plot(x_data,y_data) -> None:
    """
    Tests scatterplot with CDFs
    :param x_data: x-axis data
    :param y_data: y-axis data
    :return: None
    """
    
    # Create a scatter plot with CDFs
    fig = scatter_pdf_plot(ts_x = x_data, ts_y = y_data, title_str = 'Scatter Plot with CDFs', ylabel = 'y', lw = 3.0, ylim = None, xlabel = 'x', xlim = None)

    # Save the plot
    save_loc = os.path.join(example_plot_folder_loc, 'scatter_pdf_plot.png')
    save_fig(fig,save_loc,dpi = 600)

if __name__ == '__main__':

    # Set seed for reproducibility
    np.random.seed(0)

    # Generate a time series with a linear trend
    x_data = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)
    y_data = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)

    test_basic_scatterplot(x_data,y_data)
    test_scatter_pdf_plot(x_data,y_data)