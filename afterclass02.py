import matplotlib.pyplot as plt  
import numpy as np

x = np.arange(0,10,1)
y1 = (x+2)**2
y2 = (x**2) +2

plt.plot(x, y1, linestyle='dashed', marker='8', label= 'y=(x+2)^2')
plt.plot(x, y2, linestyle='dashdot', marker='*', label= 'y=(x^2)+2')

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.legend()
plt.show()