# setting up the soduku board
import pprint
pp = pprint.PrettyPrinter()
from utils import *

test_string = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
another_string = '..3.2.6..9..3.5..1...8..4....81.29..7.......8..6..82.....6.95..8..2.3..9..5.1.3..'
harder_string = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
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

def only_choice(values):
    """iterate over boxes, and assign any values that are only possible for a box"""
    for unit in unitlist:
        for digit in all_digits:
            digit_boxes = [];
            for box in unit:
                if digit in values[box]:
                    digit_boxes.append(box)
            if len(digit_boxes) == 1:
                values[digit_boxes[0]] = digit
    return values

def count_boxes(values, desired_count):
    """boxes with specified available values remaining"""
    boxes_with_value_count = [box for box in values.keys() if len(values[box]) == desired_count]
    return len(boxes_with_value_count)

def reduce_puzzle(values):
    stalled_or_solved = False
    while not stalled_or_solved:
        solved_values_before = count_boxes(values, 1)
        eliminate(values)
        only_choice(values)
        solved_values_after = count_boxes(values, 1)
        stalled_or_solved = solved_values_before == solved_values_after or solved_values_after == 81
        print(stalled_or_solved)
        if count_boxes(values, 0) > 0:
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    pp.pprint(values)
    if values == False:
        return False
    if all(len(values[box]) == 1 for box in values):
        print('solved')
        return values # if all boxes have 1 value, puzzle is solved
    unsolved_boxes = [box for box in values if len(values[box]) > 1]
    print('unsolved boxes', unsolved_boxes)
    # closest_unsolved_box = min([box for ])


grid = assign_grid(another_string)
search(grid)
