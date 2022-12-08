## DAY 5 -- SUPPLY STACKS

Help the elves to find the next crates to unload from the ship. 
These crates are those that would end up on the top of each stack. 
The elves have a drawing of the initial state of the stacks and the rearrangement procedure (ie. the input).

What are the crate that ends up on top of each stack?

### INPUT 

1. The initial state (from line 0 to 8)
    - each odd column (from 0 to 17) defines the stack state of the pile 
    - each crate is defined as an uppercase letter in between bracket (eg. [A])
2. the rearrangement procedure (from line 10 to the end)
    - each procedure follows the same template "move n from i to d"
    - n = number of creates to move 
    - i = initial pile 
    - d = destination pile

When n creates is moved, each crate is moved one by one from top to bottom.

### SOLVING METHOD 


- read the input 
- separate the initial state from the procedure plan 
- initialize 10 stacks based on the initial plan 
- for each line of the procedure plan 
    - use `.pop()` to move the crate between the stacks

