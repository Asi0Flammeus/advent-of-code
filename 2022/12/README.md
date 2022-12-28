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



