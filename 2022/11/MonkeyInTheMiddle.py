import re

# Open the input file
with open('input.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Split the contents into a list of lines
lines = contents.split('\n')

# Initialize a dictionary to store the information for each monkey
monkeys = {}
monkey_num = 0
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

# Print the information for each monkey
print(monkeys[2])
