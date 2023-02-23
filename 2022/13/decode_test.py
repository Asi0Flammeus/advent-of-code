def compare_nested_lists(lst1, lst2):
    print(lst1)
    print(lst2)
    print()
    if isinstance(lst1, int) and isinstance(lst2, int):
        if lst1 < lst2:
            return True
        elif lst1 > lst2:
            return False
        else:
            return compare_nested_lists([], [])
    elif isinstance(lst1, int):
        return compare_nested_lists([lst1], lst2)
    elif isinstance(lst2, int):
        return compare_nested_lists(lst1, [lst2])
    else:
        if not lst1 and not lst2:
            return True
        elif not lst1:
            return True
        elif not lst2:
            return False
        else:
            if isinstance(lst1[0], list) and isinstance(lst2[0], int):
                lst2 = [lst2]
            elif isinstance(lst1[0], int) and isinstance(lst2[0], list):
                lst1 = [lst1]

            if lst1[0] < lst2[0]:
                return True
            elif lst1[0] > lst2[0]:
                return False
            else:
                return compare_nested_lists(lst1[1:], lst2[1:])
