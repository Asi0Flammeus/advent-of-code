class Monkey:
    def __init__(self, name, starting_items, operation, test_divisibility_num, true_destination, false_destination):
        self.name = name
        self.items = starting_items
        self.operation = operation
        self.test_divisibility_num = test_divisibility_num
        self.true_destination = true_destination
        self.false_destination = false_destination
        self.inspected_item = 0

    def do_operation(self, old):
        # Evaluate the operation using the old value as input
#        old = old % self.test_divisibility_num
        new = eval(self.operation, {'old': old})
        return new

    def apply_test(self, score):
        return score%self.test_divisibility_num == 0

    def throw(self, item):
        # monkey inspects
        new_score = self.do_operation(item)
        self.inspected_item += 1
        # not broken so score is reduced
#        new_score = int(new_score/3) # uncomment for part I
        # monkey throw to another monkey based on my current worry level
        if self.apply_test(new_score):
            return (self.true_destination, new_score)
        else:
            return (self.false_destination, new_score)

    def __repr__(self):
        return f'{self.name} has {self.items} and has inspected {self.inspected_item} items'
