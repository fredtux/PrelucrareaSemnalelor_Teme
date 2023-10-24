import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p04.pdf')

fig, axs = plt.subplots(3)

t = np.linspace(0, 3, 800)

sign_sin = np.sin(2*np.pi*800*t)
sign_saw = np.mod(t, 1.0/1600) * 1600

sign_sum = sign_sin + sign_saw

axs[0].plot(t, sign_sin)
axs[1].plot(t, sign_saw)
axs[2].plot(t, sign_sum)

fig.suptitle(f'Sinus, sawtooth, suma')

pdf.append(fig)

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()