import numpy as np

data = np.loadtxt('./day_2_input.txt',dtype=str)
Nbr_round = len(data[:,0])
print(Nbr_round)
ScoreOutcome = np.zeros((Nbr_round,2))

def my_outcome(your_move,my_move):

    if your_move == "A": # you play rock
        if my_move == "X": # draw with rock
            return [3,1]
        elif my_move == "Y": # win with paper
            return [6,2]
        elif my_move == "Z": # lose with scissors
            return [0,3]

    elif your_move == "B": # you play paper
        if my_move == "X": # lose with rock
            return [0,1]
        elif my_move == "Y": # draw with paper
            return [3,2]
        elif my_move == "Z": # win with scissors
            return [6,3]

    elif your_move == "C": # you play scissors
        if my_move == "X": # win with rock
            return [6,1]
        elif my_move == "Y": # lose with paper
            return [0,2]
        elif my_move == "Z": # draw with scissors
            return [3,3]

def proposed_move(your_move,outcome):

    if your_move == "A": # you play rock
        if outcome == "X": # I lose
            return [0,3]
        elif outcome == "Y": # it's a draw
            return [3,1]
        elif outcome == "Z": # I win 
            return [6,2]

    elif your_move == "B": # you play paper
        if outcome == "X": # I lose
            return [0,1]
        elif outcome == "Y": # it's a draw
            return [3,2]
        elif outcome == "Z": # I win 
            return [6,3]

    elif your_move == "C": # you play scissors
        if outcome == "X": # I lose
            return [0,2]
        elif outcome == "Y": # it's a draw
            return [3,3]
        elif outcome == "Z": # I win 
            return [6,1]

for i in range(Nbr_round):
    ### first plan
    #ScoreOutcome[i,:] = my_outcome(data[i,0],data[i,1])

    ### Real plan 
    ScoreOutcome[i,:] = proposed_move(data[i,0],data[i,1])

print(ScoreOutcome)
print(sum(sum(ScoreOutcome)))
