
import numpy as np

### Part 1

file = open("data_part_1.dat", "r")
Lines = np.array(file.readlines())
file.close()


linebreak = np.where(Lines == "\n")[0]

intervals = np.zeros(len(linebreak)+2, dtype = int)
intervals[0] = -1
intervals[-1] = len(Lines)
intervals[1:-1] = linebreak

calories = np.zeros(len(intervals) -1)
for i in range(len(intervals)-1):

    elf_calories = np.array( [float(k) for k in Lines[intervals[i]+1:intervals[i+1]]])
    calories[i] = np.sum(elf_calories)

max_cal = np.max(calories)
print(f"The elf with the most food carries {max_cal} calories")

### Part 2

sorted_cals = np.flip(np.sort(calories))

total_cal_three = np.sum(sorted_cals[:3])

print(f"The three elfs with the most food carry {total_cal_three} calories")
