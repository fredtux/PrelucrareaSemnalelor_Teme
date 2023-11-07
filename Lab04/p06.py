import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.io import wavfile

pdf = []
pdfDoc = PdfPages('p06.pdf')

sample_rate, signal = wavfile.read("p05.wav")

# Ia pas de 1%
step = int(len(signal) * 0.01)
total_len = step * 100 - (step if step * 100 != len(signal) else 0) # Scot ultimul grup daca nu are suficiente esantioane

# Grupuri de 1% cu 50% suprapunere
groups = []
for i in range(0, total_len, step // 2):
    groups.append(signal[i:i + step])


# FFT pentru fiecare grup
fft_left = []
fft_right = []
for group in groups:
    fft_left.append(np.abs(np.fft.fft(group[:,0])))
    fft_right.append(np.abs(np.fft.fft(group[:,1])))
       
# Pe fiecare coloana a matricii - deci facem transpusa
fft_left = np.array(fft_left).T
fft_right = np.array(fft_right).T

fig, ax = plt.subplots(2)

ax[0].set_title('FFT stanga')
ax[0].imshow(np.log(fft_left), aspect='auto')

ax[1].set_title('FFT dreapta')
ax[1].imshow(np.log(fft_right), aspect='auto')

pdf.append(fig)
fig.savefig('p06.png')

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()