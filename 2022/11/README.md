## DAY 11 -- MONKEY IN THE MIDDLE

Some wity monkeys play with my items ... The only way to get these items back is to analyse their behavior. 

So I took some notes (ie. today's input txt) on how monkey makes decisions based on my worry level. It seems that when a monkey catch an item, he inpects it (aka operation on the worry level) and then test my worry level. But before that test, because the monkey didn't damage the item, my worry level is divided by 3 and round to the closest interger. Then based on the outcome of the test worry level, the monkey throw the item to another monkey. And it starts again. But monkeys take turn in their little game. Monkey 0 goes first then Monkey 1 an so on. When each monkey has done their turn, a round has been achieved. 

Because it's infeasible to chase all monkeys at once, I'll only focus on the two most active and I count the total number of times each monkey inspects items over 20 rounds.


### INPUT: 

It's composed of the initial state of all monkeys. 

A item can be considered as an object class such as: 
    - attributes: 
        - `self.name` = interger from 0 to $N-1$ (for $N$ items)
        - `self.worry_level` = worry level associated with this item

A monkey can be considered as an object class such as: 
    - attributes: 
        - `self.name` = interger from 0 to $M-1$ (for $M$ monkeys)
        - `self.items` = list of item in posession
        - `self.inspected_items` = number of inspected item
    - methods:
        - `operation(old)` = return `new` after some specific operation 
        - `divisibility_test(worry_level)` = return to which monkey the item would be thrown based on a specific test on the `worry_level`
        - `true_destination` = monkey index that receive the item if the outcome of the divisibilitytest is true
        - `false_destination` = monkey index that receive the item if the outcome of the divisibilitytest is false

 ### SOLVING METHOD 

- define `MONKEY_NUM = 0` AND `ITEM_NUM = 0`
- define `monkeys` a empty list
- parse the input txt file to define the initial state of monkeys 
    - read input txt file 7 lines by 7
    - the first line begins with `Monkey i:` where `i` is an interger
        - the name would be the `i`
        - add 1 to `MONKEY_NUM`
    - the next one starts with `Starting items:` 
        - all interger (separated by `,`) after the `:` is a item with it worry level
        - for each item add 1 to `ITEM_NUM`
    - the next one starts with `Operation:` define the method `operation(old)`
    - the next one starts with `Test:` 
        - the interger after `divisible by` is define `divisibility test` method
            - the interger at the end of the next line is the outcome if test is `True`
            - the interger at the end of the second next line is the outcome if test is `False`
    - add monkey to `monkeys` list
    - jump to next 7 lines 
- define `ROUND = 0` and `MAX_ROUND = 20`
- for in range of `MAX_ROUND`
    - for monkey in monkeys
        - if `monkey.items` is not empty:
            - add 1 to `monkey.inspected_items`
            - apply `operation` on the `worry_level` of the first item 
            - divide the `worry_level` of that item by 3 (only for part I)
            - apply the `test(worry_level)`
            - do a modulo of the worry level by which is the product of all divisibility_test_num
            - and append this item to the items list of the corresponding monkey of the test outcome

- print for all monkeys theirs number of inspected items 
    


