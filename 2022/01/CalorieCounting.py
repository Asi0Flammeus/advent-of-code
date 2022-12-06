import numpy as np

Inventories = []
Inventory = []

""" Parsing the txt file to reate an Inventory of each item's.
    Each elves is delimited with a "\n"
"""
with open('input.txt') as f:
    for line in f:
        if line == "\n":
            index += 1
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



