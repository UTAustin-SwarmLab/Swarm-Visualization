import seaborn as sns

from swarm_visualizer.utility import set_axis_infos

"""
paired boxplot, hue is a name of a column that controls what to pair by
"""


def plot_paired_boxplot(
    ax,
    df=None,
    x_var=None,
    y_var=None,
    ylim=None,
    title_str=None,
    order_list=None,
    pal=None,
    hue=None,
    **kwargs,
) -> None:
    """Plots a paired boxplot.

    :param ax: axis to plot on
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param order_list: order of the x-axis variable
    :param pal: palette
    :param hue: hue variable
    :return: None.
    """
    # Plots a boxplot
    if not pal:
        # Plots a boxplot with order
        if order_list:
            sns.boxplot(
                x=x_var,
                y=y_var,
                data=df,
                order=order_list,
                hue=hue,
                ax=ax,
                **kwargs,
            )
        else:
            sns.boxplot(
                x=x_var,
                y=y_var,
                data=df,
                order=order_list,
                hue=hue,
                ax=ax,
                **kwargs,
            )

    # Plots a boxplot with palette
    if pal:
        if order_list:
            sns.boxplot(
                x=x_var,
                y=y_var,
                data=df,
                order=order_list,
                palette=pal,
                hue=hue,
                ax=ax,
                **kwargs,
            )
        else:
            sns.boxplot(
                x=x_var,
                y=y_var,
                data=df,
                order=order_list,
                palette=pal,
                hue=hue,
                ax=ax,
                **kwargs,
            )

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)


"""
no pairing
"""


def plot_grouped_boxplot(
    ax,
    df=None,
    x_var=None,
    y_var=None,
    ylim=None,
    title_str=None,
    order_list=None,
    pal=None,
    **kwargs,
) -> None:
    """Plots a grouped boxplot.

    :param ax: axis to plot on
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param order_list: order of the x-axis variable
    :param pal: palette
    :return: None.
    """
    if not pal:
        if order_list:
            sns.boxplot(
                x=x_var, y=y_var, data=df, order=order_list, ax=ax, **kwargs
            )
        else:
            sns.boxplot(
                x=x_var, y=y_var, data=df, order=order_list, ax=ax, **kwargs
            )

    if pal:
        if order_list:
            sns.boxplot(
                x=x_var,
                y=y_var,
                data=df,
                order=order_list,
                palette=pal,
                ax=ax,
                **kwargs,
            )
        else:
            sns.boxplot(
                x=x_var,
                y=y_var,
                data=df,
                order=order_list,
                palette=pal,
                ax=ax,
                **kwargs,
            )

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)
