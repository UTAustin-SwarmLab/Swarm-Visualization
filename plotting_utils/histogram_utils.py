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

from .general_utils import set_axis_infos


def plot_pdf(data_vector = None, xlabel:str = None, plot_file:str = None, title_str:str = None, ax = None) -> None:
    """
    Plot PDF of a data vector
    :param data_vector: data vector
    :param xlabel: x-axis label
    :param plot_file: file to save the plot
    :param title_str: title of the plot
    :return: None
    """

    # Convert data vector to numpy array
    np_data = np.array(data_vector)

    # Remove NaNs
    clean_data = np_data[~np.isnan(np_data)]

    # Plot histogram with density
    sns.histplot(clean_data,kde=True,stat="density",kde_kws=dict(cut=3),
    alpha=.4, edgecolor=(1, 1, 1, .4), ax = ax)

    # Set axis infos
    set_axis_infos(ax, xlabel = xlabel, title = title_str)

def plot_several_pdf(data_vector_list = None, xlabel:str = None, 
                     plot_file:str = None, title_str:str = None, 
                     legend = None, ylabel:str = None, norm:bool = True, 
                     xlim=None, kde:bool =False, ax = None) -> None:
    """
    Plot PDF of a data vector
    :param data_vector_list: list of data vectors
    :param xlabel: x-axis label
    :param plot_file: file to save the plot
    :param title_str: title of the plot
    :param legend: legend
    :param ylabel: y-axis label
    :param norm: whether to normalize the histogram
    :param xlim: x-axis limits
    :param kde: whether to plot the KDE
    :return: None
    """

    for i, data_vector in enumerate(data_vector_list):
        #sns.distplot(data_vector, norm_hist = norm, kde=kde)
        sns.histplot(data_vector, kde=kde,stat="density",kde_kws=dict(cut=3),
    alpha=.4, edgecolor=(1, 1, 1, .4), ax = ax)
        #sns.histplot(data_vector, norm_hist = norm)
        #plt.hold(True)


    # Set axis infos
    set_axis_infos(ax, xlabel = xlabel, ylabel = ylabel, title = title_str, xlim = xlim, legend = legend)

