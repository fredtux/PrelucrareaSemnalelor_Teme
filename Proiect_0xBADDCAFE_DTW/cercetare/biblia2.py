import numpy as np
from fastdtw import fastdtw
from matplotlib import pyplot as plt
# from dtaidistance import dtw, ed
from pyts.metrics import dtw as pyts_dtw
import sqlite3

file_bible_romanian = 'cercetare/datasets/bible/cornilescu.sqlite'
file_bible_english = 'cercetare/datasets/bible/kjv.sqlite'
file_bible_luther = 'cercetare/datasets/bible/luther.sqlite'

bible_romanian = sqlite3.connect(file_bible_romanian)
bible_english = sqlite3.connect(file_bible_english)
bible_luther = sqlite3.connect(file_bible_luther)
    
total_god_english = []
total_god_romanian = []
total_god_luther = []

chapters_romanian = {}
chapters_english = {}
chapters_luther = {}


cursor = bible_romanian.cursor()
cursor.execute("SELECT book, chapter, text FROM verses WHERE text LIKE '%dumnezeu%'")
rows = cursor.fetchall()


for row in rows:
    if f"{row[0]}_{row[1]}" not in chapters_romanian:
        chapters_romanian[f"{row[0]}_{row[1]}"] = 0
        
    chapters_romanian[f"{row[0]}_{row[1]}"] += row[2].count('Dumnezeu')
    
total_god_romanian = list(chapters_romanian.values())
bible_romanian.close()

cursor = bible_english.cursor()
cursor.execute("SELECT book, chapter, text FROM verses WHERE text LIKE '%god%'")
rows = cursor.fetchall()


for row in rows:
    if f"{row[0]}_{row[1]}" not in chapters_english:
        chapters_english[f"{row[0]}_{row[1]}"] = 0
        
    chapters_english[f"{row[0]}_{row[1]}"] += row[2].count('God')
    
total_god_english = list(chapters_english.values())
bible_english.close()

cursor = bible_luther.cursor()
cursor.execute("SELECT book, chapter, text FROM verses WHERE text LIKE '%gott%'")
rows = cursor.fetchall()


for row in rows:
    if f"{row[0]}_{row[1]}" not in chapters_luther:
        chapters_luther[f"{row[0]}_{row[1]}"] = 0
        
    chapters_luther[f"{row[0]}_{row[1]}"] += row[2].count('Gott')
    
total_god_luther = list(chapters_luther.values())
bible_luther.close()

    
total_god_english = np.array(total_god_english)
total_god_romanian = np.array(total_god_romanian)
total_god_luther = np.array(total_god_luther)


print('English: ', total_god_english.sum())
print('Romanian: ', total_god_romanian.sum())
print('Luther: ', total_god_luther.sum())

# DTW on the two time series

distance = pyts_dtw(total_god_english, total_god_romanian)

fig, ax = plt.subplots()
ax.plot(total_god_english, label='English', color='blue')
ax.plot(total_god_romanian, label='Romanian', color='red')
ax.legend()
plt.show()

print(f"DTW distance between english and romanian: {distance}")

# Plot dtw path
# fig, ax = plt.subplots(figsize=(16, 12))

# # Remove the border and axes ticks
# fig.patch.set_visible(False)
# ax.axis('off')

# for [map_x, map_y] in warp_path:
#     ax.plot([map_x, map_y], [total_god_english[map_x], total_god_romanian[map_y]], '-k')

# ax.plot(total_god_english, color='blue')
# ax.plot(total_god_romanian, color='red')
# ax.tick_params(axis="both", which="major", labelsize=18)

# plt.show()

# DTW on the two time series

distance = pyts_dtw(total_god_luther, total_god_romanian)

# fig, ax = plt.subplots()
# ax.plot(total_god_english, label='English')
# ax.plot(total_god_romanian, label='Romanian')
# ax.legend()
# plt.show()

print(f"DTW distance between luther and romanian: {distance}")

fig, ax = plt.subplots()
ax.plot(total_god_luther, label='Luther', color='blue')
ax.plot(total_god_romanian, label='Romanian', color='red')
ax.legend()
plt.show()

# Plot dtw path
# fig, ax = plt.subplots(figsize=(16, 12))

# # Remove the border and axes ticks
# fig.patch.set_visible(False)
# ax.axis('off')

# for [map_x, map_y] in warp_path:
#     ax.plot([map_x, map_y], [total_god_luther[map_x], total_god_romanian[map_y]], '-k')

# ax.plot(total_god_luther, color='blue')
# ax.plot(total_god_romanian, color='red')
# ax.tick_params(axis="both", which="major", labelsize=18)

# plt.show()

distance = pyts_dtw(total_god_luther, total_god_english)


print(f"DTW distance between luther and english: {distance}")

fig, ax = plt.subplots()
ax.plot(total_god_luther, label='Luther', color='blue')
ax.plot(total_god_romanian, label='English', color='red')
ax.legend()
plt.show()