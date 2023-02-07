fn = open('file.txt','r')
count=0
fn1 = open('nfile.txt','w')
for data in fn:
    count = count + 1  
    print(count)
    if count == 5:
        continue
    else:
     fn1.write(data)

