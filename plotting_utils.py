#!/usr/bin/env python
import sys,os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from typing import Union, List, Dict, Tuple, Any, Optional


FONT_SIZE = 20
sns.set_color_codes()

plt.rc('text', usetex=True)
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : FONT_SIZE}
plt.rc('font', **font)
plt.rcParams['text.latex.preamble'] = [r'\boldmath']

LEGEND_FONT_SIZE = 14
XTICK_LABEL_SIZE = 14
YTICK_LABEL_SIZE = 14

plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["font.weight"] = "bold"
#matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]


import matplotlib.pylab as pylab
params = {'legend.fontsize': LEGEND_FONT_SIZE,
         'axes.labelsize': FONT_SIZE,
         'axes.titlesize': FONT_SIZE,
         'xtick.labelsize': XTICK_LABEL_SIZE,
         'ytick.labelsize': YTICK_LABEL_SIZE,
         'figure.autolayout': True}
pylab.rcParams.update(params)
plt.rcParams["axes.labelweight"] = "bold"


from textfile_utils import *


def normalize_ts(input_ts, zero_one_norm = False):
    """
    Normalizes a time series
    :param input_ts: input time series
    :param zero_one_norm: whether to normalize between 0 and 1
    :return: normalized time series
    """
    
    # Get min, max, std, and mean
    min_ts = np.min(input_ts)
    max_ts = np.max(input_ts)
    std_ts = np.nanstd(input_ts)
    mean_ts = np.nanmean(input_ts)

    # Normalize time series
    if zero_one_norm:
        normalized_ts = [(x - min_ts)/(max_ts - min_ts) for x in input_ts]
    else:
        normalized_ts = [(x - mean_ts)/std_ts for x in input_ts]

    # Return normalized time series
    return normalized_ts

if __name__ == "__main__":
    print('hello')

    # Test basic plot
