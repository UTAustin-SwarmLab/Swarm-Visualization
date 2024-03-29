import seaborn as sns

from swarm_visualizer.utility.general_utils import set_axis_infos

def plot_grouped_barplot(
    df=None,
    x_var=None,
    y_var=None,
    ylim=None,
    title_str=None,
    pal=None,
    ax=None,
    y_label=None,
) -> None:
    """Plots a grouped barplot. In this case, there are multiple y-var for each x-var.

    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param pal: palette
    :param ax: axis to plot on
    :return: None.
    """
    if not pal:
        df.plot(kind="bar", stacked=False, ax=ax, x=x_var, y=y_var)

    if pal:
        colors = [pal(i) for i in range(len(x_var))]
        df.plot(
            kind="bar", stacked=False, ax=ax, x=x_var, y=y_var, colors=colors
        )

    ### set y label
    if y_label:
        ax.set_ylabel(y_label)

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)

def plot_sns_grouped_barplot(
    df=None,
    x_var=None,
    y_var=None,
    hue=None,
    ylim=None,
    title_str=None,
    pal=None,
    ax=None,
    y_label=None,
) -> None:
    """Plots a grouped barplot with sns. hue specifies the group.

    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param pal: palette
    :param ax: axis to plot on
    :return: None.
    """
    if not pal:
        sns.barplot(ax=ax, x=x_var, y=y_var, hue=hue, data=df)

    if pal:
        colors = [pal(i) for i in range(len(x_var))]
        sns.barplot(
            ax=ax, x=x_var, y=y_var, palette=colors, hue=hue, data=df
        )

    ### set y label
    if y_label:
        ax.set_ylabel(y_label)

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)



def plot_stacked_barplot(
    df=None,
    x_var=None,
    y_var=None,
    ylim=None,
    title_str=None,
    pal=None,
    ax=None,
    y_label=None,
) -> None:
    """Plots a grouped barplot.

    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param ylim: y-axis limits
    :param title_str: title of the plot
    :param pal: palette
    :param ax: axis to plot on
    :return: None.
    """
    if not pal:
        df.plot(kind="bar", stacked=True, ax=ax, x=x_var, y=y_var)

    if pal:
        colors = [pal(i) for i in range(len(x_var))]
        df.plot(
            kind="bar", stacked=True, ax=ax, x=x_var, y=y_var, colors=colors
        )

    ### set y label
    if y_label:
        ax.set_ylabel(y_label)

    # Set axis infos
    set_axis_infos(ax, ylim=ylim, title_str=title_str)
