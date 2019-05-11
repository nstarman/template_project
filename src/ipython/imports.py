#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# TITLE   : Standard Import File
# AUTHOR  : Nathaniel Starkman
# PROJECT :
#
# ----------------------------------------------------------------------------

### Docstring and Metadata
r"""standard import file.
imports:

GENERAL
-------
os, sys  # operating system
time
pdb
warnings

numpy -> np

# scipy
scipy
.stats.binned_statistic -> binned_stats

tqdm.autonotebook.tqdm -> tqdm


ASTROPY
-------
astropy
.units -> u
.coordinates -> coords
    .SkyCoord
.table.Table, QTable
.visualization.quantity_support, astropy_mpl_style

**also does:
quantity_support()
plt.style -> astropy_mpl_style


PLOTTING
--------
starkplot -> plt
.mpl_decorator

matplotlib -> mpl
.colors
.cm


IPYTHON
-------
display, Latex, Markdown, set_trace,
printmd, printltx

**also does:
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
InteractiveShell.ast_node_interactivity = "all"
"""

__author__ = "Nathaniel Starkman"


##############################################################################
### Imports

# +---------------------------------------------------------------------------+
# Basic

import os, sys                        # operating system
import time                           # timing
import pdb                            # debugging 
import warnings                       # warning
import logging                        # for logging
# warnings.filterwarnings('ignore', RuntimeWarning)

# Numpy
import numpy as np  # numerical python
import scipy        # scientific python    

# +------------------------+
# TODO filter TqdmExperimentalWarning
from tqdm.autonotebook import tqdm

# +---------------------------------------------------------------------------+
# Astropy
import astropy

from astropy import units as u             # units TODO replace with mine
from astropy import coordinates as coords  # coordinates 

from astropy.coordinates import SkyCoord
from astropy.table import Table, QTable  # table data structure

# Allowing quantities in matplotlib
from astropy.visualization import quantity_support, astropy_mpl_style

# +---------------------------------------------------------------------------+
# Plotting

import starkplot as plt
from starkplot import mpl_decorator

# import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors
from matplotlib import cm

# try:  # improve matploblib backend
#     import seaborn
# except ImportError:
#     print("can't import seaborn, using default matplotlib.")

# +---------------------------------------------------------------------------+
# IPython Magic
try:
    get_ipython()  # checks inside iPython environment
except:  # TODO correct exception
    pass
else:
    # %run runs in the main namespace
    from src.ipython import display, Latex, Markdown, set_trace, printmd
    # this also does:
    #     %matplotlib inline
    #     %config InlineBackend.figure_format = 'retina'
    #     InteractiveShell.ast_node_interactivity = "all"


##############################################################################
### Code

# astropy changes
quantity_support()
plt.style.use(astropy_mpl_style)
