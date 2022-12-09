import psutil
import time
import numpy as np

start_time = time.time()

Inventories = []
Inventory = []

""" Parsing the txt file to reate an Inventory of each item's.
    Each elves is delimited with a "\n"
"""
with open('input.txt') as f:
    for line in f:
        if line == "\n":
            Inventories.append(Inventory)
            Inventory = []
        else:
            Inventory.append(int(line.rstrip("\n")))

""" From that list compute the total calorie hold by each elf
    to find the one with the maximum calorie
"""
TotalCalories = np.zeros(len(Inventories))
for i in range(len(Inventories)):
    TotalCalories[i] = sum(Inventories[i])
print("the first answer is",int(max(TotalCalories)))

""" Compute the top 3 of calorie holders
"""
TotalCalories = np.sort(TotalCalories)
print("the second answer is",int(sum(TotalCalories[-3:])))

# calculate the memory usage
used = psutil.Process().memory_info().rss / 1024 / 1024
# print the memory usage, rounded to two decimal places
print()
print(f"The script used approximately {round(used * 100) / 100} MB")

# calculate the elapsed time
elapsed_time = time.time() - start_time
# print the elapsed time, rounded to two decimal places
print(f"And it took approximately {round(elapsed_time*1000, 2)} ms to run")

