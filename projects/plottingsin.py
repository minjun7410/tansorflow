import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
t=np.arange(-1*np.pi, 1*np.pi, 0.02)
y = np.sin(t)
plt.plot(t,y)
plt.grid(True)
plt.show()
