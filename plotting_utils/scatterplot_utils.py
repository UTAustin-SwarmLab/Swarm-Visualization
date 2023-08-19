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

def basic_scatterplot(ts_x = None, ts_y = None, title_str:str = None, ylabel:str = None, lw:float=3.0, ylim = None, xlabel:str = 'time', xlim = None, ms:float =4.0, color:str = 'b', ax = None) -> None:
    """
    Basic scatter plot
    :param ts_x: x-axis time series
    :param ts_y: y-axis time series
    :param title_str: title of the plot
    :param plot_file: file to save the plot
    :param ylabel: y-axis label
    :param lw: line width
    :param ylim: y-axis limits
    :param xlabel: x-axis label
    :param xlim: x-axis limits
    :param ms: marker size
    :param color: color of the markers
    :param ax: axis to plot
    :return: None
    """

    # Scatter plot
    ax.scatter(ts_x, ts_y, lw=lw, s = ms, color = color)

    # Set labels
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Set limits
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    # Set title
    ax.set_title(title_str)

# joint plot: scatterplot with the CDFs
def scatter_pdf_plot(ts_x = None, ts_y = None, title_str:str = None, ylabel:str = None, lw:float=3.0, ylim = None, xlabel:str = 'time', xlim = None):
    """
    Scatter plot with the CDFs and saves the plot
    :param ts_x: x-axis time series
    :param ts_y: y-axis time series
    :param title_str: title of the plot
    :param ylabel: y-axis label
    :param lw: line width
    :param ylim: y-axis limits
    :param xlabel: x-axis label
    :param xlim: x-axis limits
    :return: None
    """

    # Joint plot
    fig = sns.jointplot(x = ts_x, y = ts_y,)

    # Set labels
    fig.set_axis_labels(xlabel, ylabel)
    
    # Set limits
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    # Set title
    fig.fig.suptitle(title_str)

    return fig