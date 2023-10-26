import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p01.pdf')


def fourier_matrix(N):
    dft = []
    for row in range(N):
        dft.append([])
        
        for k in range(N):
            dft[row].append(np.exp(-2j * np.pi * k  * row/ N))
    
    return dft

N = 8
f = fourier_matrix(N)

fig, axs = plt.subplots(N)

for row in range(N):
    axs[row].plot(np.real(f[row]))
    axs[row].plot(np.imag(f[row]))
    
pdf.append(fig)
fig.savefig('p01.png')

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()