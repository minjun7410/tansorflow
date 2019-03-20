import numpy as np
import matplotlib.pyplot as plt
'''
x = np.arange(-8,9,1)
y1 = np.exp(x)/2
y2 = np.exp(-x)/2
y3 = y1 - y2

plt.figure(1)
plt.plot(x,y3)
plt.xlabel('x')
plt.ylabel('sinh')
plt.title('sinh')
plt.grid(True)
plt.show()'''

x = np.arange(-8,9,0.5)
y1 = np.exp(x)/2
y2 = np.exp(-x)/2
y3 = y1 + y2

plt.figure(1)
plt.plot(x,y3,'ko-')
plt.xlabel('x')
plt.ylabel('conh')
plt.title('Cosh')
plt.grid(True)
plt.show()
