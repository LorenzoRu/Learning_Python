numbers_list = []

while True:
    number = input("Entrez un nombre (tapez ! pour arrêter le programme ): ")
    if number == "!":
        for i in numbers_list:
            def sum(numbers_list):
                total = 0
                length = len(numbers_list)
                for i in range(length):
                    total += int(numbers_list[i])
                return total
        print(sum(numbers_list))
        break
    else:
        numbers_list.append(number)