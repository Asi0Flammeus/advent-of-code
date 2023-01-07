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

""" modifier l'instruction elif pour faire un test à left[0] et right[0]
    pour vérifier si un des deux est une liste.
    Auquel cas retourner il faut continuer à décortiquer la list (comme pour les 2 prochains elif)
"""
