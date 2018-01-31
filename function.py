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
    assert len(board_values) == 81
    counter = 0
    for unit in range(0,8):
        row_boxes = board[unit]
        for box in row_boxes:
            values[box] = board_values[counter]
            counter += 1
    return values

grid = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..');
print(grid)
