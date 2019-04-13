import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

np.random.seed(0)

plt.subplot(2,2,1)#행이 2 열이 2 그중 첫번째
plt.plot(np.random.rand(5))
plt.title("1")
plt.subplot(2,2,2)#동시에 fig , axes =
# plt.subplots(2[행],2[열])이라고 먼저 선언헐 수있다.
plt.plot(np.random.rand(5))
plt.title("2")
plt.subplot(2,2,3)
plt.plot(np.random.rand(5))
plt.title("3")
plt.subplot(2,2,4)
plt.plot(np.random.rand(5))
plt.title("4")
plt.tight_layout()#간격 맞추기
plt.show()