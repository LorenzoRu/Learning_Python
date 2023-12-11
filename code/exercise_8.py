my_list = []
while True:
    item = input("items: ")
    if item != "stop":
        my_list.append(item)
    else:
        break
print(my_list)