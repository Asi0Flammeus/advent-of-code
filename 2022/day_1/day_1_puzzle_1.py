import numpy as np

elves_per_calorie = []
index = 0
tmp = []
index = 0

"""
    parsing the txt file
    create a list of each item's calorie with tmp list
    each elves is delimited with a "\n"
"""
with open('day_1_input.txt') as f:
    for line in f:
        if line == "\n":
            index += 1
            elves_per_calorie.append(tmp)
            tmp = []
        else:
            tmp.append(int(line.rstrip("\n")))

"""
    from that list compute the total calorie hold by each elf
    to find the one with the maximum calorie
"""
maximum_calories_per_elves = np.zeros(len(elves_per_calorie))
for i in range(len(elves_per_calorie)):
    maximum_calories_per_elves[i] = sum(elves_per_calorie[i])

"""
    compute the top 3 of calorie holders
"""
maximum_calories_per_elves = np.sort(maximum_calories_per_elves)
print(sum(maximum_calories_per_elves[-3:]))



