import time
import psutil
import numpy as np
import re

start_time = time.time()

def visible_from_any_edge(TREE_X, TREE_Y, FOREST_LENGTH, FOREST_WIDTH):
    # Check if the tree is visible from the up, down, left, or right edges
    up = all(forest[:TREE_X, TREE_Y] < forest[TREE_X, TREE_Y])
    down  = all(forest[TREE_X+1:, TREE_Y] < forest[TREE_X, TREE_Y])
    left  = all(forest[TREE_X, :TREE_Y] < forest[TREE_X, TREE_Y])
    right  = all(forest[TREE_X, TREE_Y+1:] < forest[TREE_X, TREE_Y])
    return up or down or left or right

def scenic_score(TREE_X, TREE_Y, FOREST_LENGTH, FOREST_WIDTH):
    COUNTERS = np.zeros(4) # counter in 4 directions

    for i in reversed(range(TREE_X)): # up direction
        COUNTERS[0] += 1
        if forest[i,TREE_Y] >= forest[TREE_X,TREE_Y]:
            break
    for i in range(TREE_X+1,FOREST_LENGTH): # down direction
        COUNTERS[1] += 1
        if forest[i,TREE_Y] >= forest[TREE_X,TREE_Y]:
            break

    for j in reversed(range(TREE_Y)): # left direction
        COUNTERS[2] += 1
        if forest[TREE_X,j] >= forest[TREE_X,TREE_Y]:
            break
    for j in range(TREE_Y+1,FOREST_WIDTH): # right direction
        COUNTERS[3] += 1
        if forest[TREE_X,j] >= forest[TREE_X,TREE_Y]:
            break
    return np.prod(COUNTERS)

# Open the input.txt file
with open("input.txt") as f:
    # Read the contents of the file
    contents = f.read()

    # Use a regular expression to match each digit and add a space before it
    new_contents = re.sub(r"\d", r" \g<0>", contents)

    # Open the processed_input.txt file
    with open("processed_input.txt", "w") as outfile:
        # Write the new contents to the file
        outfile.write(new_contents)

# Import input.txt as a numpy array called "forest"
forest = np.loadtxt("processed_input.txt")
# Define FOREST_WIDTH and FOREST_LENGTH
FOREST_WIDTH = len(forest[0,:])
FOREST_LENGTH = len(forest[:,0])
# Compute the number of tree visible
visible_trees_counter = 0
scenic_score_matrix = np.zeros((FOREST_LENGTH,FOREST_WIDTH))

for i in range(FOREST_LENGTH):
    for j in range(FOREST_WIDTH):
        # PART I 
        if visible_from_any_edge(i,j,FOREST_LENGTH,FOREST_WIDTH):
            visible_trees_counter += 1
        # PART II
        # do not include the edge
        if i != 0 and i != FOREST_LENGTH-1 and j != 0 and j != FOREST_WIDTH-1:
            scenic_score_matrix[i,j] = scenic_score(i,j,FOREST_LENGTH,FOREST_WIDTH)
""" pull out answers and script performance
"""
print("the first answer is",visible_trees_counter)
print("the second answer is",int(np.max(scenic_score_matrix)))

# calculate the memory usage
used = psutil.Process().memory_info().rss / 1024 / 1024
# print the memory usage, rounded to two decimal places
print()
print(f"The script used approximately {round(used * 100) / 100} MB")

# calculate the elapsed time
elapsed_time = time.time() - start_time
# print the elapsed time, rounded to two decimal places
print(f"And it took approximately {round(elapsed_time*1000, 2)} ms to run")

