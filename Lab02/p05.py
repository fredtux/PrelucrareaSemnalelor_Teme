import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import sounddevice as sd

rate = int(10e5)
fs = 44100

t = np.linspace(0, 2, 2*fs)
c = 10000 * np.mod(t, 1.0/400) 
wavfile.write('p05.1.wav', rate, c)

sd.wait()

r,x = wavfile.read('p05.1.wav')
sd.play(x, fs)
sd.wait()


c = 10000 * np.mod(t, 1.0/1600) 
wavfile.write('p05.2.wav', rate, c)

sd.wait()

r,x = wavfile.read('p05.2.wav')
sd.play(x, fs)
sd.wait()

# Sunetul cu frecventa mai ridicata este mai inalt