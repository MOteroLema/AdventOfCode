import numpy as np

class Register():

    def __init__(self):

        self.X = 1
        self.cycles = []

    def noop(self):
        self.cycles.append(self.X)

    def addx(self, x):

        self.cycles.append(self.X)
        self.cycles.append(self.X)
        self.X += x
    

with open('data_cathodic_ray_tube.dat', 'r') as file:
    Lines = np.array(file.readlines())
for i, line in enumerate(Lines):
    Lines[i] = line.replace("\n", "")

reg = Register()

for line in Lines:

    l = line.split(" ")

    if l[0] == "noop":
        reg.noop()
    elif l[0] == "addx":
        reg.addx(int(l[-1]))


addition = 0
interesting_cycles = set([20 + 40 * k for k in range(6)])

for i, X in enumerate(reg.cycles):

    cycle = i + 1
    power = cycle * X

    if cycle in interesting_cycles:
        addition += power

print(f"The total strength in the interesting cycles is {addition}")



######################################
############  Part 2 #################
######################################


drawing = []

for i, X in enumerate(reg.cycles):

    row = i%40

    if X == row or X == row + 1 or X == row - 1:

        drawing.append("#")

    else:

        drawing.append(".")

drawing = np.array(drawing)
drawing = drawing.reshape((6, 40))

np.savetxt("drawing.dat", drawing, fmt = "%s")






