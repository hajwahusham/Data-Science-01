import matplotlib.pyplot as plt  

# not real data

april = [27, 16, 26, 14, 7, 14, 19, 21, 2, 30, 31, 22, 7, 21, 10, 10, 14, 1, 25, 34, 10, 27, 22, 11, 3, 6, 8, 7]
may = [9, 2, 8, 12, 9, 27, 1, 3, 5, 14, 21, 32, 10, 23, 22, 21, 20, 24, 1, 28, 14, 31, 20, 10, 30, 21, 14, 18, 7, 2, 5, 6, 19, 9, 8]
june = [2, 3, 4, 2, 22, 3, 39, 3, 7, 26, 18, 17, 13, 20, 1, 25, 3, 32, 1, 10, 24, 18, 19, 27, 10]

rainfall = [april, may, june]
colors = ['c', 'r', 'm']
label = ['April', 'May', 'June']
bins = [0, 5, 10, 15, 20, 25, 30, 35]
plt.xlabel("average rainfall / mm")
plt.ylabel("no. of years")


plt.hist(rainfall, bins=bins, color=colors, 
         label=label, width=1.0)

plt.title("rainfall chart")
plt.legend()
plt.show()