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

- define `right_order_index` an empty list
- parse the input txt file
    - for each groups of 3 lines
        - assign the first line as the `left_packet`
        - assing the second line as the `right_packet`
        - apply the checking procedure 
        - if the checkin procedure returns `True` than append the index of the line to `right_order_index`
