import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p02.pdf')

# a)
t = np.linspace(0, 0.02, 1600)
a = np.sin(2*np.pi*400*t)

fig, axs = plt.subplots()
axs.plot(t, a)
fig.suptitle("a)")
pdf.append(fig)

# b)
t = np.linspace(0, 3, 800)
b = np.sin(2*np.pi*800*t)

fig, axs = plt.subplots()
fig.suptitle("b)")
axs.plot(t, b)
pdf.append(fig)

# c)
t = np.linspace(0, 0.03, 960)
c = np.mod(t, 1.0/240) 

fig, axs = plt.subplots()
fig.suptitle("c)")

axs.plot(t, c)
pdf.append(fig)


# d)
dfreq = 300
dsampling = 600
dmax = 0.02
dmin = 0

t = np.linspace(dmin, dmax, dsampling)
d = np.zeros(len(t))
for i in range(len(t)):
    sin_val = np.sin(2*np.pi*dfreq*t[i])
    if sin_val == 0:
        d[i] = np.sign(np.sin(2*np.pi*dfreq*(t[i] + (dmax - dmin)/dsampling)))
    else:
        d[i] = np.sign(sin_val)

fig, axs = plt.subplots()
fig.suptitle("d)")

axs.plot(t, d)
pdf.append(fig)

# e)
t = np.random.rand(128, 128)

fig, axs = plt.subplots()
fig.suptitle("e)")

axs.imshow(t)
pdf.append(fig)


# f)
t = np.zeros((128, 128))

def f(t):
    for x in range(128):
        for y in range(128):
            if (x + y) % 2 == 0:
                t[x][y] = np.sin(x + y) * np.cos(x - y)
    return t

t = f(t)

fig, axs = plt.subplots()
fig.suptitle("f)")

axs.imshow(t)
pdf.append(fig)


for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()