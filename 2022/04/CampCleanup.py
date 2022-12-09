import psutil
import time
import numpy as np

start_time = time.time()

nbr_embeded = 0
nbr_overlap = 0
""" Open the file and read the lines
"""
with open('./input.txt') as f:
  lines = f.readlines()

"""Loop through the lines and split each one into numbers
"""
for line in lines:
    """ Create empty arrays for the numbers
    """
    l = []
    m = []
    n = []
    o = []
    numbers = line.strip().split(',')
    l.append(int(numbers[0].split('-')[0]))
    m.append(int(numbers[0].split('-')[1]))
    n.append(int(numbers[1].split('-')[0]))
    o.append(int(numbers[1].split('-')[1]))

    """ Convert the lists to numpy arrays
    """
    tasks = np.zeros((2,3))
    ## first elf
    tasks[0,0] = np.array(l)
    tasks[0,1] = np.array(m)
    tasks[0,2] = tasks[0,1]-tasks[0,0]
    ## second elf
    tasks[1,0] = np.array(n)
    tasks[1,1] = np.array(o)
    tasks[1,2] = tasks[1,1]-tasks[1,0]

    """ choose the elf who has less tasks
        check if its taks is embeded in the tasks of the other elf
    """
    if min(tasks[0,2],tasks[1,2]) == tasks[0,2]:
        index = 0  # first elf
    else:
        index = 1 # second  elf
    if tasks[index,0] >= tasks[abs(index-1),0]: # lower bound greater or equal than the other elf
        if tasks[index,1] <= tasks[abs(index-1),1]: # upper bound lower or equal than the other elf
            nbr_embeded += 1

    """ check if there's any overlap at all
    """
    if tasks[0,0] <= tasks[1,1] and tasks[0,1] >= tasks[1,0]:
        nbr_overlap += 1

print("the first answer is",nbr_embeded)
print("the second answer is",nbr_overlap)

# calculate the memory usage
used = psutil.Process().memory_info().rss / 1024 / 1024
# print the memory usage, rounded to two decimal places
print()
print(f"The script used approximately {round(used * 100) / 100} MB")

# calculate the elapsed time
elapsed_time = time.time() - start_time
# print the elapsed time, rounded to two decimal places
print(f"And it took approximately {round(elapsed_time*1000, 2)} ms to run")

