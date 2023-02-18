import ast
from decode import Code, check_procedure
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
    left_packet = ast.literal_eval(lines[i])
    left = Code(left_packet)
    # assign the second line as the right packet
    right_packet = ast.literal_eval(lines[i+1])
    right = Code(right_packet)

    # apply the checking procedure
    order.append(check_procedure(left, right))
    if check_procedure(left, right):
        # append the index of the line to right_order_indeix
        right_order_indices.append(int(i/3)+1)

# print the indices of the right-ordered pairs
print(sum(right_order_indices))
print(order)
