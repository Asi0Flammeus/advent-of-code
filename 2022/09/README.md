## DAY 9 -- ROPE BRIDGE 

As I walk along a not-so-reassuring" rope bridge, I'm trying to distract myself by modelling a hypothetical series of motions (ie. today's input) for a rope with a knot at its head and tail.

The first puzzle is to compute how many positions the rope's tail visit at least once?

### INPUT

- Each line is a serie of motion divided in two parts:
    1. a uppercase letter to define in which direction the head would go
        - R = Right / L = Left / U = Up / D = Down
    2. an interger that define how many time the head would go in that direction

### ROPE MODEL 

- the head (H) and tail (T) must always be touching
- here we consider [Moore neighborhood](https://en.wikipedia.org/wiki/Moore_neighborhood)
- when T moves, it can overlap H
- when H and T are overlapping, it is also considered as touching
- when T does not touch the H, its motion to spring back to H and it would be based on 2 rules: 
    1. if the T is on the same row or column as H, then T moves 1 step towards H
    2. if the T isn't on the same row or column as H, then T moves 1 step towards H but diagonnaly in order to touch be in the moore neighborhood of T
- the second part of the puzzle is with a rope composed of 1 head and 9 knots
### SOLVING METHOD 

- consider a 2D grid of a given size
    - if H gets to the grid's edge, then grid size is increased by 10%
- for each line of the input
    - split the line and determine the direction and the number of move
        - for each move update the position of :
            - the Head (H) 
            - the Tail (T) if needed based on the rope model
            - if T visits a new grid site then `VISITED_SITES_COUNTER` is increased by 1
- print out `VISITED_SITES_COUNTER`
