import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pdf = []
pdfDoc = PdfPages('p01.pdf')

N = 1000

# a) unidimensionala
mu = 0 
sigma = 1
x = np.linspace(mu - 5 * sigma, mu + 5 * sigma, N)
y = (1/ np.sqrt(2*np.pi*(sigma**2))) * np.exp(-1/2 * (x - mu)**2/sigma**2)

fig, axs = plt.subplots()
axs.plot(x, y)
axs.set_title('Unidemensionala')

fig.savefig("p01_a.png")
pdf.append(fig)




for page in pdf:
    pdfDoc.savefig(page)
pdfDoc.close()