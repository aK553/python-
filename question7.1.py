import matplotlib.pyplot as plt
month = [1,2,3,4,5,6,7,8,9]
sale= [1000,1700,1400,1500,1700,1850,190,1650,2000]
sale1= [1800,3000,400,2500,1950,1800,1750,1750,1800]
sale2= [1900,1900,2400,3500,4000,1950,1600,1800,1900]
sale3= [2000,2700,3400,1900,2000,1800,1760,1900,2400]
plt.plot(month,sale, marker = '*',ms = 10,label = "line 1")
plt.plot(month,sale1, marker = '*',ms = 10,label = "line 2")
plt.plot(month,sale2, marker = '*',ms = 10,label = "line 3")
plt.plot(month,sale3, marker = '*',ms = 10,label = "line 4")
plt.legend()
plt.xlabel("month number")
plt.ylabel("total profit")
plt.tight_layout()
plt.show()
