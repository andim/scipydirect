from scipydirect import minimize
import numpy as np
import numpy.testing as npt

def test_minimize():

    # basic test
    bounds = [(-10, 10) for i in range(4)]
    def func(x):
        x -=  np.array([-1, 2, -4, 3])
        return np.dot(x, x)
    res = minimize(func, bounds)
    npt.assert_allclose(res.x, np.array([-1, 2, -4, 3]), atol=0.1)

    # test with function not defined everywhere
    def func(x):
        if np.sum(np.abs(x)) > 20:
            raise Exception("func not defined")
        x -=  np.array([-1, 2, -4, 3])
        return np.dot(x, x)
    res = minimize(func, bounds)
    npt.assert_allclose(res.x, np.array([-1, 2, -4, 3]), atol=0.1)

if __name__ == '__main__':
    test_minimize()
