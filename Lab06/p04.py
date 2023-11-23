import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import csv
from datetime import datetime
from scipy import signal

pdf = []
pdfDoc = PdfPages('p04.pdf')


train_data = {}

with open("Train.csv") as train_csv:
    train_reader = csv.DictReader(train_csv, delimiter=',')
    
    for row in train_reader:
        train_data[int(row['ID'])] = {'datetime': datetime.strptime(row['Datetime'], "%d-%m-%Y %H:%M"), 'count': int(row['Count'])}
        
# a)
start_date = train_data[0]['datetime']
end_date = start_date.replace(day=start_date.day+3)
end_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0)

x = []
for i in range(0, len(train_data)):
    if train_data[i]['datetime'] >= end_date:
        break
    x.append(train_data[i]['count'])
    
# print(len(x))

# b)
ws = [5, 9, 13, 17]

fig, axs = plt.subplots(len(ws) + 1)
axs[0].plot(x)

for w in ws:
    to_plot = np.convolve(x, np.ones(w), 'valid') / w
    axs[1 + ws.index(w)].plot(to_plot)

pdf.append(fig)
fig.savefig("p04.b.png")

# c)
f = 60 * 60
nyquist = f * 2
cutoff = 2000 # Trial and error
ncutoff = cutoff / nyquist


# d) & e)
fig, axs = plt.subplots(3)

axs[0].plot(x)

b, a = signal.butter(5, ncutoff, 'low', analog=False)
x_processed = signal.filtfilt(b, a, x)
axs[1].plot(x_processed)

b, a = signal.cheby1(5, 5, ncutoff, 'low', analog=False)
x_processed = signal.filtfilt(b, a, x)
axs[2].plot(x_processed) 

pdf.append(fig)
fig.savefig("p04.e.png")

# Aleg Butterworth pentru ca este mai aproape de semnalul original

# f)
ords = [1, 5, 10]
rps = [5, 10, 15]

fig, axs = plt.subplots(len(ords) * 2)

for ord in ords:
    b, a = signal.butter(ord, ncutoff, 'low', analog=False)
    x_processed = signal.filtfilt(b, a, x)
    axs[ords.index(ord) * 2].plot(x_processed)
    
    b, a = signal.cheby1(ord, 5, ncutoff, 'low', analog=False)
    x_processed = signal.filtfilt(b, a, x)
    axs[ords.index(ord) * 2 + 1].plot(x_processed)
    
pdf.append(fig)
fig.savefig("p04.f.1.png")

fig, axs = plt.subplots(len(rps))

for rp in rps:    
    b, a = signal.cheby1(5, rp, ncutoff, 'low', analog=False)
    x_processed = signal.filtfilt(b, a, x)
    axs[rps.index(rp)].plot(x_processed)
    
pdf.append(fig)
fig.savefig("p04.f.2.png")

for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()