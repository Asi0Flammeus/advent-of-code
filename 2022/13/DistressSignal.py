import ast
# define a function to check if a pair of packets is in the right order
def check_order(left, right):
    print(left,right)
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return check_order(left[1:], right[1:])
    """ modifier l'instruction elif pour faire un test à left[0] et right[0]
        pour vérifier si un des deux est une liste. 
        Auquel cas retourner il faut continuer à décortiquer la list (comme pour les 2 prochains elif)
    """
    elif isinstance(left, list) and isinstance(right, list):
        print(left[0], right[0])
        if left[0] < right[0]:
            return True
        elif right[0] < left[0]:
            return False
        else:
            return check_order(left[1:], right[1:])
    elif isinstance(left, int) and isinstance(right, list):
        return check_order([left] + left[1:], right)
    elif isinstance(left, list) and isinstance(right, int):
        print([right]+right[1:])
        return check_order(left, [right] + right[1:])
    else:
        return False

# define an empty list to store the indices of the right-ordered pairs
right_order_indices = []
order = []
# parse the input txt file
with open('input.txt', 'r') as f:
    lines = f.readlines()

# iterate over groups of 3 lines
for i in range(0, len(lines), 3):
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
