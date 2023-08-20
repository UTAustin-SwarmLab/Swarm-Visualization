import sys,os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Add path to plotting_utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import plotting utils
from plotting_utils import *

# Example Plots location

example_plot_folder_loc = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'example_plots'))

def test_grouped_violinplot(df,x_var,y_var,hue) -> None:
    """
    Tests grouped violinplot
    :param df: dataframe
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :return: None
    """

    fig, ax = plt.subplots(figsize=(10, 10))
    # Create a grouped violinplot
    plot_grouped_violinplot(df = df, x_var = x_var, y_var = y_var, title_str = 'Grouped Violinplot', ax = ax)

    # Save the plot
    save_loc = os.path.join(example_plot_folder_loc,"violinplots", 'grouped_violinplot.png')
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


    df = pd.DataFrame({'y': x_data, '$x_{label}$': x_label, 'groups': groups})

    # Test grouped violinplot
    test_grouped_violinplot(df,x_var='$x_{label}$', y_var='y', hue='groups')