import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p08.pdf')

a = np.arange(-np.pi/2, np.pi/2, 0.01)

fig, axs = plt.subplots(3)
sin_a = np.sin(a)

axs[0].plot(a, sin_a)
axs[1].plot(a, a)
axs[2].plot(a, a - sin_a)

fig.suptitle("sin(a) = a")

pdf.append(fig)

fig, axs = plt.subplots(3)

def pade(a):
    return (a - (7*a**3)/60) / (1 + (a**2)/20)

pade_a = pade(a)

axs[0].plot(a, sin_a)
axs[1].plot(a, pade_a)
axs[2].plot(a, sin_a - pade_a)

fig.suptitle("Pade")

pdf.append(fig)

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()