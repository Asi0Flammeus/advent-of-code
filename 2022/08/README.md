## DAY 8 -- TREETOP TREE HOUSE

Thanks to a previous expedition, we find a huge forest which seems to have the potential to host our tree house. However, the treehouse must be hidden by the forest. Hence today's quest. 

Based on a map of the height of each tree of the forest (ie. `input.txt`), the elves asked me to compute the number of visible trees. 

A visible tree is defined as such if all trees between itself and the edge are smaller than the tree in four direction (up, down, left, right).

### INPUT 

The input is a 2D grid of numbers between 0 and 9. Each number represents the height of a tree, where 9 is the tallest and 0 the shortest. 

### Solving method 

- import `input.txt` as a numpy array with `np.loadtxt()` called `forest`
- define `FOREST_WIDTH` and `FOREST_LENGTH`
- define `visible_from_any_edge(TREE_X,TREE_Y, FOREST_LENGTH, FOREST_WIDTH)`
    - up: `(EDGE_X, EDGE_Y) = (0, TREE_Y)`
    - down: `(EDGE_X, EDGE_Y) = (FOREST_LENGTH-1, TREE_Y)`
    - left: `(EDGE_X, EDGE_Y) = (TREE_X, 0)`
    - right: `(EDGE_X, EDGE_Y) = (TREE_X, FOREST_WIDTH-1)`
    - if for up, down or left the tree is visible then break the loop and increments `visible_trees_counter`
- define `scenic_score(TREE_X,TREE_Y, FOREST_LENGTH, FOREST_WIDTH)`:
    - for a given tree `(TREE_X,TREE_Y)` count the number of smaller tree from its position toward a edge
        - if a taller tree is encountered then break the loop and compute the scenic score
        - for up: `reversed(range(TREE_X-1))`
        - for down: `range(TREE_X+1,FOREST_LENGTH-1))`
        - for left: `reversed(range(TREE_Y-1))`
        - for down: `range(TREE_Y+1,FOREST_WIDTH-1))`
    - do not include the trees on the edge 
