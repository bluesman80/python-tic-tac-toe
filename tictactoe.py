border = '---------'
pipe_begin = '| '
pipe_end = '|'
_O = 'O'
_X = 'X'
# Map the input coordinates to indices of the table
COORDINATES_MAP = {'1 3': 12, '2 3': 14, '3 3': 16,
                   '1 2': 22, '2 2': 24, '3 2': 26,
                   '1 1': 32, '2 1': 34, '3 1': 36}


def create_line(_input, begin_idx, end_idx):
    line = ""
    for i in range(begin_idx, end_idx):
        line += _input[i] + " "

    return line


def is_three_in_a_row(_input, stone):
    # Horizontal condition
    for i in range(12, 37, 10):
        if _input[i] == stone and (_input[i] == _input[i + 1] == _input[i + 2]):
            return True

    # Vertical condition
    for i in range(12, 37, 2):
        if _input[i] == stone and (_input[i] == _input[i + 10] == _input[i + 20]):
            return True

    # Diagonal condition. Check for the character in the middle first.
    if _input[24] == stone and (_input[24] == _input[12] == _input[36] or _input[24] == _input[16] == _input[32]):
        return True

    return False


def validate_move(_input, _move):
    if len(_move) != 3:
        return 'You should enter numbers!'

    new_move = list(i for i in _move.split())  # Example of expected move: ['1','2']
    for i in new_move:
        if not i.isdigit():
            return 'You should enter numbers!'
        elif int(i) > 3 or int(i) < 1:
            return 'Coordinates should be from 1 to 3!'

    # Check if the cell is empty
    if _input[COORDINATES_MAP[_move]] == _O or _input[COORDINATES_MAP[_move]] == _X:
        return 'This cell is occupied! Choose another one!'

    return 'valid'


def check_result(_input):
    result = 'continue'
    # Difference between the number of Xs and Os
    count_difference = abs(_input.count('X') - _input.count('O'))
    is_there_empty_cells = any(_input[i] for i in COORDINATES_MAP.values() if _input[i].isspace())

    if (is_three_in_a_row(_input, _X) and is_three_in_a_row(_input, _O)) or count_difference > 1:
        result = 'Impossible'
    elif is_three_in_a_row(_input, _X) and count_difference <= 1:
        result = 'X wins'
    elif is_three_in_a_row(_input, _O) and count_difference <= 1:
        result = 'O wins'
    elif not is_there_empty_cells and not is_three_in_a_row(_input, _X) and not is_three_in_a_row(_input, _O):
        result = "Draw"

    return result


def next_player(playa):
    if playa == _X:
        return _O
    else:
        return _X


table = '''---------
|       |
|       |
|       |
---------'''
# Print the initial state of the game
print(table)

# First player is X
player = _X

# Ask for a move and keep asking for it until there is a winner
# and continuously validate
while True:
    move = input('Enter the coordinates: > ').strip()
    validation_result = validate_move(table, move)
    if validation_result != 'valid':
        print(validation_result)
    else:
        # Place the stone to the coordinate and print the new state
        entry_list = [i for i in table]
        entry_list[COORDINATES_MAP[move]] = player
        table = ''.join(entry_list)
        # Print the state of the game
        print(table)

        status = check_result(table)
        if status == 'continue':
            player = next_player(player)
        else:
            print(status)
            break
