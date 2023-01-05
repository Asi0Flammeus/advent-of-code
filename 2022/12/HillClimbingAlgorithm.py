import time
import psutil
import numpy as np
from breadth_first_search import find_shortest_path, get_neighbors, is_valid, build_path, visualize_path

start_time = time.time()

""" Create the hilly_labyrith 2D array and fill it with 0's
"""
input = "input.txt"
lowest_coordinates = []
# Import and parse the input text file
with open(input, 'r') as file:
    lines = file.readlines()
    length = len(lines)
    width = len(lines[0]) - 1
    hilly_labyrith = np.zeros((length,width))
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c.islower():
                hilly_labyrith[i,j] = ord(c) - ord('a') + 1
                if hilly_labyrith[i,j] == 1:
                    lowest_coordinates.append((i,j))
            elif c == 'E':
                hilly_labyrith[i,j] = 26
                end = (i,j)
            elif c == 'S':
                hilly_labyrith[i,j] = 0
                start_0 = (i,j)

# First Part of Puzzle
path = find_shortest_path(hilly_labyrith,start_0, end)
visited_nodes_0 =  len(path)-1

""" visualize path on the output file
"""
visualize_path(input,path)

# Second Part of Puzzle
visited_nodes = []

for start in lowest_coordinates:
    path = find_shortest_path(hilly_labyrith,start, end)
    if path != "not found":
        visited_nodes.append(len(path)-1)

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

