import numpy as np
from dtaidistance import dtw
from csv import reader
from matplotlib import pyplot as plt

file = 'salarii_medii.csv'

data = reader(open(file, 'r'))
data = list(data)

countries = {}

for i in range(1, len(data)):
    if data[i][6] == 'EUR':
        if data[i][1] not in countries:
            countries[data[i][1]] = []
        countries[data[i][1]].append((int(data[i][5]), float(data[i][12])))
        
# Get minimum common year
min_year = 0
for country in countries:
    years = [x[0] for x in countries[country]]
    if min_year == 0:
        min_year = min(years)
    else:
        min_year = max(min(years), min_year)
        
# Get maximum common year
max_year = 0
for country in countries:
    years = [x[0] for x in countries[country]]
    if max_year == 0:
        max_year = max(years)
    else:
        max_year = min(max(years), max_year)
        
print(f"Comparing interval: {min_year} - {max_year}")

distances = np.zeros((len(countries), len(countries)))

for i in range(0, len(countries)):
    for j in range(i + 1, len(countries)):
        if i == j:
            continue
        
        # Get data for each country
        data_i = [x[1] for x in countries[list(countries.keys())[i]] if x[0] >= min_year and x[0] <= max_year]
        data_j = [x[1] for x in countries[list(countries.keys())[j]] if x[0] >= min_year and x[0] <= max_year]
        
        distance, path = dtw.warping_paths(data_i, data_j)
        
        distances[i][j] = distance
        
        
# Minimum 5 pairs
minimum_pairs = []

for i in range(0, len(distances)):
    for j in range(i + 1, len(distances)):
        if i == j:
            continue
        
        minimum_pairs.append((i, j, distances[i][j]))
        
minimum_pairs.sort(key=lambda x: x[2])

print("5 most similar:")

fig, ax = plt.subplots(5)

for i in range(0, 5):
    print(f"{i+1}: {list(countries.keys())[minimum_pairs[i][0]]} and {list(countries.keys())[minimum_pairs[i][1]]} with distance {minimum_pairs[i][2]}")
    
    ax[i].plot([x[1] for x in countries[list(countries.keys())[minimum_pairs[i][0]]] if x[0] >= min_year and x[0] <= max_year], label=list(countries.keys())[minimum_pairs[i][0]], color='red')
    ax[i].plot([x[1] for x in countries[list(countries.keys())[minimum_pairs[i][1]]] if x[0] >= min_year and x[0] <= max_year], label=list(countries.keys())[minimum_pairs[i][1]], color='blue')
    ax[i].legend()
    ax[i].set_title(f"{minimum_pairs[i][2]}")

plt.show()