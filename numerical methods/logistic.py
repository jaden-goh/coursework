import numpy as np
import pandas as pd

def sigmoid(func, x):
    return 1/(1+np.exp(-func(x)))

def linear(x):
    return 1 + 0.5(x)


