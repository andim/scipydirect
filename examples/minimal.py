import numpy as np
from scipydirect import minimize

def obj(x):
    return (x**2).sum()

bounds = np.array([[-3.0, 3.0], [0.5, 5.0]])
res = minimize(obj, bounds=bounds)
print(res)
