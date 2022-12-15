

file = open("data_rucksack.dat", "r")
Lines = file.readlines()
file.close()

## Part 1: 

shared_item = ["" for _ in range(len(Lines))]

for i, line in enumerate(Lines):
    n = len(line)-1
    pocket_1 = set(line[:-1][:n//2])
    pocket_2 = set(line[:-1][n//2:])
    shared_item[i] = [ char for char in pocket_1 & pocket_2][0]

# To access the priority we use the ord() function, which returns the Unicode identifier
# Now, we need a conversion
# The problem states that a, b, ...z, A, ..., Z = 1, 2, ..., 26, 27, ..., 52
# However the ord function returns a, b, ...z, A, ..., Z = 97, 98, 122, 65, ..., 90

def priority(char):

    return (ord(char) - 96) if ord(char) > 96 else ord(char) - 38

priority_sums = 0

for char in shared_item:
    priority_sums += priority(char)

print(f"The priorities of the shared items in the two pockets of each rucksack add up to {priority_sums}")

## Part 2:

badges = ["" for _ in range(len(Lines)//3)]

for i, (elf_1, elf_2, elf_3) in enumerate(zip(Lines[::3], Lines[1::3], Lines[2::3])):

    sack_1 = set(elf_1[:-1])
    sack_2 = set(elf_2[:-1])
    sack_3 = set(elf_3[:-1])

    badges[i] = [char for char in sack_1 & sack_2 & sack_3][0]

priority_badges = 0

for badge in badges:
    priority_badges += priority(badge)
    
print(f"The priorities of the badges add up to {priority_badges}")
