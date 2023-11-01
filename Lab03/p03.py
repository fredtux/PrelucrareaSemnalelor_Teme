import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import cv2

def colorize_graphic(y):
    colors = []
    
    for z in y:
        distance = np.sqrt(np.real(z)**2 + np.imag(z)**2) 

        h = 1 # Hue
        s = 255 # Full saturation
        v = 255 - int(distance * 60) # Luminosity
        hsv = np.uint8([[[h, s, v]]])
        rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
        hex_red = hex(rgb[0][0][0])[2:] if len(hex(rgb[0][0][0])[2:]) == 2 else f"0{hex(rgb[0][0][0])[2:]}"
        hex_green = hex(rgb[0][0][1])[2:] if len(hex(rgb[0][0][1])[2:]) == 2 else f"0{hex(rgb[0][0][1])[2:]}"
        hex_blue = hex(rgb[0][0][2])[2:] if len(hex(rgb[0][0][2])[2:]) == 2 else f"0{hex(rgb[0][0][2])[2:]}"
        
        colors.append(f"#{hex_red}{hex_green}{hex_blue}")
    
    return colors

pdf = []
pdfDoc = PdfPages('p03.pdf')

N = 100
t = np.linspace(0, 1, N)
signal = 3 * np.sin(2 * np.pi * 2 * t) + 0.9 * np.sin(2 * np.pi * 5 * t) + 1.1 * np.sin(2 * np.pi * 3 * t)

omega = [2, 5, 3]

fig, axs = plt.subplots(2)
axs[0].plot(t, signal)

f_signal = np.zeros(N, dtype=complex)
for i in range(N):
    f_signal[i] = signal[i] * np.exp(-2j * np.pi * i / N)
    
axs[1].stem(t, np.abs(f_signal))

pdf.append(fig)
fig.savefig('p03.01.png')

fig, axs = plt.subplots(len(omega))

for omega_i in range(len(omega)):
    f_z = np.zeros(N, dtype=complex)
    for i in range(N):
        f_z[i] = signal[i] * np.exp(-2j * np.pi * i * omega[omega_i] / N)
        
    # colors = colorize_graphic(f_z)
        
    axs[omega_i].grid()
    axs[omega_i].set_title(f"Omega = {omega[omega_i]}")
    # for k in range(N):
    #     axs[omega_i].scatter(f_z[k].real, f_z[k].imag, c=colors[k])
    
    axs[omega_i].plot(f_z.real, f_z.imag)

pdf.append(fig)
fig.savefig('p03.02.png')


for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()