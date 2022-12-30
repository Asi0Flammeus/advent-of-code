import numpy as np
from breadth_first_search import find_shortest_path, get_neighbors, is_valid, build_path

# Create the hilly_labyrith 2D array and fill it with 0's


# Import and parse the input text file
with open('input.txt', 'r') as file:
    lines = file.readlines()
    length = len(lines)
    width = len(lines[0]) - 1
    hilly_labyrith = np.zeros((length,width))
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c.islower():
                hilly_labyrith[i,j] = ord(c) - ord('a')
            elif c == 'E':
                hilly_labyrith[i,j] = 26
            elif c == 'S':
                hilly_labyrith[i,j] = -1

print(hilly_labyrith)
print(get_neighbors(hilly_labyrith,(0,0)))
