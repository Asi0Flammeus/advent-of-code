def move_tail(head, tail):
    # check if the head and tail are already touching
    if is_touching(head, tail):
        return tail

    # compute the displacement between the head and tail
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    # move the tail one step towards the head
    if dx == 0 or dy == 0:
        # case 1: tail is on the same row or column as head
        tail = (tail[0] + sign(dx), tail[1] + sign(dy))
    else:
        # case 2: tail is not on the same row or column as head
        # move diagonally towards the head
        tail = (tail[0] + sign(dx), tail[1] + sign(dy))

    return tail

def is_touching(p1, p2):
    # check if two points are touching by checking if they have a common neighbor
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for n in neighbors:
        if (p1[0] + n[0], p1[1] + n[1]) == p2:
            return True
    return False

def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

