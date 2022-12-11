import time
import psutil

start_time = time.time()

# compute the signal strenght

def signal_strength(X,cycle_number):
    return X * cycle_number

# define initial values for cycle_number, X, and total_signal_strength
cycle_number = 0
X = 1
total_signal_strength = 0

SPRITE_HALF_LENGTH = 1
CRT_WIDTH = 40
CRT = ['.']*CRT_WIDTH
CRT_pixel_position = 0



# open the input txt file
with open('input.txt', 'r') as f:
    # read the file line by line
    for line in f:
        # parse the instruction in the line
        instruction = line.split()
        if instruction[0] == 'addx':
            # if the instruction is 'addx Z', add Z and complete 2 cycles
            Z = int(instruction[1])
            wait_cycles = 2
        elif instruction[0] == 'noop':
            # if the instruction is 'noop', do nothing and add 1 to cycle
            wait_cycles =  1

        for i in range(wait_cycles):
            cycle_number += 1

            # check if SPRITE is aligned with pixel
            if X - SPRITE_HALF_LENGTH <= CRT_pixel_position <= X + SPRITE_HALF_LENGTH:
                CRT[CRT_pixel_position] = "#"
            CRT_pixel_position += 1

            # if cycle is equal to condition of 1st puzzle
            if cycle_number % CRT_WIDTH == 20:
                total_signal_strength += signal_strength(X,cycle_number)

            # if cycle is a multiple of the CRT width
            if cycle_number % CRT_WIDTH == 0:
                print(" ".join(CRT))
                CRT = ['.']*CRT_WIDTH
                CRT_pixel_position = 0
        # move the sprite based on the instruction
        if instruction[0] == 'addx':
            X += Z

""" pull out answers and script performance
"""
print("the first answer is", total_signal_strength)
#print("the second answer is", visited_sites_counter_2)

# calculate the memory usage
used = psutil.Process().memory_info().rss / 1024 / 1024
# print the memory usage, rounded to two decimal places
print()
print(f"The script used approximately {round(used * 100) / 100} MB")

# calculate the elapsed time
elapsed_time = time.time() - start_time
# print the elapsed time, rounded to two decimal places
print(f"And it took approximately {round(elapsed_time*1000, 2)} ms to run")

