import numpy as np

data = np.loadtxt("data_rock_paper_scissors.dat", dtype = "str")

## We will exploit the fact that the rock paper scissors game encodes a three-state system with a three-state outcome
## If 0, 1, 2 = rock, paper, scissors, then operations between each number (mod 3) always yield 0, 1 or 2
## The result of that difference can then encode the three different outcomes (win, lose, draw)



## Part 1 

# O = rock, 1 = paper, 2 = scissors for both the elf and the player
# We also encode 0, 1, 2 = lose, draw, win. This is so score = 3 * outcome
# Then we exploit the fact that (player - elf + 1)%3 = outcome
# For example:
# Elf plays paper (1) and we play rock (0). Then (0 - 1 + 1)%3 = 0 and we lost (0)
# Elf plays scissors (2) and we play rock (0). Then (0 - 2 + 1)%3 = 2 and we won (2)
# ...
# The score is then 3 * [(player - elf + 1)%3] + player + 1, since all shapes have point values equal to their code + 1

elf_key = {"A": 0, "B": 1, "C": 2}
player_key = {"X": 0, "Y": 1, "Z": 2}

def game_outcome(player, elf):
    return ((player - elf +1)%3)  

total_score = 0
for game in data:
    k_elf, k_player = game
    elf, player = elf_key[k_elf], player_key[k_player]
    total_score += 3 * game_outcome(player, elf) + player + 1

print(f"The total score is {total_score} points")

## Part 2

# The elf key is the same, but now the have elf and outcome as the inputs, and we need to calculate the player
# If we perform the operation (elf + outcome - 1)%3 we arrive to the shape played by the player
# For example:
# Elf plays rock (0) and we draw (1). Then (0 + 1 - 1)%3 = 0, and thus the player played rock (0)
# Elf plays scissors (2) and we win (2). Then (2 + 2 - 1)%3 = 1, and thus the player played rock (0)
# Elf plays scissors (2) and we lose (0). Then (2 + 0 - 1)%3 = 1, and thus the player played paper (1) 
# ...
# The score is then 3 * outcome + player + 1 = 3 * outcome + (elf + outcome - 1)%3 + 1

def player_play(elf, outcome):
    return (elf + outcome - 1)%3

total_score = 0
for game in data:
    k_elf, k_outcome = game
    elf, outcome = elf_key[k_elf], player_key[k_outcome]
    total_score += 3 * outcome + player_play(elf, outcome) + 1

print(f"The total score with the new key is {total_score} points")