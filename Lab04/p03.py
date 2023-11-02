import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from time import time

pdf = []
pdfDoc = PdfPages('p03.pdf')

f0 = 10
fs = 12
t = np.arange(0, 1, 1/fs)
t2 = np.arange(0, 1, 1/(200 * f0))
signal = np.sin(2 * np.pi * f0 * t)
signal_good = np.sin(2 * np.pi * f0 * t2)

fig, axs = plt.subplots(3)

axs[0].plot(t, signal, color='blue')
axs[0].stem(t, signal)
axs[0].plot(t2, signal_good, color='red')

K = [2, 3]
for k in range(len(K)):
    signal_sim = np.sin(2 * np.pi * (f0 + K[k] * fs) * t)
    axs[k + 1].stem(t, signal_sim)
    axs[k + 1].plot(t, signal_sim)
    
    signal_sim_good = np.sin(2 * np.pi * (f0 + K[k] * fs) * t2)
    axs[k + 1].plot(t2, signal_sim_good, color='red')

pdf.append(fig)
fig.savefig('p03.png')

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()