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

def save_fig(fig,save_loc:str = None, dpi:int = 600) -> None:
    fig.savefig(save_loc, dpi = dpi)
    plt.close("all")
