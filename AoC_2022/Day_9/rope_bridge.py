import numpy as np


        
class Rope():

    def __init__(self, n_knots):

        self.knots = [ np.zeros(2) for _ in range(n_knots) ]  ## First knot is the head, last is the tail
        self._x = np.array([1, 0])
        self._y = np.array([0, 1])

    
    def _update_knot(self, i):

        h = self.knots[i - 1]
        t = self.knots[i]

        diff = h - t

        if np.any( h == t ):

            self.knots[i] += diff /2 
        
        else:

            self.knots[i] += np.sign(diff)

    def movement(self, head_movement):

        self.knots[0] += head_movement

        for i in range(1, len(self.knots)):

            if np.linalg.norm(self.knots[i - 1] - self.knots[i]) > np.sqrt(2):

                self._update_knot(i)



key = {"R": np.array([1, 0]), "L": np.array([-1, 0]), "U": np.array([0, 1]), "D": np.array([0, -1])}


with open('data_rope_bridge.dat', 'r') as file:
    Lines = np.array(file.readlines())
for i, line in enumerate(Lines):
    Lines[i] = line.replace("\n", "")

instructions = []

for i, line in enumerate(Lines):

    direction, num = line.split(" ")
    num = int(num)
    instructions.append([direction, num])


rope = Rope(2)
unique_spots = set()
unique_spots.add(tuple(rope.knots[-1]))

for i, command in enumerate(instructions):

    direction, num = command

    for _ in range(num):
        rope.movement(key[direction])
        unique_spots.add(tuple(rope.knots[-1]))

print(f"The number of unique positions visited by the tail of the 2-knot rope is {len(unique_spots)}")

#########
# PART 2
#########


rope = Rope(10)
unique_spots = set()
unique_spots.add(tuple(rope.knots[-1]))

for i, command in enumerate(instructions):

    direction, num = command

    for _ in range(num):
        rope.movement(key[direction])
        unique_spots.add(tuple(rope.knots[-1]))

print(f"The number of unique positions visited by the tail of the 10-knot rope is {len(unique_spots)}")


        