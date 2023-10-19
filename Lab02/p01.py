import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p01.pdf')

fig, axs = plt.subplots(2)

t = np.linspace(0, 3, 1600)
s = 2 * np.sin(2*np.pi*1600*t + 2)
axs[0].plot(t, s)
axs[0].legend('Sin')

c = 2 * np.cos(np.pi/2 - (2*np.pi*1600*t + 2))
axs[1].plot(t, c)
axs[1].legend('Cos')

pdf.append(fig)


for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()
