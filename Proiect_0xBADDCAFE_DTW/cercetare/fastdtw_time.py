import numpy as np
import matplotlib.pyplot as plt
from fastdtw import fastdtw
import time
from dtaidistance import dtw
from scipy.spatial.distance import euclidean
from pyts.metrics import dtw as pyts_dtw

time1 = np.linspace(0, 0.02, 3200)

s1 = np.sin(2*np.pi*800*time1)
s2 = np.sin(2*np.pi*800*time1 + np.pi/4)

dtw_time = time.time()
# [distanta, potriviri] = DTW(s1, s2)
distanta = pyts_dtw(s1, s2)
dtw_time = time.time() - dtw_time

print(f"DTW time: {dtw_time}")
print(f"DTW distance: {distanta}")


fastdw_time = time.time()
distance= pyts_dtw(s1, s2, method='fast', options={'radius': 10})
fastdw_time = time.time() - fastdw_time

print(f"Fast DTW time: {fastdw_time}")
print(f"Fast DTW distance: {distance}")

fastdw_time = time.time()
distance= pyts_dtw(s1, s2, method='fast')
fastdw_time = time.time() - fastdw_time

print(f"Fast DTW time: {fastdw_time}")
print(f"Fast DTW distance: {distance}")