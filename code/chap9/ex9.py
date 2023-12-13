directory = {}
while True:
    name = input("Name ")
    if name != "stop":
        phone = input("Phone ")
        directory[name] = phone
    else:
        break
print(directory)