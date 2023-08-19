import sys,os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Add path to plotting_utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plotting_utils import *

# Example Plots location
example_plot_folder_loc = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'example_plots'))


def test_paired_boxplot(df,x_var,y_var,hue) -> None:
    """
    Tests paired boxplot
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :return: None
    """

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a paired boxplot
    plot_paired_boxplot(df = df, x_var = x_var, y_var = y_var,hue=hue, title_str = 'Paired Boxplot', ax = ax)

    # Save the plot
    save_loc = os.path.join(example_plot_folder_loc,"boxplots", 'paired_boxplot.png')
    save_fig(fig,save_loc,dpi = 600)

def test_grouped_boxplot(df,x_var,y_var) -> None:
    """
    Tests grouped boxplot
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :return: None
    """

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a grouped boxplot
    plot_grouped_boxplot(df = df, x_var = x_var, y_var = y_var, title_str = 'Grouped Boxplot', ax = ax)

    # Save the plot
    save_loc = os.path.join(example_plot_folder_loc,"boxplots", 'grouped_boxplot.png')
    save_fig(fig,save_loc,dpi = 600)


if __name__ == '__main__':

    # Set seed for reproducibility
    np.random.seed(0)

    # Generate a time series with a linear trend
    x1_data = np.arange(0, 5, 0.05) + np.random.normal(0, 0.1, 100)
    x2_data = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)

    # Concatenate the data
    x_data = np.concatenate([x1_data, x2_data])
    x_label = np.concatenate([np.repeat('x1',100),np.repeat('x2',100)])

    # Additional Groupings in each x with groups of 50 as group a and group b
    groups = np.concatenate([np.repeat('a',50),np.repeat('b',50),np.repeat('a',50),np.repeat('b',50)])


    df = pd.DataFrame({'y': x_data, 'x_label': x_label, 'groups': groups})

    # Test paired boxplot
    test_paired_boxplot(df = df, x_var = 'x_label', y_var = 'y',hue = 'groups')

    # Test grouped boxplot
    test_grouped_boxplot(df = df, x_var = 'x_label', y_var = 'y')

