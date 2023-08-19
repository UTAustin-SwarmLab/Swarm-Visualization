
def plot_grouped_violinplot(df = None, x_var = None, y_var = None, plot_file = None, ylim = None, title_str = None, order_list = None, pal = None, ax= None) -> None:
    """
    Plots a grouped violinplot
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

    # Creates a figure
    fig = plt.figure()

    # Plots a violinplot
    if not pal:
        if order_list:
            plot = sns.violinplot(x=x_var, y=y_var, data=df, order = order_list, ax = ax)
        else:
            plot = sns.violinplot(x=x_var, y=y_var, data=df, order = order_list, ax = ax)

    # Plots a violinplot with palette
    if pal:
        if order_list:
            plot = sns.violinplot(x=x_var, y=y_var, data=df, order = order_list, palette = pal, ax = ax)
        else:
            plot = sns.violinplot(x=x_var, y=y_var, data=df, order = order_list, palette = pal, ax = ax)

    # Sets y-axis limits
    if ylim:
        plt.ylim(ylim[0], ylim[1])

    # Sets title
    if title_str:
        plt.title(title_str)

