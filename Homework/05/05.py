'''複製+修改，參考LeeYi的程式碼，並藉由ChatGPT完成'''

import numpy as np
from engine import Value
from numpy.linalg import norm


def grad(f, p):
    p_values = [Value(x) for x in p]
    fp = f(p_values)
    fp.backward()
    return np.array([x.grad for x in p_values])

def gradientDescendent(f, p0, h=0.01, max_loops=100000):
    p = p0.copy()
    for _ in range(max_loops):
        fp = f(p)
        fp.backward()
        gp = [param.grad for param in p]  
        glen = norm(gp)
        if glen < 0.00001:
            break
        gh = np.multiply(gp, -h)
        p = [param + grad for param, grad in zip(p, gh)]  
    print(p)
    return p

def f(p):
    [x, y, z] = p
    return (x-1)**2+(y-2)**2+(z-3)**2

p = [Value(0), Value(0), Value(0)]
print(f(gradientDescendent(f, p)))