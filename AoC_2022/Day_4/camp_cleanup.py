import numpy as np


data = np.loadtxt("data_camp_cleanup.dat", delimiter = ",", dtype = "str")
first_elf = np.array([[int(s) for s in d[0].split("-")] for d in data])
second_elf = np.array([[int(s) for s in d[1].split("-")] for d in data])


def contained(elf_1, elf_2):

    start_1, finish_1 = elf_1
    finish_1 += 1

    start_2, finish_2 = elf_2
    finish_2 += 1

    set_1 = set(np.arange(start_1, finish_1))
    set_2 = set(np.arange(start_2, finish_2))

    union = set_1.union(set_2)

    return int(set_1.issubset(set_2) or set_2.issubset(set_1))

contained_count = 0

for e1 ,e2 in zip(first_elf, second_elf):

    contained_count += contained(e1, e2)

print(f"The number of assigments in which one contains the other is {contained_count}")

################################################################################
################################################################################
################################################################################

def overlap(elf_1, elf_2):

    start_1, finish_1 = elf_1
    finish_1 += 1

    start_2, finish_2 = elf_2
    finish_2 += 1

    set_1 = set(np.arange(start_1, finish_1))
    set_2 = set(np.arange(start_2, finish_2))

    intersection = set_1 & set_2
    empy_set = set()
    
    return (1 - intersection.issubset(empy_set))

overlap_count = 0

for e1 ,e2 in zip(first_elf, second_elf):

    overlap_count += overlap(e1, e2)

print(f"The number of assigments that overlap is {overlap_count}")