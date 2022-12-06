## DAY 2 -- ROCK PAPER SCISSORS 

To decide which elves would be closest to the snack tent, a giant RoPaSci is organized. 
Some well-inclined elf want you to win.
Thus the input.txt, a encrypted strategy guide. 
You have to decode it to win. 
What would be your total score with this strategy guide ? 


### SCORE COMPUTATION

- outcome score 
    - a win = +6
    - a draw = +3
    - a lose = +0
- move score 
    - rock = +1 
    - paper = +2 
    - scissors = +3 

### INPUT

each line encrypts the stategy to follow for a round
- 1st column : 
    - Rock = A 
    - Paper = B
    - Scissors = C
- at first sight you thought that 2nd column was :
    - Rock = X
    - Paper = Y
    - Scissors = Z
- yet it's finally:
    - get a lose = X
    - get a draw = Y
    - get a win = Z
 
### SOLVING METHO
- with `np.loadtxt` parse the input.txt and define the score associated to each round
- `my_outcome(your_move,my_move)`: compute the score based on the 1st interpretation of the 2nd column
- `proposed_move(your_move,outcome)`: compute the score based on the 2nd interpretation of the 2nd column





