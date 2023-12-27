initial_position = input("Entrez la position de la tour (ex: A1): ")
final_position = input("Entrez la position finale de la tour (ex: H1): ")
initial_position = list(initial_position)
final_position = list(final_position)

def move_cheker(initial_position, final_position):
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
    intial_row = int(initial_position[1])
    intial_col = field[initial_position[0]]
    final_row = int(final_position[1])
    final_col = field[final_position[0]]
    return intial_row == final_row or intial_col == final_col

print(move_cheker(initial_position, final_position))