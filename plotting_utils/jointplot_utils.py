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

def seaborn_jointplot(x = None, y = None, df = None, title_str = None, plot_file = None):
    """
    Plots a jointplot
    :param x: x-axis variable
    :param y: y-axis variable
    :param df: dataframe
    :param title_str: title of the plot
    :param plot_file: file to save the plot
    :return: None
    """

    # Plots a jointplot
    sns.jointplot(x=x, y= y , data=df, kind="kde");
    plt.title(title_str)
    plt.savefig(plot_file)
    plt.close()
