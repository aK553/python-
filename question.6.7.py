import time
from datetime import datetime
dat=datetime.now()
dat1 = dat.weekday()
if dat1 == 0:
    print("monday!")
elif dat1 == 1:
    print("tuesday!")
elif dat1 == 2:
    print("wednesday!")
elif dat1 == 3:
    print("thursday!")
elif dat1 == 4:
    print("friday!")
elif dat1 == 5:
    print("saturday!")
else:
    print("sunday!")

