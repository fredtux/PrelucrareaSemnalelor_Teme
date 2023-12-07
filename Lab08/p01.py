import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p01.pdf')

# a)
N = 1000
t = np.linspace(0, 1, N)

# Trend
trend = 3 * t**2 + 2 * t + 1

# Seasonality
seasonality = np.cos(2 * np.pi * t * 15) + np.sin(2 * np.pi * t * 5)

# Noise
noise = np.random.normal(0, 0.05, N)

# Time series
ts = trend + seasonality + noise

fig, axs = plt.subplots(4)
axs[0].plot(t, trend)
axs[0].set_title('Trend')
axs[1].plot(t, seasonality)
axs[1].set_title('Seasonality')
axs[2].plot(t, noise)
axs[2].set_title('Noise')
axs[3].plot(t, ts)
axs[3].set_title('Time Series')

pdf.append(fig)
fig.savefig("p01a.png")

# b)
acorr = np.correlate(ts, ts, mode='full')



for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()