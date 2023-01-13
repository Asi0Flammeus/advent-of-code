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

a = [[1],[2,3,4]]

code_test = Code(a)
print(a)
print(code_test.intergers)


""" next step try to find a way to check value between 2 different codes
"""
