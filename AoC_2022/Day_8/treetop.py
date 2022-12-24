import numpy as np



with open('data_treetop.dat', 'r') as file:
    lines_trees = file.readlines()
for i, line in enumerate(lines_trees):
    lines_trees[i] = line.replace("\n", "")

rows = len(lines_trees)
cols = len(lines_trees[0])

trees = np.zeros((rows, cols))

for i, line in enumerate(lines_trees):

    row = np.array([int(char) for char in line])
    trees[i, :] = row


visible_trees = 0


for i in range(rows):
        for j in range(cols):
            
            if j == 0 or j == cols - 1:

                visible_trees += 1

            elif i == 0 or i == rows -1:

                visible_trees += 1
            
            else:
                tree_size = trees[i, j]
                top = np.all( np.array([tree_size - size for size in trees[:i, j]]) > 0)
                bottom = np.all( np.array([tree_size - size for size in trees[i+1:, j]]) > 0)
                left = np.all( np.array([tree_size - size for size in trees[i, :j]]) > 0)
                right = np.all( np.array([tree_size - size for size in trees[i, j+1:]]) > 0)

                if (top or bottom or left or right):
                    
                    visible_trees += 1

print(f"There are {visible_trees} visible trees")


#####################
#####################
#####################


scenic_scores = np.zeros_like(trees)

def score(tree, vector):
    s = 1
    for v in vector[:-1]:
        if v < tree:
            s += 1
        if v >= tree:
            break
    return s


for i in range(rows):
    for j in range(cols):
        
        tree_size = trees[i, j]

        if i == 0 or i == rows - 1:
          
          pass
        
        elif j == 0 or j == cols -1:

            pass

        else:

            top = np.flip(trees[:i, j])
            bottom = trees[i+1:, j]
            left = np.flip(trees[i, :j])
            right = trees[i, j+1:]

            directions = [top, bottom, left, right]

            scores = np.array([score(tree_size, d) for d in directions])

            scenic_scores[i, j] = np.prod(scores)

print(f"The maximum scenic score is {np.max(scenic_scores)}")





