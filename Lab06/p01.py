import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p01.pdf')

x = np.random.random(100)

fig, axs = plt.subplots(4)

axs[0].plot(x)

def multiply(x):
    return np.convolve(x,x, mode='same')

axs[1].plot(multiply(x))
axs[2].plot(multiply(multiply(x)))
axs[3].plot(multiply(multiply(multiply(x))))

pdf.append(fig)
fig.savefig("p01.png")

# Se produce un semnal asemanator cu o distributie gaussiana

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()