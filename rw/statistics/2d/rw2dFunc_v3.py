# Function to calculate properties of 2d Random Walk (all models)
# square lattice, trianglar lattice, FJC chain全てをまとめることにした（250222）

from math import *
import numpy as np
import random as rd

def rw2dS(N, model):

    num_step = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]

    theta_s = np.array([0, 0.5*np.pi, np.pi, 1.5*np.pi]) # x軸からの角度、square lattice model
    theta_t = np.array([0, 2/3*np.pi, 4/3*np.pi])        # x軸からの角度、triangular lattice model

    for n in range(N):
        if model == "S":    # square lattice model 
            theta = rd.choice(theta_s)
        if model == "T":    # triangular lattice model 
            theta = rd.choice(theta_t)
        if model == "F":    # FJC Chain model 
            theta = 2*pi*rd.random()
        x = x + np.cos(theta)
        y = y + np.sin(theta)
        x_list.append(x)
        y_list.append(y)

        num_step += 1

#    print("final num = {0}".format(num_step)) # to check the number of steps

    return x_list, y_list

def rw2dM(N, M, model):

    xt_list = []            # 終点のリスト
    yt_list = []
    r2_list = []            # r^2のリスト

    for m in range(M):
        if (m!=0 and m%10000 ==0):              # added to check the progress
            print("repeated cycle =", m)
        x_list, y_list = rw2dS(N, model)
        xt = x_list[-1]
        yt = y_list[-1]
        r2 = xt**2 + yt**2        
        xt_list.append(xt)
        yt_list.append(yt)
        r2_list.append(r2)

#        print("repeat num = {0}".format(m+1))

    return xt_list, yt_list, r2_list
