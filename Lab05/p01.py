import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import csv
from datetime import datetime

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
signal = np.array([x['count'] for x in train_data.values()])
print(signal)

fft_signal = np.fft.fft(signal)
t = fs * np.linspace(0, len(signal)//2, len(signal)//2) / len(signal)

fig, axs = plt.subplots()
axs.plot(t, abs(fft_signal/len(signal))[:len(signal)//2])

pdf.append(fig)
fig.savefig('p01_d.png')

# e)


for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()