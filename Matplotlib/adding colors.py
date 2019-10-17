from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x1 = [5,8,10]
y1 = [12,16,6]

x2 = [12,7,16]
y2 = [14,19,17]



plt.plot(x1,y1, 'g', label='LineOne', linewidth=5)
plt.plot(x2,y2, 'r', label='LineTwo', linewidth=5)

plt.title("Info")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")

plt.grid(True, color='K')

plt.legend()

plt.show()