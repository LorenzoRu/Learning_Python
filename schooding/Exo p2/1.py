initial_location =  input ("Entrez la position du cavalier (ex: A1): ")
final_location = input ("Entrez la position finale du cavalier (ex: B3): ")
initial_location = list(initial_location)
final_location = list(final_location)

def move_cheker (initial_location, final_location):
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
   intial_row = int(initial_location[1])
   intial_col = field[initial_location[0]]
   diff_row = int(final_location[1]) - intial_row
   diff_col = field[final_location[0]] - intial_col
   return (diff_row == 2 and diff_col == 1) or (diff_row == 1 and diff_col == 2) or (diff_row == -2 and diff_col == -1) or (diff_row == -1 and diff_col == -2) or (diff_row == 2 and diff_col == -1) or (diff_row == 1 and diff_col == -2) or (diff_row == -2 and diff_col == 1) or (diff_row == -1 and diff_col == 2)

print(move_cheker(initial_location, final_location))



