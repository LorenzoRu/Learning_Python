number_list = [2, 20, 6, 7, 15, 13, 3]
number_list.sort()
print("minimum : ")
print(number_list[0])
print("maximum : ")
print(number_list[-1])


#madinane
if len(number_list)%2 == 1:
    print("médiane pour un nb impaire : ")
    print(number_list[len(number_list)//2])

else : 
    print("médiane pour un nb paire : ")
    print((number_list[len(number_list)//2] + number_list[len(number_list)//2-1])/2)