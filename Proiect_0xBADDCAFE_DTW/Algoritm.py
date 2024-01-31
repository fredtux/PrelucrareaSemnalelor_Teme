import numpy as np
import matplotlib.pyplot as plt

def dist_eucl(S1, S2):
    eucl_matrix = np.zeros((len(S1), len(S2)))
    for i in range(len(S1)):
        for j in range(len(S2)):
            eucl_matrix[i][j] = (i-j) ** 2 + (S1[i]-S2[j])**2
    return eucl_matrix

def DTW(S1, S2):        #s1 si s2 sunt serii de timp
    dtw_matrix = np.zeros((len(S1), len(S2)))
    dtw_matrix[0,0] = abs(S1[0]-S2[0])
    
    for i in range(1, len(S1)):
        dtw_matrix[i][0] = abs(S1[i]-S2[0]) + dtw_matrix[i-1][0]
        
    for j in range(1, len(S2)):
        dtw_matrix[0][j] = abs(S1[0]-S2[j]) + dtw_matrix[0][j-1]
    
    for i in range(1, len(S1)):
        for j in range(1, len(S2)):
            dtw_matrix[i][j] = abs(S1[i]-S2[j]) + min(dtw_matrix[i][j-1], dtw_matrix[i-1][j-1], dtw_matrix[i-1][j])
            
    i = len(S1)-1
    j = len(S2)-1
    
    potriviri = []
    
    while i > 0 or j > 0:
        potriviri.append((i, j))
        prev = min(dtw_matrix[i][j-1], dtw_matrix[i-1][j-1], dtw_matrix[i-1][j])
        if prev == dtw_matrix[i][j-1]:
            j = j - 1
        elif prev == dtw_matrix[i-1][j-1]:
            i = i - 1
            j = j - 1
        else:
            i = i - 1
            
    potriviri.append((0, 0))
    potriviri.reverse()
    
    distanta = dtw_matrix[len(S1)-1][len(S2)-1]
    
    return[distanta, potriviri]

def DTW_Window(S1, S2, window_size_function):        #s1 si s2 sunt serii de timp
    window_size = window_size_function(len(S1), len(S2))
    dtw_matrix = np.zeros((len(S1), len(S2)))
    dtw_matrix[0][0] = abs(S1[0]-S2[0])
    
    for i in range(1, len(S1)):
        dtw_matrix[i][0] = abs(S1[i]-S2[0]) + dtw_matrix[i-1][0]
        
    for j in range(1, len(S2)):
        dtw_matrix[0][j] = abs(S1[0]-S2[j]) + dtw_matrix[0][j-1]
    
    for i in range(1, len(S1)):
        for j in range(max(1, i-window_size), min(len(S2), i+window_size)):
            dtw_matrix[i][j] = abs(S1[i]-S2[j]) + min(dtw_matrix[i][j-1], dtw_matrix[i-1][j-1], dtw_matrix[i-1][j])
            
    i = len(S1)-1
    j = len(S2)-1
    potriviri = []
    while i > 0 and j > 0:
        potriviri.append((i, j))
        prev = min(dtw_matrix[i][j-1], dtw_matrix[i-1][j-1], dtw_matrix[i-1][j])
        if prev == dtw_matrix[i][j-1]:
            j = j - 1
        elif prev == dtw_matrix[i-1][j-1]:
            i = i - 1
            j = j - 1
        else:
            i = i - 1
    potriviri.append((0, 0))
    potriviri.reverse()

    distanta = dtw_matrix[len(S1)-1][len(S2)-1]

    return[distanta, potriviri]

time1 = np.linspace(start=0, stop=1, num=50)
time2 = time1[0:40]

s1 = np.sin(2*np.pi*800*time1 + np.pi/4)
s2 = 2 * np.sin(2*np.pi*800*time1)

distanta, potriviri = DTW(s1, s2)

for pot in potriviri:
    plt.plot([pot[0], pot[1]], [s1[pot[0]], s2[pot[1]]], ':k')

plt.plot(s1, color='blue', marker='o', markersize=10, linewidth=3)
plt.plot(s2, color='red', marker='o', markersize=10, linewidth=3)


plt.show()
print(f"Distanta: {distanta}")
print(f"Potriviri: {potriviri}")

window_size_function = lambda ls1, ls2: int(0.15 * max(ls1, ls2))
distanta_window, potriviri_window = DTW_Window(s1, s2, window_size_function)

for pot in potriviri_window:
    plt.plot([pot[0], pot[1]], [s1[pot[0]], s2[pot[1]]], ':k')
    
plt.plot(s1, color='blue', marker='o', markersize=10, linewidth=3)
plt.plot(s2, color='red', marker='o', markersize=10, linewidth=3)

plt.show()
print(f"Distanta (15%): {distanta_window}")
print(f"Potriviri: {potriviri_window}")

window_size_function = lambda ls1, ls2: int(1 * max(ls1, ls2))
distanta_window, potriviri_window = DTW_Window(s1, s2, window_size_function)

for pot in potriviri_window:
    plt.plot([pot[0], pot[1]], [s1[pot[0]], s2[pot[1]]], ':k')
    
plt.plot(s1, color='blue', marker='o', markersize=10, linewidth=3)
plt.plot(s2, color='red', marker='o', markersize=10, linewidth=3)

plt.show()
print(f"Distanta (100%): {distanta_window}")
print(f"Potriviri: {potriviri_window}")
