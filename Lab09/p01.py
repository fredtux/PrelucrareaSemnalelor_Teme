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
alpha = 0.2

s = np.zeros(N)
s[0] = ts[0]
for i in range(1, N):
    sum = 0
    for j in range(0, i):
        sum += (1 - alpha)**(i - j) * ts[j]
        
    s[i] = alpha * sum + (1 - alpha) * ts[0]
    
fig, axs = plt.subplots(2)
axs[0].plot(t, ts)
axs[0].set_title('Time Series')
axs[1].plot(t, s)
axs[1].set_title('Exponential Mediation')

pdf.append(fig)
fig.savefig("p01b.png")

# c)
q = 5
ma = np.zeros(N)

e = np.random.normal(0, 1, N)
theta = 0.5

for i in range(q, N):
    sum = 0
    for j in range(0, q):
        sum += theta**j * e[i - j]
        
    ma[i] = sum

ts2 = ts + ma

    
fig, axs = plt.subplots(1)
axs.plot(t, ts2)
axs.set_title('Moving Average')

pdf.append(fig)
fig.savefig("p01c.png")




for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()