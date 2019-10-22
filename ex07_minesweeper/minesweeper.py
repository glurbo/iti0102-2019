"""Minesweeper has to swipe the mines."""
import copy


def create_minefield(height: int, width: int) -> list:
    """
    Create and return minefield.

    Minefield must be height high and width wide. Each position must contain single dot (`.`).
    :param height: int
    :param width: int
    :return: list
    """
    minefield = [["." for _ in range(width)]for _ in range(height)]
    return minefield


def add_mines(minefield: list, mines: list) -> list:
    """
    Add mines to a minefield and return minefield.

    This function cannot modify the original minefield list.
    Minefield must be length long and width wide. Each non-mine position must contain single dot.
    If a position is empty ("."), then a small mine is added ("x").
    If a position contains small mine ("x"), a large mine is added ("X").
    Mines are in a list.
    Mine is a list. Each mine has 4 integer parameters in the format [N, S, E, W].
        - N is the distance between area of mines and top of the minefield.
        - S ... area of mines and bottom of the minefield.
        - E ... area of mines and right of the minefield.
        - W ... area of mines and left of the minefield.
    :param minefield: list
    :param mines: list
    :return: list
    """
    minefield = copy.deepcopy(minefield)
    for mine in mines:
        for rowi in range(mine[0], len(minefield) - mine[1]):
            for coli in range(mine[3], len(minefield[rowi]) - mine[2]):
                if minefield[rowi][coli] == ".":
                    minefield[rowi][coli] = "x"
                elif minefield[rowi][coli] == "x":
                    minefield[rowi][coli] = "X"
    return minefield


def get_minefield_string(minefield: list) -> str:
    """
    Return minefield's string representation.

    .....
    .....
    x....
    Xx...

    :param minefield:
    :return:
    """
    minefield_string = "\n".join("".join(sub) for sub in minefield)
    return str(minefield_string)


def count_bombs_for_cell(minefield, row, col) -> int:
    """
    Count the number of mines in each cell's surroundings and outputs the number of mines.

    :param minefield:
    :param row:
    :param col:
    :return:
    """
    count = 0
    for rowi in range(row - 1, row + 2):
        for coli in range(col - 1, col + 2):
            if 0 <= rowi < len(minefield):
                if 0 <= coli < len(minefield[row]):
                    if minefield[rowi][coli] in ("x", "X"):
                        count += 1
    return count


def calculate_mine_count(minefield: list) -> list:
    """
    For each cell in minefield, calculate how many mines are nearby.

    This function cannot modify the original list.
    So, the result should be a new list (or copy of original).

    ....
    ..x.
    X.X.
    x..X

    =>

    0111
    13x2
    X4X3
    x32X

    :param minefield:
    :return:
    """
    minefield = copy.deepcopy(minefield)
    for rowi in range(len(minefield)):
        for coli in range(len(minefield[rowi])):
            if minefield[rowi][coli] == ".":
                minefield[rowi][coli] = str(count_bombs_for_cell(minefield, rowi, coli))

    return minefield


def get_position(minefield):
    """
    Find the position of #.

    :param minefield:
    :return:
    """
    for rowi in range(0, len(minefield)):
        for coli in range(0, len(minefield[rowi])):
            if minefield[rowi][coli] == "#":
                return rowi, coli


def get_new_position(minefield, move, row, col):
    """
    Get new position for #.

    :param move:
    :param row:
    :param col:
    :return:
    """
    newrow, newcol = row, col
    if move == "N":
        if row in range(1, row):
            newrow = row - 1
    elif move == "S":
        if row in range(0, len(minefield) - 1):
            newrow = row + 1
    elif move == "E":
        if col in range(0, len(minefield[row])):
            newcol = col + 1
    elif move == "W":
        if col in range(1, col):
            newcol = col - 1
    return newrow, newcol


