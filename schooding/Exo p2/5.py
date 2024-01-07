numbers = input()
numbers_list = numbers.split(',')
counter = 0

for i in numbers_list:
    i = int(i)
    if i >= 10:
        counter += 1

print(counter)
