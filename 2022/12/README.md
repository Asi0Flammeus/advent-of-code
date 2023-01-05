# DAY 12: HILL CLIMBING ALGORITHM

In order to contact to contact the elves I need to get more signal, hence today's puzzle.
Based on an elevation map (ie. puzzle's input) I need to find the path to where the best signal is and minimize my energy to get there.
It is basically an optimatization problem. 
I can move in four direction (up, down, left, right) but when the destination case is higher than the current one, I can only move there if the destination case is only 1 height above.
Otherwise, there's no constraint if the destination case is lower than the current one. 

## INPUT 

The input txt file is a 2D-array composed of lowercase letters, except 2 letters which denote my initial position `S` and the position where the best signal is `E`.
Each lowercase letter is associated with a relative height, relative to my initial position ; `a` is the lowest, and `z` the heighest.

## SOLVING METHOD

My first idea is inspired by this [video](https://www.youtube.com/watch?v=akZ8JJ4gGLs&ab_channel=Numberphile) that I saw couple months ago. 
Because I need to find the shortest path in a kind of hilly labyrinth, I'll try to implement a breadth-first search algorithm to find it. 

- create 2D array called `hilly_labyrith` and composed of 0's
- import txt file
- parse the input text as a 2D string array
    - if character is lowercase then `hilly_labyrith(i,j)` is set to the relative position of the caracter is the lowercase set + 1
    - if character is `E` then `hilly_labyrith(i,j)` is set to 26
    - if character is `S` then `hilly_labyrith(i,j)` is set to 0
- compute a breadth-first search on `hilly_labyrith` from 0 to 26
    - a potential trajectory is only considered 
        - if next step is equal or 1 higher than the current position
        - else if next step is lower than the current position
- return the lowest number of steps from start to end through `hilly_labyrith`
- the absolutely-not-optimised solution of part II is to apply the breadth-first search on all coordinate at elevation 1

