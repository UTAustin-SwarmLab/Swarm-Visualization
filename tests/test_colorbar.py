from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
import seaborn as sns

from swarm_visualizer import plot_basic_scatterplot

from swarm_visualizer.utility import save_fig, set_plot_properties, create_colorbar

# Example Plots location
_X_DATA = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)
_Y_DATA = np.arange(0, 10, 0.1) + np.random.normal(0, 0.1, 100)

_DISCRETE_NUMERICAL_LABEL_DATA = [ i//10 for i in range(100)]
_DISCRETE_CATEGORY_LABEL_DATA = ["Group "+str(i//10) for i in range(100)]
_CONTINUOUS_LABEL_DATA = [np.random.rand()+i for i in range(100)]

_DATA_FRAME = pd.DataFrame({"x": _X_DATA, "y": _Y_DATA, "discrete_numerical_label": _DISCRETE_NUMERICAL_LABEL_DATA,
                            "discrete_category_label": _DISCRETE_CATEGORY_LABEL_DATA, "continuous_label": _CONTINUOUS_LABEL_DATA})

_DISCRETE_CATEGORY_VISIBLE_LABEL_DATA = ["Group 1", "Group 5", "Group 6", "Group 9"]
_CONTINUOUS_VISIBLE_LABEL_DATA = [2.5, 45, 88, 50]

_CONTINUOUS_PALETTE = "magma"
_DISCRETE_PALETTE = "tab20"
_DISCRETE_COLORS = ["red", "blue", "green", "yellow" , "black", "purple", "orange", "brown", "pink", "gray"]




_SAVE_LOC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "example_plots")
)

@pytest.mark.parametrize(
        ("x_data", "y_data", "discrete_numerical_label_data","discrete_palette"), [(_X_DATA, _Y_DATA, _DISCRETE_NUMERICAL_LABEL_DATA, _DISCRETE_PALETTE)]
)
def test_basic_discrete_colorbar(x_data, y_data, discrete_numerical_label_data, discrete_palette) -> None:
    """Tests basic discrete colorbar.

    :param x_data: x-axis data
    :param y_data: y-axis data
    :param discrete_numerical_label_data: discrete numerical label data
    :param discrete_palette: discrete palette
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(12, 10), nrows=1, ncols=2, dpi=600, gridspec_kw={ 'width_ratios': [1, 0.03]})
    

    # Unique values in the discrete numerical label data
    unique_values = np.unique(discrete_numerical_label_data)

    # Create a basic scatter plot first
    palette_colors = sns.color_palette(discrete_palette, len(unique_values))

    # Find colors for each value in the discrete numerical label data
    colors = [palette_colors[unique_values.tolist().index(i)] for i in discrete_numerical_label_data]

    plot_basic_scatterplot(ax[0], x=x_data, y=y_data, color=colors,
                            title_str= "Basic Scatter Plot with Discrete Colorbar",
                            ylabel="$y$",
                            lw=3.0,
                            ylim=None,
                            xlabel="$x$",
                            xlim=None,
                            ms=10.0)
    
    create_colorbar(ax[1], unique_values, palette=discrete_palette, discrete=True)

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "colorbars", "discrete_colorbar_with_all_labels.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(
        ("x_data", "y_data", "discrete_category_label_data", "discrete_category_visible_label_data" ,"discrete_colors"), [(_X_DATA, _Y_DATA, _DISCRETE_CATEGORY_LABEL_DATA,_DISCRETE_CATEGORY_VISIBLE_LABEL_DATA, _DISCRETE_COLORS)]
)
def test_discrete_colorbar_w_limited_visible(x_data, y_data, discrete_category_label_data,discrete_category_visible_label_data, discrete_colors) -> None:
    """Tests basic discrete colorbar.

    :param x_data: x-axis data
    :param y_data: y-axis data
    :param discrete_category_label_data: discrete categorical label data
    :param discrete_category_visible_label_data: discrete categorical label data
    :param discrete_palette: discrete palette
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(12, 10), nrows=1, ncols=2, dpi=600, gridspec_kw={ 'width_ratios': [1, 0.03]})
    

    # Unique values in the discrete numerical label data
    unique_values = np.unique(discrete_category_label_data).tolist()

    # Find colors for each value in the discrete numerical label data
    colors = [discrete_colors[unique_values.index(i)] for i in discrete_category_label_data]

    plot_basic_scatterplot(ax[0], x=x_data, y=y_data, color=colors,
                            title_str= "Basic Scatter Plot with Discrete Colorbar",
                            ylabel="$y$",
                            lw=3.0,
                            ylim=None,
                            xlabel="$x$",
                            xlim=None,
                            ms=10.0)
    
    create_colorbar(ax[1], unique_values, visible_labels=discrete_category_visible_label_data, colors=discrete_colors, discrete=True)

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "colorbars", "discrete_colorbar_with_some_labels.png")
    save_fig(fig, save_loc, dpi=600)


@pytest.mark.parametrize(
        ("data_frame","x_var", "y_var", "hue","continuous_palette"), [(_DATA_FRAME,"x", "y", "continuous_label", _CONTINUOUS_PALETTE)]
)
def test_basic_continous_colorbar(data_frame,x_var, y_var, hue, continuous_palette) -> None:
    """Tests basic discrete colorbar.

    :param data_frame: data frame
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :param continuous_palette: continuous palette
    :return: None
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(12, 10), nrows=1, ncols=2, dpi=600, gridspec_kw={ 'width_ratios': [1, 0.03]})
    
    sns.scatterplot(data=data_frame, x=x_var, y=y_var, hue=hue, palette=continuous_palette, ax=ax[0], 
                    s=100,legend=False)

    create_colorbar(ax[1], data_frame[hue], title="Continuous Colorbar",palette=continuous_palette)

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "colorbars", "continous_colorbar.png")
    save_fig(fig, save_loc, dpi=600)

@pytest.mark.parametrize(
        ("data_frame","x_var", "y_var", "hue", "continuous_visible","continuous_palette"), [(_DATA_FRAME,"x", "y", "continuous_label",_CONTINUOUS_VISIBLE_LABEL_DATA, _CONTINUOUS_PALETTE)]
)
def test_continous_colorbar_w_limited_visible(data_frame,x_var, y_var, hue,continuous_visible, continuous_palette) -> None:
    """Tests basic discrete colorbar.

    :param data_frame: data frame
    :param x_var: x-axis variable
    :param y_var: y-axis variable
    :param hue: hue variable
    :param continuous_visible: continuous visible labels
    :param continuous_palette: continuous palette
    """
    # Sets plot style
    set_plot_properties()

    fig, ax = plt.subplots(figsize=(10, 12), nrows=2, ncols=1, dpi=600, gridspec_kw={ 'height_ratios': [1, 0.03]})
    
    sns.scatterplot(data=data_frame, x=x_var, y=y_var, hue=hue, palette=continuous_palette, ax=ax[0], 
                    s=100,legend=False)

    create_colorbar(ax[1], data_frame[hue],title="Continuous Colorbar",visible_labels=continuous_visible, palette=continuous_palette, orientation="horizontal")

    # Save the plot
    save_loc = os.path.join(_SAVE_LOC, "colorbars", "continous_limited_data_colorbar.png")
    plt.tight_layout()
    save_fig(fig, save_loc, dpi=600)