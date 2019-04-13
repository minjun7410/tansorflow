import matplotlib as mpl
import matplotlib.pylab as plt

plt.title("x'y Lim")
plt.plot([10,20,30,40],[1,4,9,16],c="y",lw=3, ls = "-.",
         marker = "o", ms = "15", mec = "r",mew =2, mfc="b")
plt.xlim(0,40)
plt.ylim(-10,20)
plt.show()