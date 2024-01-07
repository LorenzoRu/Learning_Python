initial_location = input()
final_location = input()

initial_row = int(initial_location[1:])
initial_col = initial_location[0].upper()
final_row = int(final_location[1:])
final_col = final_location[0].upper()

field = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8
}

def valid_cell(col, row):
    return col in field and 1 <= row <= 8

def move_checker(initial_location, final_location):
    initial_col, initial_row = initial_location[0].upper(), int(initial_location[1:])
    final_col, final_row = final_location[0].upper(), int(final_location[1:])

    if not valid_cell(initial_col, initial_row) or not valid_cell(final_col, final_row):
        return "impossible"

    if abs(field[initial_col] - field[final_col]) == abs(initial_row - final_row):
        return True
    else:
        return False

print(move_checker(initial_location, final_location))
