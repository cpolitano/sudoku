# setting up the soduku board
from utils import *

test_string = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def assign_grid(board_values):
    """assign initial values to grid spaces"""
    values = []
    all_digits = '123456789'
    for number in board_values:
        if number == '.':
            values.append(all_digits)
        elif number in all_digits:
            values.append(number)
    assert len(values) == 81
    return dict(zip(boxes, values))

# print(assign_grid(test_string))

def eliminate(values):
    """iterate over all boxes, and for any box with only one value, remove that value from all peer boxes"""
    solved_values = [box for box in values.keys() if len(values[box]) == 1] # select boxes with one digit
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values

print(eliminate(assign_grid(test_string)))
