from scipydirect import minimize
import numpy as np
import numpy.testing as npt

def func(x):
    x -=  np.array([-1, 2, -4, 3])
    return np.dot(x, x)

def test_minimize():
    bounds = [(-10, 10) for i in range(4)]
    res = minimize(func, bounds)
    npt.assert_allclose(res.x, np.array([-1, 2, -4, 3]), atol=0.1)

if __name__ == '__main__':
    test_minimize()
