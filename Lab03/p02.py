import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import cv2

def colorize_graphic(y):
    colors = []
    
    for z in y:
        distance = np.sqrt(np.real(z)**2 + np.imag(z)**2) 

        h = 100 # Hue
        s = 255 # Full saturation
        v = 255 - int(distance * 255) # Luminosity
        hsv = np.uint8([[[h, s, v]]])
        rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
        hex_red = hex(rgb[0][0][0])[2:] if len(hex(rgb[0][0][0])[2:]) == 2 else f"0{hex(rgb[0][0][0])[2:]}"
        hex_green = hex(rgb[0][0][1])[2:] if len(hex(rgb[0][0][1])[2:]) == 2 else f"0{hex(rgb[0][0][1])[2:]}"
        hex_blue = hex(rgb[0][0][2])[2:] if len(hex(rgb[0][0][2])[2:]) == 2 else f"0{hex(rgb[0][0][2])[2:]}"
        
        colors.append(f"#{hex_red}{hex_green}{hex_blue}")
    
    return colors
    

pdf = []
pdfDoc = PdfPages('p02.pdf')

N = 1000
t = np.linspace(0, 1, N)
signal = np.sin(2 * np.pi * 10 * t)

# a)
f_y = np.zeros(N, dtype=complex)
for i in range(N):
    f_y[i] = signal[i] * np.exp(-2j * np.pi * i / N)
    
fig, axs = plt.subplots(2)

fig.canvas.draw()
axs[0].plot(t, signal)
axs[1].grid()

colors = colorize_graphic(f_y)

for i in range(N):
    axs[1].scatter(f_y[i].real, f_y[i].imag, c=colors[i])

pdf.append(fig)
fig.savefig('p02.01.png')

# b)
omega = [1, 2, 7, 10]

fig, axs = plt.subplots(len(omega))

for i in range(len(omega)):
    f_z = np.zeros(N, dtype=complex)
    for j in range(N):
        f_z[j] = signal[j] * np.exp(-2j * np.pi * j * omega[i] / N)
    
    colors = colorize_graphic(f_z)
    
    axs[i].grid()
    axs[i].set_title(f"Omega = {omega[i]}")
    for k in range(N):
        axs[i].scatter(f_z[k].real, f_z[k].imag, c=colors[k])
    
pdf.append(fig)
fig.savefig('p02.02.png')

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()