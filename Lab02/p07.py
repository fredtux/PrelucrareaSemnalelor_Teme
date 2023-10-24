import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p07.pdf')

fig, axs = plt.subplots(2)

fs = 1000
t = np.linspace(0, 0.01, fs)

sign_original = np.sin(2*np.pi*800*t)

# a)
sign_a = sign_original[::4]
t_a = t[::4]


axs[0].plot(t, sign_original)
axs[1].plot(t_a, sign_a)


fig.suptitle('a)')
pdf.append(fig)

# In sign_a avem mai putine puncte, dar algoritmul de interpolare le face sa para identice

# b)
fig, axs = plt.subplots()

sign_b = [el for index, el in enumerate(sign_original) if index % 4 == 1]
t_b = [el for index, el in enumerate(t) if index % 4 == 1]

axs.plot(t_b, sign_b)

fig.suptitle('b)')

pdf.append(fig)

# La fel ca la a)

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()