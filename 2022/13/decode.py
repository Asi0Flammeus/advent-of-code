class Code:
    def __init__(self, input_txt):
        self.intergers = {}
        self.depth = 0
        self.list_index = 0
        self.dict_index = 0
        self.traverse_code(input_txt)

    def traverse_code(self, nested_list):
        """ parse a nested list to extract the address of
            each intergers.
            an address is define by a depth and and list_index
        """
        if isinstance(nested_list, int):
            interger = nested_list
            self.intergers[self.dict_index] = {
                                                "value": interger,
                                                "depth": self.depth,
                                                "index": self.list_index
                                            }
            self.dict_index += 1
        elif len(nested_list) == 0:
            interger = -1 # -1 this value is associated to an empty set
            self.intergers[self.dict_index] = {
                                                "value": interger,
                                                "depth": self.depth,
                                                "index": self.list_index
                                            }
            self.dict_index += 1
        else:
            self.depth += 1
            for i, element in enumerate(nested_list):
                self.list_index = i
                self.traverse_code(element)

# a = [[[]]]
# b = [[]]
# 
# a = [1,[2,[3,[4,[5,6,[]]]]],9,5,5,9]
# b = [1,[2,[3,[4,[5,6,[[]]]]]],8,9]
# 
# left = Code(a)
# right = Code(b)
# 
# print(a)
# print(left.intergers)
# # print(left.intergers.get(0,None)["value"])
# 
# print()
# print(b)
# print(right.intergers)
""" next step try to find a way to check value between 2 different codes
"""

def check_procedure(left, right):
    left_depth = 1
    right_depth = 1
    right_order = True # default value True in case left ran out of items first

    for index in range(len(left.intergers)):
        if right.intergers.get(index,None) is None:
            # right packet ran out of items so it's not in the right order
            right_order = False
            break
        elif right.intergers.get(index,None)["value"] == -1 and left.intergers.get(index,None)["value"] == -1:
            if right.intergers.get(index,None)["depth"] < left.intergers.get(index,None)["depth"]:
                # right list is lower than left one so it's not in the right order
                right_order = False
        elif right.intergers.get(index,None)["value"] == -1 and left.intergers.get(index,None)["value"] != -1:
            # right list ran out of elements so it's not in the right order
            right_order = False
        elif right.intergers.get(index,None)["value"] != -1 and left.intergers.get(index,None)["value"] == -1:
            # left list ran out of elements so it's in the right order
            break
        elif right.intergers.get(index,None)["value"] > left.intergers.get(index,None)["value"]:
            # left item is lower than left one so it's in the right order
            break
        elif right.intergers.get(index,None)["value"] < left.intergers.get(index,None)["value"]:
            # right item is lower than left one so it's not in the right order
            right_order = False
            break
    return right_order


# print(check_procedure(left, right))
