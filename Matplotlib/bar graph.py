from matplotlib import pyplot as plt

plt.bar([5,8,10,13,19],[12,16,6,17,18], label="Example One")
plt.bar([12,7,16,6,9],[14,19,17,12,4], label="Example Two", color='b')


plt.legend()
plt.ylabel("bar number")
plt.xlabel("bar number")

plt.title("The Data")

plt.show()
