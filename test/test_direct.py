from scipydirect import minimize
import numpy as np

trans = np.array([-1, 2, -4, 3])

def func(x):
    x -= trans
    return np.dot(x, x), 0


if __name__ == '__main__':

    bounds = [(-10, 10) for i in range(4)]

    res = minimize(func, bounds)

    print 'Optimal point:', res.x
    print 'Optimal value:', res.fun
    print 'Exit status:', res.status
    
    
