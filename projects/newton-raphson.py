import math;
import numpy as np
def sech(x):
    return np.cosh(x)**(-1)
def newton_raspson(func, dfunc , xr):
    maxit = 50
    es = 1.0e-5
    iter = 0
    while(1):
        xroid = xrxr = np.float(xr-func(xr)/dfunc(xr))
        iter += 1
        if xr != 0:
            ea = np.float(np.abs((np.flat(xr)-np.float(xroid))/np.float(xr))*100)
        if np.int(ea <= es) | np.int(iter >= maxit):
            break
    root = xr
    fx = func(xr)
    return root , fx ,ea , iter
if __name__ == '__main__':
    g = 9.81; cd = 0.25; v = 36; t = 4 ;
    fp= lambda m: np.sqrt(g*m/cd)*np.tanh(np.sqrt(g*cd/m)*t)
    dfp = lambda m : (1/2)*np.sqrt(9.81/(m*0.25))*np.tanh(np.sqrt(9.81*0.25/m)*4)-9.81*4/(2*m)*(sech(np.sqrt(9.81*0.25/m)*4))**2
    root,fx,ea,iter = newton_raspson(fp,dfp,140)
    print('root weight= ', root)
    print('f(root weight, should bs zero) = ' , fx)
    print('ea = should be less than 1.0e-4',ea)
    print('iter = ', iter)
