import numpy as np

def incremental(func, xmin , xmax):
    x = np.arange(xmin, xmax+1)
    f = func(x)
    nb = 0
    xb = []
    for k in np.arange(np.size(x)-1):
        if np.sign(f[k+1]) != np.sign(f[k]):
            nb += 1
            xb.append(f[k])
            xb.append(f[k+1])
    return np, xb
if __name__ == "__main__":
    g = 9.8; m = 68.1 ; cd = 0.25; v = 36; t = 4
    fp = lambda mp : np.sqrt(g*m/cd)*np.tanh(np.sqrt(g*cd/m)*t)-v
    nb , xb = incremental(fp,1,200)
    print(np)
    print(xb)