def walk(minefield, moves, lives) -> list:
    """
    Make moves on the minefield.

    This function cannot modify the original minefield list.
    Starting position is marked by #.
    There is always exactly one # on the field.
    The position you start is an empty cell (".").

    Moves is a list of move "orders":
    N - up,
    S - down,
    E - right,
    W - left.

    Example: "NWWES"

    If the position you have to move contains "x" (small mine),
    then the mine is cleared (position becomes "."),
    but you cannot move there.
    In case of clearing a small mine, ff the position where the minesweeper is, has 5 or more mines nearby
    (see the previous function), minesweeper also loses a life.
    If it has 0 lives left, then clearing is not done and moving stops.

    Example:
    #x
    ..
    moves: ESS

    =>

    1st step ("E"):
    #.
    ..

    2nd step ("S"):
    ..
    #.

    3rd step ("S"):
    ..
    #.

    Example #2
    XXX
    x.x
    .#X
    moves: NWES, lives = 1

    1) "N"
    XXX
    x#x
    ..X

    2) "W". the small mine is cleared, but with the cost of one life :'(
    XXX
    .#x
    ..X
    lives = 0

    3) "E"
    XXX
    .#x
    ..X
    As clearing the mine on the right, he would lose a life (because minesweeper has 5 or more mines nearby).
    But as he has no lives left, he stops there. No more moves will be carried out.

    If the position you have to move contains "X" (huge mine),
    then you move there and lose a life.

    #X
    ..
    moves: ESS

    1) (lives = lives - 1)
    .#
    ..
    2)
    ..
    .#
    3)
    ..
    .#

    If you have to move into a position with a huge mine "X"
    but you don't have any more lives, then you finish your moves.

    lives: 2

    #XXXX
    .....
    moves: EEES

    1) lives = 1
    .#XXX
    .....
    2) lives = 0
    ..#XX
    .....
    3) stop, because you would die
    final result:
    ..#XX
    .....

    :param minefield:
    :param moves:
    :param lives:
    :return:
    """
    minefield = copy.deepcopy(minefield)
    row, col = get_position(minefield)
    minefield[row][col] = "."

    for move in moves:
        newrow, newcol = get_new_position(minefield, move, row, col)
        if minefield[newrow][newcol] == ".":
            row, col = newrow, newcol
        elif minefield[newrow][newcol] == "x":
            minefield[newrow][newcol] = "."
            if count_bombs_for_cell(minefield, row, col) < 5:
                continue
            else:
                lives = lives - 1
            if lives == 0:
                break
        elif minefield[newrow][newcol] == "X":
            minefield[newrow][newcol] = "."
            row, col = newrow, newcol
            lives = lives - 1
            if lives == 0:
                break
    minefield[row][col] = "#"
    return minefield


if __name__ == '__main__':
    minefield_a = create_minefield(4, 3)
    print(minefield_a)  # ->
    """
    [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    """

    minefield_a = add_mines(minefield_a, [[0, 3, 2, 0], [2, 1, 0, 1]])
    print(minefield_a)  # ->
    """
    [
        ['x', '.', '.'],
        ['.', '.', '.'],
        ['.', 'x', 'x'],
        ['.', '.', '.']
    ]
    """

    print(get_minefield_string(minefield_a))
    minefield_ac = calculate_mine_count(minefield_a)
    print(get_minefield_string(minefield_ac))

    minefield_b = create_minefield(8, 7)
    minefield_b = add_mines(minefield_b, [[2, 1, 3, 2], [0, 5, 3, 0]])

    print(minefield_b)  # ->
    """
    [
        ['x', 'x', 'x', 'x', '.', '.', '.'],
        ['x', 'x', 'x', 'x', '.', '.', '.'],
        ['x', 'x', 'X', 'X', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']
    ]
    """

    minefield_c = create_minefield(5, 5)
    minefield_c = add_mines(minefield_c, [[0, 0, 2, 2]])
    print(minefield_c)  # ->
    """
    [
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.']
    ]
    """

    mf = [['.', '.', '.', '.'], ['.', '.', 'x', '.'], ['X', '.', 'X', '.'], ['x', '.', '.', 'X']]
    print(calculate_mine_count(mf))

    """
    [
        ['0', '1', '1', '1'],
        ['1', '3', 'x', '2'],
        ['X', '4', 'X', '3'],
        ['x', '3', '2', 'X']
    ]
    """

    mf = copy.deepcopy(minefield_c)
    mf[0][0] = '#'
    print(get_minefield_string(walk(mf, "WEESE", 2)))
    """
    .....
    .#...
    ..x..
    ..x..
    ..x..
    """

    mf = create_minefield(3, 5)
    mf = add_mines(mf, [[0, 0, 1, 2]])
    mf = add_mines(mf, [[0, 1, 1, 1]])
    print(get_minefield_string(mf))
    """
.xXX.
.xXX.
..xx.
    """
    mf[0][4] = "#"
    mf = walk(mf, "WSSWN", 2)
    print(get_minefield_string(mf))
    """
.xX..
.xX#.
..x..
    """
    # minesweeper would die if stepping into the mine, therefore he stops
