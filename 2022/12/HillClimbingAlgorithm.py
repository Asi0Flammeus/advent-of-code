import time
import psutil
import numpy as np
from breadth_first_search import find_shortest_path, get_neighbors, is_valid, build_path

start_time = time.time()

""" Create the hilly_labyrith 2D array and fill it with 0's
"""
# Import and parse the input text file
with open('input.txt', 'r') as file:
    lines = file.readlines()
    length = len(lines)
    width = len(lines[0]) - 1
    hilly_labyrith = np.zeros((length,width))
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c.islower():
                hilly_labyrith[i,j] = ord(c) - ord('a') + 1
            elif c == 'E':
                hilly_labyrith[i,j] = 26
                end = (i,j)
            elif c == 'S':
                hilly_labyrith[i,j] = 0
                start_0 = (i,j)

# First Part of Puzzle
path = find_shortest_path(hilly_labyrith,start_0, end)
visited_nodes_0 =  len(path)-1

# Second Part of Puzzle
visited_nodes = []
# find all the coords where hilly_labyrith = 1

for start in coordinates:
    path = find_shortest_path(hilly_labyrith,start, end)
    visited_nodes.append(len(path)-1)

""" visualize path on the output file
"""
## Open the input file in read mode
#with open("input.txt", "r") as in_file:
#  # Read the file into a list of lines
#  lines = in_file.readlines()
#
## Convert the list of lines into a 2D list of characters
#matrix = [list(line.strip()) for line in lines]
#
## Modify the elements of the matrix based on their row and column coordinates
#for i in range(len(matrix)):
#    for j in range(len(matrix[i])):
#        if [i,j] in path:
#            index = path.index([i,j])
#            if index < len(path)-1:
#                next_node = path[index+1]
#
#                if i == next_node[0] - 1:
#                    matrix[i][j] = "v"
#                elif i == next_node[0] + 1:
#                    matrix[i][j] = "^"
#                elif j == next_node[1] - 1:
#                    matrix[i][j] = ">"
#                elif j == next_node[1] + 1:
#                    matrix[i][j] = "<"
#        else:
#            matrix[i][j] = "."
#
## Open the output file in write mode
#with open("output.txt", "w") as out_file:
#  # Write the modified matrix to the output file
#  for row in matrix:
#    out_file.write(''.join(row) + '\n')


""" pull out answers and script performance
"""
print("the first answer is", visited_nodes_0)
print("the second answer is", min(visited_nodes))

# calculate the memory usage
used = psutil.Process().memory_info().rss / 1024 / 1024
# print the memory usage, rounded to two decimal places
print()
print(f"The script used approximately {round(used * 100) / 100} MB")

# calculate the elapsed time
elapsed_time = time.time() - start_time
# print the elapsed time, rounded to two decimal places
print(f"And it took approximately {round(elapsed_time*1000, 2)} ms to run")

