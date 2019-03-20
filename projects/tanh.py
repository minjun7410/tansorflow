import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-8,9,1)
y1 = np.exp(x)/2
y2 = np.exp(-x)/2
y3 = y1 - y2
y4 = y1 + y2
y5 = y3/y4
plt.figure(1)
plt.plot(x,y5)
plt.xlabel('x')
plt.ylabel('tanh')
plt.title('tanh')
plt.grid(True)
plt.show()
