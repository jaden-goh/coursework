import numpy as np

def goldenSearch(xl, xu, f, max_iter = 10000):
    R = (np.sqrt(5) - 1) / 2
    d = R*(xu-xl)
    x1 = xl+d
    x2 = xu-d
    eps = 1e-6
    iter = 0

    while abs(xu-xl) > eps and iter < max_iter:
        if f(x1) > f(x2):
            xl = x2
            x2 = x1
            d = R*(xu-xl)
            x1 = xl + d
        
        elif f(x1) < f(x2):
            xu = x1
            x1 = x2
            d = R*(xu-xl)
            x2 = xu - d 
        iter += 1

    optimum = (xl+xu)/2
    print(f"Optimum occurs at x = {optimum}")


def targetfunction(x):
    y = np.sin(x)**2 + 23*x**3 - 5
    return y 

goldenSearch(0,10,targetfunction)