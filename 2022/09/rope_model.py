def move_tail(head, tail):
    # check if the head and tail are already touching
    if is_touching(head, tail):
        return tail

    # compute the displacement between the head and tail
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    tail = (tail[0] + sign(dx), tail[1] + sign(dy))

    return tail

def move_knots(head, knots):
    # check if the knots are already touching
    if is_touching(head, knots[0]):
        return knots

    # move the first knot towards the head
    dx = head[0] - knots[0][0]
    dy = head[1] - knots[0][1]
    knots[0] = (knots[0][0] + sign(dx), knots[0][1] + sign(dy))

    # move each knot towards the one in front of it
    for i in range(1, len(knots)):
        if not is_touching(knots[i],knots[i-1]):
            dx = knots[i-1][0] - knots[i][0]
            dy = knots[i-1][1] - knots[i][1]
            knots[i] = (knots[i][0] + sign(dx), knots[i][1] + sign(dy))

    return knots

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

