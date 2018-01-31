# setting up the soduku board

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

def create_board():
    boxes = cross(rows, cols)
    row_units = [cross(r, cols) for r in rows]
    column_units = [cross(rows, c) for c in cols]
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    unitlist = row_units + column_units + square_units
    return unitlist

def grid_values(board_values):
    values = {}
    board = create_board()
    if len(board) == len(board_values):
        counter = 0
        for b in board:
            values[b] = board_values[counter]
            counter++
    else:
        raise ValueError('invalid board values. pls do better')
    return values
