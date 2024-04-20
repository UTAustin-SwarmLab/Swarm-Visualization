import seaborn as sns

from swarm_visualizer.utility import set_axis_infos

def plot_grouped_barplot(
    ax,
    df=None,
    x_var=None,
    y_var=None,
    ylim=None,
    title_str=None,
    pal=None,
    y_label=None,
    **kwargs
) -> None:
    """Plots a grouped barplot. In this case, there are multiple y-var for each x-var.

    :param ax: axis to plot on
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param pal: palette
    :return: None.
    """
    if not pal:
        df.plot(kind="bar", stacked=False, ax=ax, x=x_var, y=y_var, **kwargs)

    if pal:
        colors = [pal(i) for i in range(len(x_var))]
        df.plot(
            kind="bar", stacked=False, ax=ax, x=x_var, y=y_var, colors=colors, **kwargs
        )

    ### set y label
    if y_label:
        ax.set_ylabel(y_label)

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)

def plot_sns_grouped_barplot(
    ax,
    df=None,
    x_var=None,
    y_var=None,
    hue=None,
    ylim=None,
    title_str=None,
    pal=None,
    y_label=None,
    **kwargs
) -> None:
    """Plots a grouped barplot with sns. hue specifies the group.

    :param ax: axis to plot on
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param pal: palette
    :return: None.
    """
    if not pal:
        sns.barplot(ax=ax, x=x_var, y=y_var, hue=hue, data=df, **kwargs)

    if pal:
        colors = [pal(i) for i in range(len(x_var))]
        sns.barplot(
            ax=ax, x=x_var, y=y_var, palette=colors, hue=hue, data=df, **kwargs
        )

    ### set y label
    if y_label:
        ax.set_ylabel(y_label)

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)



def plot_stacked_barplot(
    ax,
    df=None,
    x_var=None,
    y_var=None,
    ylim=None,
    title_str=None,
    pal=None,
    y_label=None,
    **kwargs
) -> None:
    """Plots a grouped barplot.

    :param ax: axis to plot on
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param pal: palette
    :return: None.
    """
    if not pal:
        df.plot(kind="bar", stacked=True, ax=ax, x=x_var, y=y_var, **kwargs)

    if pal:
        colors = [pal(i) for i in range(len(x_var))]
        df.plot(
            kind="bar", stacked=True, ax=ax, x=x_var, y=y_var, colors=colors, **kwargs
        )

    ### set y label
    if y_label:
        ax.set_ylabel(y_label)

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)
