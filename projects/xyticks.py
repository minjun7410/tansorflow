import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
plt.title("xyticks")
plt.plot(X,C)
plt.xticks([-np.pi,-np.pi / 2, 0 , np.pi / 2,np.pi])
plt.yticks([-1,0,+1],["Low","Zero","High"])
plt.show()