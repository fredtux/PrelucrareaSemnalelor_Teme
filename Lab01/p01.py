import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages


def x(t):
    return np.cos(520*np.pi*t + np.pi/3)


def y(t):
    return np.cos(280*np.pi*t-np.pi/3)

def z(t):
    return np.cos(120*np.pi*t+np.pi/3)


pdf = []
pdfDoc = PdfPages('p01.pdf')


# a)
t = np.arange(0, 0.03, 0.0005)

# b)
resx, resy, resz = x(t), y(t), z(t)
fig, axs = plt.subplots(3)
fig.suptitle("b)")
axs[0].plot(t, resx)
axs[1].plot(t, resy)
axs[2].plot(t, resz)
pdf.append(fig)

# c)
fig, axs = plt.subplots(3)
fig.suptitle("c)")

t = np.arange(0, 0.03, 0.03 * 1.0/200)

resx = x(t)
axs[0].plot(t, resx)

resy = y(t)
axs[1].plot(t, resy)

resz = z(t)
axs[2].plot(t, resz)

pdf.append(fig)


for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()
