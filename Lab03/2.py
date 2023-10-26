import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.axis import Axis

# def fourier_matrix(N):
#     dft = []
#     for row in range(N):
#         dft.append([])
        
#         for k in range(N):
#             dft[row].append(np.exp(-2j * np.pi * k  * row/ N))
    
#     return dft


def colorize_axis(y):
    colors = []
    
    for z in y:
        distance = int(np.sqrt(np.real(z)**2 + np.imag(z)**2) * N)
        
        red = distance // 256
        hex_red = hex(red)[2:]
        if len(hex_red) == 1:
            hex_red = "0" + hex_red
            
        blue = np.mod(distance, 256)
        hex_blue = hex(blue)[2:]
        if len(hex_blue) == 1:
            hex_blue = "0" + hex_blue
        
        colors.append(f"#{hex_red}00{hex_blue}")
    
    return colors
    

pdf = []
pdfDoc = PdfPages('p02.pdf')

N = 1000
t = np.linspace(0, 1, N)
signal = np.sin(2 * np.pi * 10 * t)

f_y = np.zeros(N, dtype=complex)
for i in range(N):
    f_y[i] = signal[i] * np.exp(-2j * np.pi * i / N)
    
fig, axs = plt.subplots(2)

fig.canvas.draw()
axs[0].plot(t, signal)
axs[1].grid()

# colors = colorize_axis(f_y)
data = {
    "x": np.real(f_y),
    "y": np.imag(f_y),
    "color": colorize_axis(f_y)
}

axs[1].scatter('x', 'y', color='color', data=data)

pdf.append(fig)
fig.savefig('p02.01.png')

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()