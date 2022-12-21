import numpy as np
import re

class CrateMover_9000():

    def __init__(self, piles):

        self.crates = {}
        for i, pile in enumerate(piles):

            self.crates[str(i+1)] = list(np.copy(pile))
    
    def move(self, how_many, origin, destination):

        for _ in range(how_many):

            item = self.crates[origin].pop(-1)
            self.crates[destination].append(item)

class CrateMover_9001():

    def __init__(self, piles):

        self.crates = {}
        for i, pile in enumerate(piles):

            self.crates[str(i+1)] = list(np.copy(pile))
    
    def move(self, how_many, origin, destination):

        items = np.flip([ self.crates[origin].pop(-1) for _ in range(how_many)])
        for item in items:
            self.crates[destination].append(item)

### Loading data

with open('data_crates.dat', 'r') as file:
    Lines = file.readlines()

Lines = np.array(Lines)
where_line_break = np.where(Lines == "\n")[0][0]

crate_structure = Lines[:where_line_break]
instructions = Lines[(1+where_line_break):]

for i, c in enumerate(crate_structure):
    crate_structure[i] = c.replace("\n", " ")

numbers = np.flip(crate_structure)[0].replace(" ", "")
n_piles = int(numbers[-1])
crate_structure = np.flip(crate_structure)[1:]

## The letters are located at postiions 1, 5, 9, ..., len(line) - 3

piles = [[] for _ in range(n_piles)]

for line in crate_structure:

    characters = [s for s in line[1::4]]

    for i, char in enumerate(characters):

        if char != " ":
            piles[i].append(char)

## Object initialization

crates_9000 = CrateMover_9000(piles)
crates_9001 = CrateMover_9001(piles)

str_how_many = r"move (\d+)"
str_origin = r"from (\d+)"
str_destination = r"to (\d+)"

how_many = re.compile(str_how_many)
origin = re.compile(str_origin)
destination = re.compile(str_destination)

for i in instructions:

    n, o, d = int(how_many.findall(i)[0]), origin.findall(i)[0], destination.findall(i)[0]
    crates_9000.move(n, o, d)

top = ""
for k in crates_9000.crates:
    top += crates_9000.crates[k][-1]

print(f"The top crates using CrateMover 9000 are {top}")



#### Second part of the problem

for i in instructions:

    n, o, d = int(how_many.findall(i)[0]), origin.findall(i)[0], destination.findall(i)[0]
    crates_9001.move(n, o, d)

top = ""
for k in crates_9001.crates:
    top += crates_9001.crates[k][-1]

print(f"The top crates using CrateMover 9001 are {top}")