keys = ['ten','twenty','thirty']
values = [10,20,30]
dic= dict()
for data in range(len(keys)):
    dic.update({keys[data]: values[data]})
print(dic)
