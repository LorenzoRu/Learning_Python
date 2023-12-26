my_list = []
while True:
    item = input("what do you want to do? (press a to add, r to remove and s to stop)")
    match item:
        case "a":
            item = input("item to add: ")
            my_list.append(item)
        case "r":
            item = input("item to remove: ")
            my_list.remove(item)
        case "s":
            break
        case _:
            print("invalid input")
print(my_list)