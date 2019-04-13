import numpy as np
import matplotlib.pyplot as plt
t = np.arange(-2*np.pi , 2*np.pi , 0.5)
y1 = np.sin(t)
y2 = np.cos(t)
plt.subplot(2,1,1)
plt.plot(t, y1,'ko-')
plt.title('2 subplots')
plt.xlabel('time')
plt.ylabel('sine')
plt.grid(True)
plt.show()