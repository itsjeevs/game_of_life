from sets import Set


def get_list_neighbors(x, y):
    returnable = Set()
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (i == x and j ==y):
                returnable.add((i, j))
    return returnable


def is_alive(x, y):
    if (x, y) in knownCells:
        return knownCells[(x, y)]
    else:
        return False


def set_alive(x, y):
    knownCells[(x,y)] = True


def set_dead(x, y):
    knownCells[(x, y)] = False


def get_num_alive_neighbors(x,y):
    num_alive_neighbors = 0
    for neighbor in get_list_neighbors(x,y):
        if is_alive(neighbor[0], neighbor[1]):
            num_alive_neighbors += 1

    return num_alive_neighbors


def is_underpopulated(x, y):
    if is_alive(x, y) and get_num_alive_neighbors(x, y) < 2:
        return True
    else:
        return False


def is_survival(x, y):
    if is_alive(x, y) and (get_num_alive_neighbors(x, y) ==2 or get_num_alive_neighbors(x, y) ==3 ):
        return True
    else:
        return False


def is_overpopulated(x, y):
    if is_alive(x, y) and get_num_alive_neighbors(x, y) > 3:
        return True
    else:
        return False


def is_birth(x, y):
    if not is_alive(x,y) and get_num_alive_neighbors(x,y) ==3:
        return True
    else:
        return False


def next_state_is_alive(x,y):
    if is_alive(x, y):
        if is_underpopulated(x, y) or is_overpopulated(x, y):
            return False
        else:
            return True
    else:
        if is_birth(x, y):
            return True
        else:
            return False

def reset_game():

knownCells = {}

