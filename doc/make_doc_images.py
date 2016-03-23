from __future__ import division
from scipydirect import minimize
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import os

IMAGES_BASE = 'images'

def savefig(title):
    plt.savefig(os.path.join(IMAGES_BASE, title), bbox_inches='tight', pad_inches=0)


def tutorial1():
    """Images for tutorial 1"""
    
    def obj(x):
        """Six-hump camelback function"""
        
        x1 = x[0]
        x2 = x[1]
        
        f = (4 - 2.1*(x1*x1) + (x1*x1*x1*x1)/3.0)*(x1*x1) + x1*x2 + (-4 + 4*(x2*x2))*(x2*x2)
        return f
    
    bounds = [(-3, 3), (-2, 2)]
    res = minimize(obj, bounds)

    #
    # Plot the results.
    #
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = res.x
    X, Y = np.mgrid[x[0]-1:x[0]+1:50j, x[1]-1:x[1]+1:50j]
    Z = np.zeros_like(X)

    for i in range(X.size):
        Z.ravel()[i] = obj([X.flatten()[i], Y.flatten()[i]])
        
    ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet)
    ax.scatter(x[0], x[1], res.fun, c='r', marker='o')
    ax.set_title('Six-hump Camelback Function')
    ax.view_init(30, 45)
    savefig('six_hump.png')
    

if __name__ == '__main__':
    tutorial1()    
    plt.show()
