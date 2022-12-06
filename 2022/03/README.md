## DAY 3 -- RUCKSACK REORGANIZATION

A not-so-clever elf messed up with the rucksack packing.
He added a same-type item in both compartiments of the bag. 
Each item type is defined by a upper or lowercase letter. (a-Z) 
The first task is to find that same item in every rucksack and compute the total score of those items. 

The second task is to find the badge of each group of three elves and compute the total score of thoses item. 
A badge is define as the only item in common within the group. 


### INPUT 

Each line represents a rucksack. 
Each caracter is an item and each item type is symbolized with a lower or uppercase letter.
Compartiment A is the first half of the string ; Compartiment B is the other half.

### SOLVING METHOD

- use `string.ascii_letters` to get an order list of the item type
- define `total_priotity`
- for each line (ie. rucksack)
    - split in 2 compartiment
    - find the intersection between both sets (ie. the common item type)
    - compute the associated priority
    - add to total priority 
- for each 3 lines (ie. group)
    - find the common item in the first two lines 
    - find the common item with the last line 
    - compute the priority of the badge 
    - add to total priority 
