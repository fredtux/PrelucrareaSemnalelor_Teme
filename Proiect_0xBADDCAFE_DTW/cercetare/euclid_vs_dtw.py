import numpy as np
from fastdtw import fastdtw
from matplotlib import pyplot as plt
from dtaidistance import dtw as dtw_dta, ed
import time
from tslearn.metrics import dtw_path, dtw as ts_dtw
from pyts.metrics import dtw as pyts_dtw
# from dtw import *

t = np.linspace(0, 0.02, 3200)

sinusoidal_a = np.sin(2*np.pi*800*t)
sinusoidal_b = np.sin(2*np.pi*800*t + np.pi/4)

# Euclidian distance
euclidian_distance = ed.distance(sinusoidal_a, sinusoidal_b)

# DTW distance
dtadistance_time = time.time()
distance, warp_path = dtw_dta.warping_paths(sinusoidal_a, sinusoidal_b, use_c=True)
dtadistance_time = time.time() - dtadistance_time

print(f"DTA distance time: {dtadistance_time}")

print(f"Euclidian distance: {euclidian_distance}")
# print(f"DTW distance: {distance}")

# fig, ax = plt.subplots()
# ax.plot(sinusoidal_a, label='A', color='red')
# ax.plot(sinusoidal_b, label='B', color='blue')

# # for [map_x, map_y] in warp_path:
# #     ax.plot([map_x, map_y], [sinusoidal_a[map_x], sinusoidal_b[map_y]], '-k')

# plt.show()

tslearn_time = time.time()
path, distance = dtw_path(sinusoidal_a, sinusoidal_b)
tslearn_time = time.time() - tslearn_time

print(f"Tslearn time: {tslearn_time}")
print(f"Tslearn distance: {distance}")


pyts_time = time.time()
distance = pyts_dtw(sinusoidal_a, sinusoidal_b)
pyts_time = time.time() - pyts_time

print(f"DTW time: {pyts_time}")