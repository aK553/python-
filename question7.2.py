import matplotlib.pyplot as plt
month = [1,2,3,4,5,6,7,8,9]
sale=[1000,1700,1400,1500,1700,1850,190,1650,2000]
sale1=[1800,3000,400,2500,1950,1800,1750,1750,1800]
plt.subplot(2,1,1)
plt.plot(month,sale,label = "line 1",color = "b",marker = 'o')
plt.title("sale data of a bathing soap")
plt.legend()
plt.subplot(2,1,2)
plt.plot(month,sale1,label = "line 2",color = "r",marker = 'o')
plt.title("sale data of a face wash")
plt.legend()
plt.xlabel("month number")
plt.ylabel("total profit")
plt.tight_layout()
plt.show()


