import string
import numpy as np

letters = list(string.ascii_letters)
inventory = np.loadtxt("./input.txt", dtype=str)
N_rucksack = len(inventory)

""" First Part of the puzzle
    find the common item in both compartiment (ie. line)
"""
total_priority = 0
for i in range(N_rucksack):
    rucksack = inventory[i]
    # Split the list of letters in half
    first_half = set(rucksack[:len(rucksack)//2])
    second_half = set(rucksack[len(rucksack)//2:])
    common_item = list(first_half.intersection(second_half))
    for j in range(len(letters)):
        if letters[j] == common_item[0]:
            total_priority += (j+1)
            break
print("first answer is",total_priority)

""" Second Part of the puzzle
    find the common item within 3 rucksacks (ie. 3 lines)
"""
total_priority = 0
group_size = 3
k = 0
for i in range(N_rucksack//group_size):
    rucksacks = list(inventory[k:k+3])
    # find the common item 
    common_item = set(rucksacks[0]).intersection(set(rucksacks[1]))
    badge = list(common_item.intersection(set(rucksacks[2])))
    for j in range(len(letters)):
        if letters[j] == badge[0]:
            total_priority += (j+1)
            break
    k += 3
print("second answer is",total_priority)
