import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from time import time

pdf = []
pdfDoc = PdfPages('p01.pdf')


def fourier_matrix(N):
    dft = []
    for row in range(N):
        dft.append([])
        
        for k in range(N):
            dft[row].append(np.exp(-2j * np.pi * k  * row/ N))
    
    return dft

N = [128, 256, 512, 1024, 2048, 4096, 8192]

times_py = []
times_np = []

for n in N:
    time_start = time()
    fourier_matrix(n)
    time_end = time()
    
    times_py.append(time_end - time_start)
    
    time_start = time()
    np.fft.fft(np.zeros(n))
    time_end = time()
    
    times_np.append(time_end - time_start)
    
# Log-log plot
fig, axs = plt.subplots(1)
axs.set_yscale('log')

axs.plot(N, times_py, label='Python')
axs.plot(N, times_np, label='Numpy')

pdf.append(fig)
fig.savefig('p01.png')

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()