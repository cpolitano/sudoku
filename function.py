# setting up the soduku board

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
print(row_units)

column_units = [cross(rows, c) for c in cols]
print(column_units)

square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
print(square_units)

unitlist = row_units + column_units + square_units
