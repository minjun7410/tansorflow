import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-2*np.pi , 2*np.pi , 0.5)

y1 = np.sin(t)
y2 = np.cos(t)

plt.subplot(2,1,1)
plt.plot(t,y1,'ko-')
plt.title("sin")
plt.xlabel('time')
plt.ylabel('Sin')
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t,y2,'r.-')
plt.xlabel('time (s)')
plt.ylabel('Cos')
plt.grid(True)
plt.show()
