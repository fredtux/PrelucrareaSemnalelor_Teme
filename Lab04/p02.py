import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from time import time

pdf = []
pdfDoc = PdfPages('p02.pdf')

f0 = 10
fs = 12
t = np.arange(0, 1, 1/fs)
signal = np.sin(2 * np.pi * f0 * t)

fig, axs = plt.subplots(3)

axs[0].plot(t, signal)
axs[0].stem(t, signal)

K = [2, 3]
for k in range(len(K)):
    signal_sim = np.sin(2 * np.pi * (f0 + K[k] * fs) * t)
    
    axs[k + 1].stem(t, signal_sim)
    axs[k + 1].plot(t, signal_sim)


pdf.append(fig)
fig.savefig('p02.png')

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()