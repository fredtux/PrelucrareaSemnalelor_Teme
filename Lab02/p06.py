import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p06.pdf')

fig, axs = plt.subplots(3)

t = np.linspace(0, 0.03, 1600)

fs = 800
sign1 = np.sin(2*np.pi*(fs/2.0)*t)
sign2 = np.sin(2*np.pi*(fs/4.0)*t)
sign3 = np.sin(2*np.pi*0*t)


axs[0].plot(t, sign1)
axs[1].plot(t, sign2)
axs[2].plot(t, sign3)

fig.suptitle(f'fs/2, fs/4, 0')

pdf.append(fig)

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()

# Diferenta dintre primele 2 semnale consta in frecventa, o frecventa mai mica inseamna un sunet mai jos (problema anterioara) si deci mai putine oscilatii pe secunda
# Al 3-lea semnal este un semnal constant, deci nu se aude nimic si apare ca o linie dreapta pe grafic