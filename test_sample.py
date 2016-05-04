import main
from sets import Set

def testWorld():

    assert main.get_list_neighbors(2, 2) == Set([(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)])
    assert main.get_list_neighbors(3, 3) == Set([(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)])

    main.set_alive(2, 2)
    main.set_alive(2, 3)
    main.set_alive(2, 4)
    main.set_alive(3, 2)
    main.set_alive(3, 4)
    assert main.get_num_alive_neighbors(3, 3) == 5

    main.set_dead(3, 4)
    assert main.get_num_alive_neighbors(3, 3) == 4

    assert main.is_underpopulated(3, 3) == False

    main.set_alive(6, 6)
    assert main.is_underpopulated(6, 6) == True

    main.set_alive(6, 7)
    assert main.is_survival(6, 6) == False

    main.set_alive(6, 5)
    assert main.is_survival(6, 6) == True

    main.set_alive(5, 5)
    assert main.is_survival(6, 6) == True

    main.set_alive(5, 6)
    assert main.is_survival(6, 6) == False

    assert main.is_overpopulated(6, 6) == True

    main.set_dead(5, 6)
    assert main.is_overpopulated(6, 6) == False

    main.set_dead(6, 6)
    assert main.is_birth(6, 6) == True

    main.set_dead(5, 5)
    assert main.is_birth(6, 6) == False

    assert main.next_state_is_alive(11, 11) == False

    main.set_alive(11, 11)
    assert main.next_state_is_alive(11, 11) == False

    main.set_alive(10, 10)
    assert main.next_state_is_alive(11, 11) == False

    main.set_alive(10, 11)
    assert main.next_state_is_alive(11, 11) == True

    main.set_alive(11, 12)
    assert main.next_state_is_alive(11, 11) == True

    main.set_dead(11, 11)
    assert main.next_state_is_alive(11, 11) == True

    main.set_alive(11, 11)
    main.set_alive(10, 12)
    assert main.next_state_is_alive(11, 11) == False

    main.reset_game()
    main.play([(1,1), (1,3), (2, 3), (2,4), (4,4)])



