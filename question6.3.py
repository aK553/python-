count=1#initilaize the count as 1,there should be minimum one value in the tuple
tuples = (50,60,10,50,50,70,50,60)
for data in range(0,len(tuples)):
    if tuples[data] == tuples[data-1]:
      count = count + 1
print(f' Reapeated number count is : {count}')

