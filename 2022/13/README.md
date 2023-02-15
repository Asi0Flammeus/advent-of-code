# DAY 13 : DISTRESS SIGNAL

I am now a the top of the hill, ready to contact those elves. 
Instead I received a *distress signal* (ie. today's input). 
Obviously my device seems to not work properly, hence today's puzzle : decoding message.

The message is sent by pair of packets.
So I need to check how many pair of packets are in the right order. 

# INPUT

Each pair of packets are separated by an empty line. 
Each packet is a list which contain either:
- nothing
- an interger
- another list which can contain nothing, an interger, or another list

For a given pair of packet, the first one is considered to be the `left` packet and the second one the `right` one. 

To check weither the pair of packets is in the right order, I have to follow this procedure : 
- if the both values are `int`
    - if left is lower than right, the pair of packets is in the right order (ie. return `True`))
    - elif right is lower than left, the pair of packets is not in the right order (ie. return `False`))
    - else continue the procedure (ie. go to next value)
- if both values are `list`
    - compare the first element
        - if left element is lower than the right element then it is in the right order 
        - if right element is lower than left element then it is not in the right order
        - if both is equal than go to the next element
- if one of them is an interger and the other a list:
    - transform the interger into a list containing the interger and apply re-apply the checking procedure
- if the right side ran out of items, than it is not in the right order
- if the left side ran out of items, than it is in the right order

# SOLVING METHOD 

I want to have a `decode.py` that contains the Code class. 
A code is an *arbitrarily nested list* that contains intergers and list. 
Each interger would be track through `code.intergers`, a nested dictionnary for keeping track of the value, depth and position of each interger. 

- [x] define the `__init__` constructor with the help of a `traverse_code()` function
- [ ] define a `check_procedure(left,right)` to check if the packets are in the right order
    - [x] right ran out of items
    - [x] left ran out of items => default value
    - [x] both element are equal so pass on next element for both list => let the loop continue
    - [x] right item is lower than left item
- [ ] verify that `check_procedure` works with the example input txt
