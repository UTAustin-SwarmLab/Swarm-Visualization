import seaborn as sns
from typing import Dict

from .general_utils import set_axis_infos


def basic_plot_ts(ts_vector = None, title_str:str = None, ylabel:str = None, lw:float =3.0, ylim = None, xlabel:str = 'time', ax = None) -> None:
    """
    Basic plot of a time series
    :param ts_vector: time series
    :param title_str: title of the plot
    :param ylabel: y-axis label
    :param lw: line width
    :param ylim: y-axis limits
    :param xlabel: x-axis label
    :param ax: axis to plot on
    :return: None
    """

    # Plot time series
    ax.plot(ts_vector, lw=lw)

    set_axis_infos(ax, xlabel=xlabel,ylabel=ylabel, ylim = ylim, title = title_str)


def overlaid_ts(normalized_ts_dict:Dict = None, title_str:str = None, 
                ylabel:str = None, xlabel:str = 'time', fontsize:float = 30, xticks = None, 
                ylim = None, DEFAULT_ALPHA:float = 1.0, legend_present:bool = True, 
                DEFAULT_MARKERSIZE:float = 15, delete_yticks:bool = False, ax = None) -> None:
    """
    Overlaid time series plot
    :param normalized_ts_dict: dictionary with time series to plot
    :param title_str: title of the plot
    :param ylabel: y-axis label
    :param xlabel: x-axis label
    :param fontsize: font size
    :param xticks: x-axis ticks
    :param ylim: y-axis limits
    :param DEFAULT_ALPHA: default alpha value
    :param legend_present: whether to plot the legend
    :param DEFAULT_MARKERSIZE: default marker size
    :param delete_yticks: whether to delete the y-axis ticks
    :param ax: axis to plot on
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
                ax.plot(ts_data_dict['xvec'], ts_data_dict['ts_vector'], lw= ts_data_dict['lw'], label = ts_name, marker = ts_data_dict['marker'], ls = ts_data_dict['linestyle'], alpha = alpha, ms = DEFAULT_MARKERSIZE, color = color, zorder= zorder)
            else:
                ax.plot(ts_data_dict['xvec'], ts_data_dict['ts_vector'], lw= ts_data_dict['lw'], label = ts_name, ls = ts_data_dict['linestyle'], alpha = alpha, color = color, zorder=zorder)
        # Plot without x-axis if xvec is not specified
        else:
            if 'marker' in ts_data_dict.keys():
                ax.plot(ts_data_dict['ts_vector'], lw= ts_data_dict['lw'], label = ts_name, marker = ts_data_dict['marker'], ls = ts_data_dict['linestyle'], alpha = alpha, ms = DEFAULT_MARKERSIZE, color = color, zorder=zorder)
            else:
                ax.plot(ts_data_dict['ts_vector'], lw= ts_data_dict['lw'], label = ts_name, ls = ts_data_dict['linestyle'], alpha = alpha, color = color, zorder=zorder)

        i += 1


    # Set labels 
    if fontsize:
        if xlabel:
            ax.set_xlabel(xlabel, fontsize=fontsize)
        if ylabel:
            ax.set_ylabel(ylabel, fontsize=fontsize)
    else:
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)


    # Set x-axis ticks
    if xticks:
        ax.set_xticks(xticks)

    # Set y-axis limits
    if ylim:
        ax.set_ylim(ylim[0], ylim[1])

    # Plot legend
    if legend_present:
        print('legend present!')
        ax.legend(loc = 'best')

    # Set title if not none
    if title_str is not None:
        ax.set_title(title_str, fontsize=fontsize)
    
    # Delete y-axis ticks if specified
    if delete_yticks:
        ax.set_yticks([])
