import ast
from decode_test import compare_nested_lists
# define an empty list to store the indices of the right-ordered pairs
right_order_indices = []
order = []
# parse the input txt file
with open('input.txt', 'r') as f:
    lines = f.readlines()

i = 3

# iterate over groups of 3 lines
for i in range(0, len(lines), 3):
    # assign the first line as the left packet
    left = ast.literal_eval(lines[i])
    # assign the second line as the right packet
    right = ast.literal_eval(lines[i+1])

    # apply the checking procedure
    print(left)
    order.append(compare_nested_lists(left, right))
    if compare_nested_lists(left, right):
        # append the index of the line to right_order_indeix
        right_order_indices.append(int(i/3)+1)

# print the indices of the right-ordered pairs
print(sum(right_order_indices))
print(order)
