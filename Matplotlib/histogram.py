from matplotlib import pyplot as plt

population_ages = [22,34,54,23,21,27,55,67,89,120,112,78,90,56,12,]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Histogram")
plt.legend()
plt.show()

