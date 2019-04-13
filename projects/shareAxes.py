import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

fig , ax0 = plt.subplots()
ax1 = ax0.twinx()
ax0.set_title("Share in 1 figure")
ax0.plot([10,5,1,6,5],'ro-', label = "y0")
ax0.set_ylabel("y0")#안쓰면 안나옴
ax1.plot([100,200,220,180,120], 'g:',label="y1")
ax1.set_ylabel("y1")
ax0.set_xlabel("Share x")
plt.show()