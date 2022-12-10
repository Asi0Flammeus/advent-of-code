import time
import psutil
from rope_model import move_tail, move_knots

start_time = time.time()

# define the size of the grid
N = 1000

# initialize the grids with all sites unvisited
grid_1 = [[False for j in range(N)] for i in range(N)]
grid_2 = [[False for j in range(N)] for i in range(N)]

# initialize the counters for visited sites
visited_sites_counter_1 = 0
visited_sites_counter_2 = 0

# initialize the coordinates of the head and tail
head = (0, 0)
tail = (0, 0)
knots = [(0, 0) for i in range(9)]

# open the input file for reading
with open("input.txt", "r") as f:
    # read each line of the input file
    for line in f:
        # split the line into direction and number of moves
        direction, num_moves = line.split()
        num_moves = int(num_moves)

        # determine the displacement based on the direction
        if direction == "R":
            dx, dy = 1, 0
        elif direction == "L":
            dx, dy = -1, 0
        elif direction == "U":
            dx, dy = 0, -1
        elif direction == "D":
            dx, dy = 0, 1

        # move the head by the specified number of moves
        for i in range(num_moves):
            head = (head[0] + dx, head[1] + dy)

            # move the tail if needed and update the visited sites counter
            tail = move_tail(head, tail)
            if not grid_1[tail[0]][tail[1]]:
                visited_sites_counter_1 += 1
                grid_1[tail[0]][tail[1]] = True

            # move the knots if needed and update the visited sites counter
            knots = move_knots(head, knots)
            if not grid_2[knots[-1][0]][knots[-1][1]]:
                visited_sites_counter_2 += 1
                grid_2[knots[-1][0]][knots[-1][1]] = True

""" pull out answers and script performance
"""
print("the first answer is", visited_sites_counter_1)
print("the second answer is", visited_sites_counter_2)

# calculate the memory usage
used = psutil.Process().memory_info().rss / 1024 / 1024
# print the memory usage, rounded to two decimal places
print()
print(f"The script used approximately {round(used * 100) / 100} MB")

# calculate the elapsed time
elapsed_time = time.time() - start_time
# print the elapsed time, rounded to two decimal places
print(f"And it took approximately {round(elapsed_time*1000, 2)} ms to run")

