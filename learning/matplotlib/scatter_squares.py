import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9, 16,25]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=50)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)


plt.show()
