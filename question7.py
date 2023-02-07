import matplotlib.pyplot as plt
month = [1,2,3,4,5,6,7,8,9]
profit=[200000,170000,240000,250000,250000,230000,370000,210000,250000]
plt.plot(month,profit)
plt.title('company profit per month')
plt.xlabel('month number')
plt.ylabel('total profit')
plt.tight_layout()
plt.show()
