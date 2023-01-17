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
            interger = -1 # -1 is associated to an empty set
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

a = [[],[1,[3,[0]]],[]]
b = [[],[[0,[5,3,0,1,0],[3,0,5,7],10,[2,8,5,0]],10,[2,4,[1],[5,6,7],[]],[]]]

left = Code(a)
right = Code(b)

print(a)
print(left.intergers)
print(left.intergers.get(25,None) is None)

print()
print(b)
print(right.intergers)
""" next step try to find a way to check value between 2 different codes
"""

def check_procedure(left, right):
    left_depth = 1
    right_depth = 1

    for index in range(len(left.intergers)):
        if right.intergers.get(index,None) is None:
            return False
        else:
            # how to parse each element to verify left < right?
            pass
