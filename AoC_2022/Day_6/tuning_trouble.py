import numpy as np

with open('data_tuning.dat', 'r') as file:
    input = file.readlines()[0]

list = np.array([char for char in input])

for i in range(len(list)-4):

    subset = list[i:i+4]

    if len(np.unique(subset)) == 4:

        break

character = i + 4

print(f"First marker after character {character}")

for i in range(len(list)-14):

    subset = list[i:i+14]

    if len(np.unique(subset)) == 14:

        break

character = i + 14

print(f"First message marker after character {character}")