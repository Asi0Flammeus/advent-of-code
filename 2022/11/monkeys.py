class Monkey:
    def __init__(self, starting_items, operation, test, true_destination, false_destination):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.true_destination = true_destination
        self.false_destination = false_destination

    def do_operation(self, old):
        return eval(self.operation)

    def apply_test(self, item):
        return item % self.test == 0

    def throw(self, item):
        new_item = self.do_operation(item)
        if self.apply_test(new_item):
            return self.true_destination
        else:
            return self.false_destination

    def __repr__(self):
        return (self.name,self.items)


