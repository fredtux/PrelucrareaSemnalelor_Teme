import numpy as np
from dtaidistance import dtw
from csv import reader
from matplotlib import pyplot as plt

file = 'cercetare/finance_company.csv'

data = reader(open(file, 'r'))

data = list(data)


data = np.array([[int(x) for x in row] for row in data])

labels = ['Income', 'Costs of Goods Sold', 'Gross Profit', 'Total Operating Expenses', 'EBIT']

distances = np.zeros((len(data), len(data)))
paths = []

for i in range(0, len(data)):
    for j in range(i + 1, len(data)):
        if i == j:
            continue
        
        distance, path = dtw.warping_paths(data[i], data[j])
        
        distances[i][j] = distance
        paths.append((i, j, path))
        
minimum_pairs = []
for i in range(0, len(distances)):
    for j in range(i + 1, len(distances)):
        if i == j:
            continue
        
        minimum_pairs.append((i, j, distances[i][j]))
        
minimum_pairs.sort(key=lambda x: x[2])

print("3 most similar:")

fig, ax = plt.subplots(3)

for i in range(0, 3):
    print(f"{i+1}: {labels[minimum_pairs[i][0]]} and {labels[minimum_pairs[i][1]]} with distance {minimum_pairs[i][2]}")
    
    ax[i].plot(data[minimum_pairs[i][0]], label=labels[minimum_pairs[i][0]], color='red')
    ax[i].plot(data[minimum_pairs[i][1]], label=labels[minimum_pairs[i][1]], color='blue')
    ax[i].legend()
    ax[i].set_title(f"{minimum_pairs[i][2]}")
    
plt.show()