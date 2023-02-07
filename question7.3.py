import matplotlib.pyplot as plt
month =[1,2,3,4,5,6,7,8,9]
sale = [1000,1700,1400,1500,1700,1850,190,1650,200]
plt.bar(month,sale)
plt.title("bathingsoap sales data")
plt.xlabel("month number")
plt.ylabel("sales units in number")
plt.grid(linestyle = "--")
plt.tight_layout()
plt.show()

