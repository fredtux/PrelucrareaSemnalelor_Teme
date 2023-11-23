import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p03.pdf')

f = 100
t = np.linspace(0, 0.1, 2*f)

sin_signal = 1 * np.sin(2 * np.pi * f * t + 0)

def rect_window_create(N):
    result =  np.zeros(N)
    result[N//4:3*N//4] = 1
    return result

def hann_window_create(N):
    return 0.5 * (1 - np.cos(2 * np.pi * np.arange(N) / N))

win_rect = rect_window_create(len(sin_signal))
win_hann = hann_window_create(len(sin_signal))
# win_hann_debug = np.hanning(len(sin_signal))

fig, axs = plt.subplots(4)
axs[0].plot(t, sin_signal)
axs[1].plot(t, sin_signal * win_rect)
axs[2].plot(t, sin_signal * win_hann)
# axs[3].plot(t, sin_signal * win_hann_debug)

pdf.append(fig)
fig.savefig("p03.png")

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()