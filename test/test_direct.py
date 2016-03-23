from scipydirect import minimize
import numpy as np

def func(x):
    x -=  np.array([-1, 2, -4, 3])
    return np.dot(x, x)

if __name__ == '__main__':
    bounds = [(-10, 10) for i in range(4)]
    res = minimize(func, bounds)
    print res
