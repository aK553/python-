import time
b = time.strftime("%m/%d/%Y")
print(type(b))
print(time.strptime(b,"%m/%d/%Y"))

