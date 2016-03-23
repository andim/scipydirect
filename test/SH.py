#!/usr/bin/python
"""
Solve the 2D Shubert function.
"""

from __future__ import division
from scipydirect import minimize
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

def obj(x):
    """Two Dimensional Shubert Function"""
    
    j = np.arange(1, 6)
    tmp1 = np.dot(j, np.cos((j+1)*x[0] + j))
    tmp2 = np.dot(j, np.cos((j+1)*x[1] + j))
    return tmp1 * tmp2


if __name__ == '__main__':
    bounds = [(-10, 10), (-10, 10)]
    res = minimize(obj, bounds)
    print res

    # Plot the results.
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = res.x
    X, Y = np.mgrid[x[0]-2:x[0]+2:50j, x[1]-2:x[1]+2:50j]
    Z = np.zeros_like(X)

    for i in range(X.size):
        Z.ravel()[i] = obj([X.flatten()[i], Y.flatten()[i]])
        
    ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet)
    ax.scatter(x[0], x[1], res.fun, c='r', marker='o')
    ax.set_title('Two Dimensional Shubert Function')
    plt.show()
