def update_partially_guessed_word(word_to_guess, partially_guessed_word, letter):
    updated_word = ""

    for i in range(len(word_to_guess)):
        if partially_guessed_word[i] == '*':
            if word_to_guess[i] == letter:
                updated_word += letter
            else:
                updated_word += '*'
        else:
            updated_word += partially_guessed_word[i]

    return updated_word


word_to_guess = input()
partially_guessed_word = input()
letter = input()

result = update_partially_guessed_word(word_to_guess, partially_guessed_word, letter)


print(result)
