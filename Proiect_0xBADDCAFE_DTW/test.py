import pandas as pd
import numpy as np

# Plotting Packages
import matplotlib.pyplot as plt
import seaborn as sbn

# Configuring Matplotlib
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
savefig_options = dict(format="png", dpi=300, bbox_inches="tight")

# Computation packages
from scipy.spatial.distance import euclidean
from dtaidistance import dtw, dtw_visualisation as dtwvis


t = np.linspace(0, 1, 50)

x1 = np.sin(2*np.pi*2*t + np.pi/4)
x2 = 2 * np.sin(2*np.pi*2*t)


warp_path = dtw.warping_path(x1, x2, use_c=False)


fig, ax = dtwvis.plot_warping(x1, x2, warp_path)

fig.savefig("ex2_dtw_distance.png", **savefig_options)