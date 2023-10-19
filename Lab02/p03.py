import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from scipy.io import wavfile
import sounddevice as sd

rate = int(10e5)
fs = 44100

# a)
t = np.linspace(0, 2, 1600)
a = np.sin(2*np.pi*400*t)
wavfile.write('p03.a.wav', rate, a)

sd.wait()
r,x = wavfile.read('p03.a.wav')
print("Play a")
# sd.play(x, fs)
sd.wait()



# b)
t = np.linspace(0, 3, 3*fs)
b = np.sin(2*np.pi*800*t)
wavfile.write('p03.b.wav', rate, b)

sd.wait()

r,x = wavfile.read('p03.b.wav')
print("Play b")
# sd.play(x, fs)
sd.wait()



# c)
t = np.linspace(0, 2, 2*fs)
c = 10000 * np.mod(t, 1.0/240) 
wavfile.write('p03.c.wav', rate, c)

sd.wait()

r,x = wavfile.read('p03.c.wav')
print("Play c")
sd.play(x, fs)
sd.wait()




# d)
dfreq = 300
dsampling = 2*fs
dmax = 2
dmin = 0

t = np.linspace(dmin, dmax, dsampling)
d = np.zeros(len(t))
for i in range(len(t)):
    sin_val = np.sin(2*np.pi*dfreq*t[i])
    if sin_val == 0:
        d[i] = np.sign(np.sin(2*np.pi*dfreq*(t[i] + (dmax - dmin)/dsampling)))
    else:
        d[i] = np.sign(sin_val)

wavfile.write('p03.d.wav', rate, d)

sd.wait()

r,x = wavfile.read('p03.d.wav')
print("Play d")
# sd.play(x, fs)
sd.wait()
