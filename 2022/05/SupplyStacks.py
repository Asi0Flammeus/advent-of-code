import psutil
import time
import re
import copy

start_time = time.time()

""" Open the input file in read-only mode
"""
with open("input.txt", "r") as f:
  """ Read the entire contents of the file as a single string
  """
  text = f.read()

""" Split the input text into two parts using the line that begins with "1" as the delimiter
"""
parts = text.split(" 1   2")

""" The first part is the initial state of the piles
"""

initial_state = parts[0]
initial_state = initial_state.split('\n')

""" The second part is the procedure to be applied to the piles
"""
procedure = parts[1]
procedure = procedure.split('\n')
procedure = procedure[2:-1]

""" parse the initial_state list to create the initial state
    of each stack
"""
INTRA_COLUMN_WIDTH = 3
INTER_COLUMN_WIDTH = 1
NUM_STACKS = 9

stacks = [[] for i in range(NUM_STACKS)]

for i in reversed(range(len(initial_state)-1)): # start from the base
    for j in range(NUM_STACKS):
        if initial_state[i][(INTRA_COLUMN_WIDTH+INTER_COLUMN_WIDTH)*j+1] != " ": # check if there's crate for the j stack
            stacks[j].append(initial_state[i][(INTRA_COLUMN_WIDTH+INTER_COLUMN_WIDTH)*j+1])

stacks9000 = copy.deepcopy(stacks)
stacks9001 = copy.deepcopy(stacks)

""" parse the procedure to apply each move
"""
# loop through each element in the list
for step in procedure:
    # use a regular expression to extract all integers from the element
    numbers = re.findall(r'\d+', step)
    # convert the numbers to int data type
    numbers = [int(number) for number in numbers]

    NUM_CRATES = numbers[0]
    INITIAL_STACK = numbers[1]-1
    FINAL_STACK = numbers[2]-1

    """ anticipate the procedure with CraneMover9000 (ie. one by one)
    """
    for i in range(NUM_CRATES):
        stacks9000[FINAL_STACK].append(stacks9000[INITIAL_STACK].pop())

    """ anticipate the procedure with CraneMover9001 (ie. multiple crates at once)
    """
    SPLIT_INDEX = len(stacks9001[INITIAL_STACK]) - NUM_CRATES
    MOVING_CRATES = stacks9001[INITIAL_STACK][SPLIT_INDEX:]

    stacks9001[INITIAL_STACK] = stacks9001[INITIAL_STACK][:SPLIT_INDEX]
    stacks9001[FINAL_STACK] += MOVING_CRATES

""" give the first answer (ie. the top crates of each stacks))
"""
ANSWER_1 = []
ANSWER_2 = []
for i in range(NUM_STACKS):
    ANSWER_1 += stacks9000[i][-1]
    ANSWER_2 += stacks9001[i][-1]
ANSWER_1 = "".join([element for element in ANSWER_1])
ANSWER_2 = "".join([element for element in ANSWER_2])
print("The 1st answer is",ANSWER_1)
print("The 2st answer is",ANSWER_2)


# calculate the memory usage
used = psutil.Process().memory_info().rss / 1024 / 1024
# print the memory usage, rounded to two decimal places
print()
print(f"The script used approximately {round(used * 100) / 100} MB")

# calculate the elapsed time
elapsed_time = time.time() - start_time
# print the elapsed time, rounded to two decimal places
print(f"And it took approximately {round(elapsed_time*1000, 2)} ms to run")


