import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p02.pdf')

fig, axs = plt.subplots(4)

phi = [1, 2, 10, 13]

t = np.linspace(0, 3, 1600)
s = np.sin(2*np.pi*1600*t)

signals = []

for i in range(len(phi)):
    s_el = np.sin(2*np.pi*1600*t + phi[i])
    axs[i].plot(t, s_el)
    signals.append(s_el)
    

fig.suptitle(f'Fazele {",".join([str(i) for i in phi])}')

pdf.append(fig)

snrs = [0.1, 1, 10, 100]



for i in range(len(snrs)):
    fig, axs = plt.subplots(len(signals))
    fig.suptitle(f"SNR {snrs[i]}")
    
    for j in range(len(signals)):
        noised_signal = [x for x in signals[j]]
        
        noise = np.random.normal(0, 1, len(t))
        gamma = np.sqrt(np.linalg.norm(noised_signal) / (np.linalg.norm(noise) * snrs[i]))
        noised_signal = noised_signal + noise * gamma
        axs[j].plot(t, noised_signal)
    pdf.append(fig)
    


for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()
