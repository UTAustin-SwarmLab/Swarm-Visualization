import sys,os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from typing import Union, List, Dict, Tuple, Any, Optional

import numpy as np
from scipy.ndimage.interpolation import shift

from numpy import linalg as LA


"""
paired boxplot, hue is a name of a column that controls what to pair by
"""

def plot_paired_boxplot(df = None, x_var = None, y_var = None, plot_file = None, ylim = None, title_str = None, order_list = None, pal = None, hue = None, ax = None) -> None:
    """
    Plots a paired boxplot
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param plot_file: file to save the plot
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param order_list: order of the x-axis variable
    :param pal: palette
    :param hue: hue variable
    :return: 
    """

    # Plots a boxplot
    if not pal:
        
        # Plots a boxplot with order
        if order_list:
            sns.boxplot(x=x_var, y=y_var, data=df, order = order_list, hue = hue, ax = ax)
        else:
            sns.boxplot(x=x_var, y=y_var, data=df, order = order_list, hue = hue, ax = ax)

    # Plots a boxplot with palette
    if pal:
        if order_list:
            sns.boxplot(x=x_var, y=y_var, data=df, order = order_list, palette = pal, hue = hue, ax = ax)
        else:
            sns.boxplot(x=x_var, y=y_var, data=df, order = order_list, palette = pal, hue = hue, ax = ax)


    # Sets y-axis limits
    if ylim:
        ax.set_ylim(ylim[0], ylim[1])
    #sns.plt.tight_layout()
    #sns.plt.savefig(plot_file)
    #sns.plt.clf()

    # Sets title
    if title_str:
        ax.set_title(title_str)

"""
no pairing
"""
def plot_grouped_boxplot(df = None, x_var = None, y_var = None, plot_file = None, ylim = None, title_str = None, order_list = None, pal = None, ax = None) -> None:
    """
    Plots a grouped boxplot
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param plot_file: file to save the plot
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param order_list: order of the x-axis variable
    :param pal: palette
    :return: None
    """
    fig = plt.figure()

    if not pal:
        if order_list:
            plot = sns.boxplot(x=x_var, y=y_var, data=df, order = order_list, ax = ax)
        else:
            plot = sns.boxplot(x=x_var, y=y_var, data=df, order = order_list, ax = ax)

    if pal:
        if order_list:
            plot = sns.boxplot(x=x_var, y=y_var, data=df, order = order_list, palette = pal, ax = ax)
        else:
            plot = sns.boxplot(x=x_var, y=y_var, data=df, order = order_list, palette = pal, ax = ax)


    if ylim:
        plt.ylim(ylim[0], ylim[1])
    #sns.plt.tight_layout()
    #sns.plt.savefig(plot_file)
    #sns.plt.clf()

    if title_str:
        plt.title(title_str)

