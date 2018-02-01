# setting up the soduku board
from utils import *

test_string = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
all_digits = '123456789'

def assign_grid(board_values):
    """assign initial values to grid spaces"""
    values = []
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

# print(eliminate(assign_grid(test_string)))

def only_values(values):
    """iterate over boxes, and assign any values that are only possible for a box"""
    for unit in unitlist:
        digits = {}
        for digit in all_digits:
            digit_boxes = [];
            for box in unit:
                if digit in values[box]:
                    digit_boxes.append(box)
            if len(digit_boxes) == 1:
                values[digit_boxes[0]] = digit
    return values

grid = assign_grid(test_string)
eliminated = eliminate(grid)
print(only_values(eliminated))
