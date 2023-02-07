list1 = [1,2,5,12,33,45,68,]
listOdd = []
listEven = []
for num in list1:
    if num%2 == 0:
        listEven.append(num)
    else:
        listOdd.append(num)
        #print lists
print(listEven)
print(listOdd)
