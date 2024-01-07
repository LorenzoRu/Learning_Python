word_to_guess = input()
word_partially_gues = input()
letter = input()

print(letter in word_to_guess and letter not in word_partially_gues)
