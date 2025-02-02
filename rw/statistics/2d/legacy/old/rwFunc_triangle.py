import numpy as np
import random as rd
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import *

# Calculation of 2d Random Walk
def calc_rmean(N):
    M = 100

    direction_list = (0, 2/3, 4/3)

    r2_list = []
    r_list = []

    for m in range(M):
        x, y = 0, 0
        x_list = [0]
        y_list = [0]
        for n in range(N):
            theta = pi*rd.choice(direction_list)
            x = x+cos(theta)
            y = y+sin(theta)
            x_list.append(x)
            y_list.append(y)

        r2 = x*x + y*y
        r = np.sqrt(r2)
        r2_list.append(r2)
        r_list.append(r)

    r2_mean = np.mean(r2_list)
    sqrt_r2 = np.sqrt(r2_mean)
    return sqrt_r2

