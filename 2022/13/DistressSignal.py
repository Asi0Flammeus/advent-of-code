import ast
from decoding import check_order
# define an empty list to store the indices of the right-ordered pairs
right_order_indices = []
order = []
# parse the input txt file
with open('input.txt', 'r') as f:
    lines = f.readlines()

i = 3
# iterate over groups of 3 lines
#for i in range(0, len(lines), 3):

# assign the first line as the left packet
left_packet = ast.literal_eval(lines[i])
# assign the second line as the right packet
right_packet = ast.literal_eval(lines[i+1])

# apply the checking procedure
order.append(check_order(left_packet,right_packet))
if check_order(left_packet, right_packet):
    # append the index of the line to right_order_index
    right_order_indices.append(int(i/3))

# print the indices of the right-ordered pairs
print(right_order_indices)
print(order)
