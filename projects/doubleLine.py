import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

t = np.arange(0.,5.,0.2)
plt.title("Many Line")
# plt.hold(True)   # 인터프리터 방식에서 사용한다.
plt.plot(t,t,'r-.',label="1")
plt.plot(t,0.5*t**2,'bo:',label="2")
plt.plot(t,0.2*t**3,'g^-',label="3")
plt.legend(loc=2)
plt.show()