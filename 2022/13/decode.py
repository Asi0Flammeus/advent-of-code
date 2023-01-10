class Code:
    def __init__(self, input_list):
        self.intergers = {}
        for i, element in enumerate(input_list):
            self.intergers[i] = {"value": element,
                                "address": (0,0)
                                 }


a = [[1],[2,3,4]]

code_test = Code(a)
print(code_test.intergers)

current_adrress = [0]
a_adresses = []
for i, element in enumerate(a):
    if isinstance(element, int) or element == None:
        a_adresses.append(current_adrress)
    else:
        a = 1
b = [[[]]]
depth = 0
index = 0
def traverse(nested_list, depth, index):
    global addresses

    if isinstance(nested_list, int):
        interger = nested_list
        addresses.append([interger, depth, index])

    elif len(nested_list) == 0:
        empty_list = nested_list
        addresses.append([empty_list, depth, index])
    else:
        depth += 1
        for i, element in enumerate(nested_list):
            traverse(element, depth, i)

c = [1,[2,[3,[4,[5,6,7]]]],8,9]
addresses = []
print(traverse(c, depth, index))
print()
print(addresses)

""" need to add the traverse function into the Code class into order to only change addresses dict of the corresponding code instance.
"""
