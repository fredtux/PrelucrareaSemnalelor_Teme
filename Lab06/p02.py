import numpy as np

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
pfft = np.fft.fft(p, 2*N - 1)
qfft = np.fft.fft(q, 2*N - 1)

fft_conv = np.real(np.fft.ifft(pfft * qfft))
print(f"Convolutie FFT: {fft_conv}")

