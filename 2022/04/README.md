## DAY 4 -- CAMP CLEANUP 

Elves need to clean their camp to unload their ship.
Each section of the camp is assigned an ID number. 
Elves would pair up to clean and both has a certain range of sections assigned.

First task: how many of asi one of the range is embeded in the other? 
Second task: In how many assignment pairs do the ranges overlap?

### INPUT

Each line represents the range of sections anh assignment pair.
- `,` separates the first elf from the other 
- `-` separates the lower bound and the upper bound of the range

### SOLVING METHOD 

- to parse the input, we have to use of `readlines` because each line is composed of a mixed of types (string+int) 
- for each line 
    - split the line to find the lower and upper bound for both elves
    - fill up the tasks array and add the distance range 
    - choose the elf with the smaller range
    - check if its range is embeded in the range of the other elf
    - check if there's any overlap
 
