import time
import psutil
import re
from monkeys import Monkey

start_time = time.time()

# Open the input file
with open('input.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Split the contents into a list of lines
lines = contents.split('\n')

# Initialize a dictionary to store the information for each monkey
monkeys = {}
monkey_num = 0
p_product = 1
# Iterate over the lines
for line in lines:
    # Check if the line starts with "Monkey"
    if line.startswith("Monkey"):
        # Extract the monkey number from the line
        monkey_num = int(line.split()[1][:-1])
        # Initialize an empty dictionary for the monkey
        monkeys[monkey_num] = {}

    # Check if the line starts with "Starting items"
    elif line.startswith("  Starting items"):
        # Extract the starting items from the line after remove the ","
        item_list = (line.split()[2:])
        formated_item_list = []
        for item in item_list:
            if item[-1] == ",":
                item = item[:-1]
            formated_item_list.append(item)
        starting_items = list(map(int, formated_item_list))
        # Add the starting items to the monkey's dictionary
        monkeys[monkey_num]['starting_items'] = starting_items

    # Check if the line starts with "Operation"
    elif line.startswith("  Operation"):
        # Extract the operation from the line
        operation = line.split(':')[1][1:]
        operation = operation.replace("new = ", "")
        # Add the operation to the monkey's dictionary
        monkeys[monkey_num]['operation'] = operation

    # Check if the line starts with "Test"
    elif line.startswith("  Test"):
        # Extract the test divisibility number from the line
        test_divisibility_num = int(line.split()[-1])
        # Add the test divisibility number to the monkey's dictionary
        monkeys[monkey_num]['test_divisibility_num'] = test_divisibility_num

    # Check if the line starts with "If true"
    elif line.startswith("    If true"):
        # Extract the true destination from the line
        true_destination = int(line.split()[-1])
        # Add the true destination to the monkey's dictionary
        monkeys[monkey_num]['true_destination'] = true_destination

    # Check if the line starts with "If false"
    elif line.startswith("    If false"):
        # Extract the false destination from the line
        false_destination = int(line.split()[-1])
        # Add the false destination to the monkey's dictionary
        monkeys[monkey_num]['false_destination'] = false_destination

# A list to store the created Monkey instances
monkeys_list = []

# Iterate through the dictionary to create monkey instances
for i, data in monkeys.items():
    # Create a Monkey instance with the data from the dictionary
    monkey = Monkey(i, data['starting_items'], data['operation'], data['test_divisibility_num'], data['true_destination'], data['false_destination'])
    # Add the instance to the list
    monkeys_list.append(monkey)
    p_product = p_product * monkey.test_divisibility_num

print(p_product)
# Simulate the round of the game monkey in the middle
ROUND_NUM = 10000 # 20 for PART I

for i in range(ROUND_NUM):
    for monkey in monkeys_list:
        for item in monkey.items: # monkey holds at least 1 item
            item = item % p_product
            next_monkey, worry_level = monkey.throw(item)
            monkeys_list[next_monkey].items.append(worry_level)
        monkey.items = []

# Compute monkey business
monkey_business = []
for monkey in monkeys_list:
    monkey_business.append(monkey.inspected_item)
monkey_business.sort()
total_monkey_business = monkey_business[-2]*monkey_business[-1]

""" pull out answers and script performance
"""
print("the answer is", total_monkey_business)
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

