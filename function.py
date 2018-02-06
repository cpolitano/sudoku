# setting up the soduku board
from utils import *

test_string = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
another_string = '..3.2.6..9..3.5..1...8..4....81.29..7.......8..6..82.....6.95..8..2.3..9..5.1.3..'
harder_string = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
diagonal_string = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
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

def eliminate(values):
    """iterate over all boxes, and for any box with only one value, remove that value from all peer boxes"""
    solved_values = [box for box in values.keys() if len(values[box]) == 1] # select boxes with one digit
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values

def naked_twins(values):
    doubles_values = [box for box in values.keys() if len(values[box]) == 2] # select boxes with two digits
    # evaluate units of each double to check for twins
    for double in doubles_values:
        twin = values[double] # ex 23, 45, 53
        for unit in units[double]:
            twin_exists = False
            for box in unit:
                if values[box] == twin:
                    twin_exists = True
                    break
            if twin_exists:
                for box in unit:
                    potential_twin = values[box]
                    first_twin = twin[0]
                    second_twin = twin[1]
                    # match 27 and 2347
                    if any(digit == first_twin for digit in potential_twin) and any(digit == second_twin for digit in potential_twin) and potential_twin != twin:
                        # remove twins from all other unit boxes
                        print('replacing twin', potential_twin, twin)
                        values[box] = values[box].replace(first_twin, '')
                        values[box] = values[box].replace(second_twin, '')
    return values

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
        naked_twins(values)
        only_choice(values)
        solved_values_after = count_boxes(values, 1)
        stalled_or_solved = solved_values_before == solved_values_after or solved_values_after == 81
        print(stalled_or_solved)
        if count_boxes(values, 0) > 0:
            print('empty boxes')
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if values == False:
        return False
    if all(len(values[box]) == 1 for box in values):
        print('solved!')
        return values # if all boxes have 1 value, puzzle is solved
    unsolved_boxes = [box for box in values if len(values[box]) > 1]
    box_count, closest_unsolved_box = min((len(values[box]), box) for box in unsolved_boxes)
    for value in values[closest_unsolved_box]:
        sudoku_attempt = values.copy()
        sudoku_attempt[closest_unsolved_box] = value
        solved_puzzle = search(sudoku_attempt)
        print(solved_puzzle)
        if solved_puzzle:
            print('solved!')
            return solved_puzzle


grid = assign_grid(diagonal_string)
search(grid)
# naked_twins(before_naked_twins_1)
