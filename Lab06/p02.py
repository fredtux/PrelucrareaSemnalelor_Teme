import numpy as np
import matplotlib.pyplot as plt

N = 5

p = np.random.randn(N)
q = np.random.randn(N)

debug_mul = np.convolve(p,q)
print(f"Debug: {debug_mul}")

# Inmultirea
mul = np.zeros(2*N - 1)
for i in range(len(p)):
    for j in range(len(q)):
        mul[i + j] += p[i] * q[j]
print(f"Inmultirea: {mul}")

# Convolutia cu fft
pfft = np.fft.fft(p)
qfft = np.fft.fft(q)

fft_conv = (np.fft.ifft(np.convolve(pfft,qfft)))
print(f"Convolutie FFT: {fft_conv}")

