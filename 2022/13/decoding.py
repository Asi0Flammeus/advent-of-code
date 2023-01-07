# define a function to check if a pair of packets is in the right order
def check_order(left, right):
    print()
    print("left is ",left)
    print("right is ",right)
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return check_order(left[1:], right[1:])

    elif isinstance(left, int) and isinstance(right, list):
        while isinstance(right, list): # peeling the left packet
            right = right[0]
        return check_order(left, right)

    elif isinstance(left, list) and isinstance(right, int):
        while isinstance(left, list): # peeling the right packet
            left = left[0]
        return check_order(left, right)

    elif isinstance(left, list) and isinstance(right, list):
        while isinstance(left, list) and isinstance(right, list): # peeling both packet
            left = left[0]
            right = right[0]
        return check_order(left, right)
    else:
        return "something's wrong"

""" modifier l'instruction elif pour faire un test à left[0] et right[0]
    pour vérifier si un des deux est une liste.
    Auquel cas retourner il faut continuer à décortiquer la list (comme pour les 2 prochains elif)
"""

def get_core_list(lst):
    if not isinstance(lst, list):
        return lst
    elif len(lst) == 1:
        return get_core_list(lst[0])
    elif len(lst) > 1:
        return lst
    else:
        return None

# test the function
lst = [[[0,[[1,[[1, 2, 3]]]]]]]
print(get_core_list(lst))
lst = [[[[[[[]]]]]]]
print(get_core_list(lst))
lst = [[[[[[[], []]]]]]]
print(get_core_list(lst))

lst = 1
print(get_core_list(lst))
