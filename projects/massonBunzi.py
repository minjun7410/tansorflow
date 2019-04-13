import numpy as np
import matplotlib.pyplot as plt

g = 9.81
cd = 0.25
t = 4
m = 68
print(np.sqrt(g*m/cd)*np.tanh(np.sqrt(g*cd/m)*t))

m = 69
v = np.sqrt(g*m/cd)*np.tanh(np.sqrt(g*cd/m)*t)
print(v)

m = 70
v = np.sqrt(g*m/cd)*np.tanh(np.sqrt(g*cd/m)*t)
print(v)

