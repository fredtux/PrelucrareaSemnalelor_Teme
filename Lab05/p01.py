import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import csv
from datetime import datetime
from scipy import signal

pdf = []
pdfDoc = PdfPages('p01.pdf')

train_data = {}

with open("Train.csv") as train_csv:
    train_reader = csv.DictReader(train_csv, delimiter=',')
    
    for row in train_reader:
        train_data[int(row['ID'])] = {'datetime': datetime.strptime(row['Datetime'], "%d-%m-%Y %H:%M"), 'count': int(row['Count'])}
        

# a) Frecventa este de 0.000277777777777777 Hz, adica 1 esantion pe ora
fs = 1/(60*60)
print(fs)

# b) 18288 ore | 762.0 zile | 25.4 luni intre 25-08-2012 00:00 si 25-09-2014 23:00
print(f"{len(train_data)} ore | {len(train_data) / 24} zile | {len(train_data) / 24 / 30} luni")

# c) 0.0001388888888888889 Hz , adica 1/2 din cea de esantionare din cauza Nyquist
f_max = fs / 2
print(f_max)

# d)
r_signal = np.array([x['count'] for x in train_data.values()])
# print(r_signal)

fft_r_signal = np.fft.fft(r_signal)
t = fs * np.linspace(0, len(r_signal)//2, len(r_signal)//2) / len(r_signal)

fig, axs = plt.subplots()
axs.plot(t, abs(fft_r_signal/len(r_signal))[:len(r_signal)//2])

pdf.append(fig)
fig.savefig('p01_d.png')

# e) Da, contine deoarece sunt peakuri pe FFT
fft_filtered_signal = fft_r_signal.copy()

# Scot cele mai mari 2 peakuri
for _ in range(2):
    i_peak = np.argmax(np.abs(fft_filtered_signal))
    # print(f"ip: {i_peak}")
    # print(f"max: {fft_filtered_signal[i_peak]}")
    fft_filtered_signal[i_peak] = 0

fig, axs = plt.subplots()
axs.plot(t, abs(fft_filtered_signal/len(fft_filtered_signal))[:len(fft_filtered_signal)//2])

pdf.append(fig)
fig.savefig('p01_e.png')


# f)
fft_r_signal_abs = abs(fft_r_signal/len(r_signal))[:len(r_signal)//2]
fft_r_signal_abs[::-1].sort()
mc4 = fft_r_signal_abs[:4]
print(mc4)
# Primele 4 cele mai mari valori: [138.95811461  66.85385766  35.21917298  27.10202229]

fft_r_signal_abs = abs(fft_r_signal/len(r_signal))
sz = len(fft_r_signal_abs)
indexes = []
for i in mc4:
    indexes.append(np.where(fft_r_signal_abs == i)[0][0])
print(indexes)

freqs = np.fft.fftfreq(sz, fs)
# print(f"freqs: {freqs}")
freq_indexes = [freqs[x] for x in indexes]
print([str(x) + " Hz" for x in freq_indexes])
# Frecventele in Hz corespunzatoare: ['0.0 Hz', '0.19685039370078738 Hz', '0.39370078740157477 Hz', '150.0 Hz']

# Se asociaza: prima este o componenta continua, a doua unei scaderi, a treia unei cresteri si a patra inaintea unei cresteri bruste urmata de o scadere brusca

# g)
start_date = 0
for v in train_data.items():
    if v[1]['datetime'].weekday() == 0:
        # print(v[1]['datetime'])
        start_date = v[1]['datetime']
        break

start_date = v[1]['datetime']
end_date = start_date.replace(month=start_date.month+1)
print(start_date, end_date)

# Incepe din prima zi de luni si are 18240 de esantioane
new_train_data = [x[1]['count'] for x in train_data.items() if x[1]['datetime'] >= start_date]
print(len(new_train_data))
        
# Iau prima luna (corespunde cu prima luna si din noul esantion) - 744 sampleuri pentru ca are 31 zile * 24 sampleuri/zi
sample_month = [x[1]['count'] for x in train_data.items() if x[1]['datetime'] >= start_date and x[1]['datetime'] < end_date]
print(len(sample_month))

fig, axs = plt.subplots()
axs.plot(sample_month)
pdf.append(fig)
fig.savefig('p01_g.png')

# h) Daca este 1, de obicei are un peak. De asemenea, schimbarile sunt mai putin intense vinerea si sambata. Nu putem prezice cu exactitate ziua deoarece exista intotdeauna peakuri si nu stim exact cand se vor produce acestea.

# i) Aleg orice frecventa peste 149 Hz deoarece avem cel putin un peak peste aceasta frecventa conform punctului f)
nyquist = (1/fs) / 2
cutoff = 149
ncutoff = cutoff / nyquist

# high pass filter
b, a = signal.butter(5, ncutoff, 'high', analog=False)
r_signal_processed = signal.filtfilt(b, a, r_signal)

fft_r_signal_processed = np.fft.fft(r_signal_processed)
t = fs * np.linspace(0, len(r_signal_processed)//2, len(r_signal_processed)//2) / len(r_signal_processed)

fig, axs = plt.subplots()
axs.plot(t, abs(fft_r_signal_processed/len(r_signal))[:len(r_signal)//2])

pdf.append(fig)
fig.savefig('p01_i.png')

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()