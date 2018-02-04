
rows = 'ABCDEFGHI'
rows_reversed = ''.join(reversed(rows))
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
# create and add diagonal units as array of keys
first_diagonal = []
second_diagonal = []
for x in range(0,9):
    first_diagonal.append(rows[x] + cols[x])
    second_diagonal.append(rows_reversed[x] + cols[x])
unitlist = row_units + column_units + square_units + [first_diagonal] + [second_diagonal]
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
