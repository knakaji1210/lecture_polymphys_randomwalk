# Function to calculate properties of 2d Random Walk (triangular lattice model)

from math import *
import numpy as np
import random as rd

def rw2dS(N):

    num_step = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]

    direction = np.array([0,2/3*np.pi, 4/3*np.pi])      # x軸からの角度

    for n in range(N):
        step = rd.choice(direction)
        x = x + np.cos(step)
        y = y + np.sin(step)
        x_list.append(x)
        y_list.append(y)

        num_step += 1

#    print("final num = {0}".format(num_step)) # to check the number of steps

    return x_list, y_list

def rw2dM(N,M):

    xt_list = []            # 終点のリスト
    yt_list = []
    r2_list = []            # r^2のリスト

    for m in range(M):
        if (m!=0 and m%10000 ==0):              # added to check the progress
            print("repeated cycle =", m)
        x_list, y_list = rw2dS(N)
        xt = x_list[-1]
        yt = y_list[-1]
        r2 = xt**2 + yt**2        
        xt_list.append(xt)
        yt_list.append(yt)
        r2_list.append(r2)

#        print("repeat num = {0}".format(m+1))

    return xt_list, yt_list, r2_list
