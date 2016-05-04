from sets import Set


def reset_game():
    known_cells = {}


def get_list_neighbors(x, y):
    returnable = Set()
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (i == x and j ==y):
                returnable.add((i, j))
    return returnable


def is_alive(x, y):
    if (x, y) in known_cells:
        return known_cells[(x, y)]
    else:
        return False


def set_alive(x, y):
    known_cells[(x, y)] = True


def set_dead(x, y):
    known_cells[(x, y)] = False


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
    if is_alive(x, y) and (get_num_alive_neighbors(x, y) ==2 or get_num_alive_neighbors(x, y) == 3):
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


def play(list_of_alive_indices):

    for xy in list_of_alive_indices:
        set_alive(xy[0], xy[1])

    print_board()
    new_state = {}

    global known_cells
    for xy in known_cells:
        if next_state_is_alive(xy[0], xy[1]):
            new_state[(xy[0], xy[1])] = True
        else:
            new_state[(xy[0], xy[1])] = False
    print "--------------------------------------------------"
    known_cells = new_state
    print_board()



def print_board():
    if len(known_cells) ==0:
        print "empty board"
    else:
        min_x = reduce(lambda x1, x2: x1 if x1 < x2 else x2, map(lambda xy: xy[0], known_cells.keys()) )
        max_x = reduce(lambda x1, x2: x1 if x1 > x2 else x2, map(lambda xy: xy[0], known_cells.keys()) )
        min_y = reduce(lambda x1, x2: x1 if x1 < x2 else x2, map(lambda xy: xy[1], known_cells.keys()) )
        max_y = reduce(lambda x1, x2: x1 if x1 > x2 else x2, map(lambda xy: xy[1], known_cells.keys()) )

        for i in range(min_x, max_x +1):
            for j in range(min_y, max_y +1):
                if (i, j) in known_cells and known_cells[(i, j)]:
                    print "1",
                else:
                    print "0",
            print ""


play([(1,1), (1,3), (2, 3), (2,4), (4,4)])