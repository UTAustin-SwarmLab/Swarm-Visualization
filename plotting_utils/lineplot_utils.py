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

def basic_plot_ts(ts_vector = None, title_str:str = None, plot_file:str = None, ylabel:str = None, lw:float =3.0, ylim = None, xlabel:str = 'time', ax = None) -> None:
    """
    Basic plot of a time series
    :param ts_vector: time series
    :param title_str: title of the plot
    :param plot_file: file to save the plot
    :param ylabel: y-axis label
    :param lw: line width
    :param ylim: y-axis limits
    :param xlabel: x-axis label
    :return: None
    """

    # Plot time series
    plt.plot(ts_vector, lw=lw, ax = ax)

    # Set labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Set limits
    if ylim:
        plt.ylim(ylim[0], ylim[1])

    # Set title
    plt.title(title_str)


def overlaid_ts(normalized_ts_dict:Dict = None, title_str:str = None, plot_file:str = None, 
                ylabel:str = None, xlabel:str = 'time', fontsize:float = 30, xticks = None, 
                ylim = None, DEFAULT_ALPHA:float = 1.0, legend_present:bool = True, 
                DEFAULT_MARKERSIZE:float = 15, delete_yticks:bool = False, ax = None) -> None:
    """
    Overlaid time series plot
    :param normalized_ts_dict: dictionary with time series to plot
    :param title_str: title of the plot
    :param plot_file: file to save the plot
    :param ylabel: y-axis label
    :param xlabel: x-axis label
    :param fontsize: font size
    :param xticks: x-axis ticks
    :param ylim: y-axis limits
    :param DEFAULT_ALPHA: default alpha value
    :param legend_present: whether to plot the legend
    :param DEFAULT_MARKERSIZE: default marker size
    :param delete_yticks: whether to delete the y-axis ticks
    :return: None
    """

    # dictionary:
    # key = ts_name, value is a dict, value = {'xvec': , 'ts_vector', 'lw', 'linestyle', 'color'}

    # Colors used in plots
    colors = ["denim blue", "medium green", "pale red", "amber", "greyish", "dusty purple"]
    
    # Plot time series
    i = 0
    for ts_name, ts_data_dict in normalized_ts_dict.items():

        # Order of the line
        if 'zorder' in ts_data_dict.keys():
            zorder = ts_data_dict['zorder']
        else:
            zorder = None

        # Color of the line
        if 'color' in ts_data_dict.keys():
            color = ts_data_dict['color']
        else:
            color = sns.xkcd_rgb[colors[i]]

        # Alpha value of the line
        if 'alpha' in ts_data_dict.keys():
            alpha = ts_data_dict['alpha']
        else:
            alpha = DEFAULT_ALPHA

        # Plot with x-axis if xvec is specified
        if 'xvec' in ts_data_dict.keys():
            
            # Plot with markers if marker is specified 
            if 'marker' in ts_data_dict.keys():
                plt.plot(ts_data_dict['xvec'], ts_data_dict['ts_vector'], ax= ax, lw= ts_data_dict['lw'], label = ts_name, marker = ts_data_dict['marker'], ls = ts_data_dict['linestyle'], alpha = alpha, ms = DEFAULT_MARKERSIZE, color = color, zorder= zorder)
            else:
                plt.plot(ts_data_dict['xvec'], ts_data_dict['ts_vector'], ax= ax, lw= ts_data_dict['lw'], label = ts_name, ls = ts_data_dict['linestyle'], alpha = alpha, color = color, zorder=zorder)
        # Plot without x-axis if xvec is not specified
        else:
            if 'marker' in ts_data_dict.keys():
                plt.plot(ts_data_dict['ts_vector'], lw= ts_data_dict['lw'], ax= ax, label = ts_name, marker = ts_data_dict['marker'], ls = ts_data_dict['linestyle'], alpha = alpha, ms = DEFAULT_MARKERSIZE, color = color, zorder=zorder)
            else:
                plt.plot(ts_data_dict['ts_vector'], lw= ts_data_dict['lw'], ax= ax, label = ts_name, ls = ts_data_dict['linestyle'], alpha = alpha, color = color, zorder=zorder)

        #plt.hold(True)

        i += 1

    # Set labels 
    if fontsize:
        if xlabel:
            plt.xlabel(xlabel, fontsize=fontsize)
        if ylabel:
            plt.ylabel(ylabel, fontsize=fontsize)
    else:
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)

    # Set x-axis ticks
    if xticks:
        plt.xticks(xticks)

    # Set y-axis limits
    if ylim:
        plt.ylim(ylim)

    # Plot legend
    if legend_present:
        print('legend present!')
        plt.legend(loc = 'best')


        #if i % 2 == 0:
        #    ncol = 2
        #elif i % 3 == 0:
        #    ncol = 3
        #else:
        #    ncol = 1
        #plt.legend(loc='best', bbox_to_anchor = (0., 1.02, 1., .102), ncol = ncol, fontsize ='x-small')

    # Set title if not none
    if title_str is not None:
        plt.title(title_str, fontsize=fontsize)
    
    # Delete y-axis ticks if specified
    if delete_yticks:
        plt.yticks([])
