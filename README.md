# [Learning/EMLV]-Python

## [Chap_8]-List

### Exercise 1

```Python
my_list = []
while True:
    item = input("items: ")
    if item != "stop":
        my_list.append(item)
    else:
        break
print(my_list)
```

## [Chap_9]-List

### Exercise 1
```Python 
directory = {}
while True:
    name = input("Name ")
    if name != "stop":
        phone = input("Phone ")
        directory[name] = phone
    else:
        break
print(directory)
```