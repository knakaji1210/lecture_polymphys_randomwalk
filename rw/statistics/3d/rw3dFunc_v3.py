# Function to calculate properties of 3d Random Walk (all models)
# square lattice, FJC chainをまとめることにした（250222）
# そのために球面座標系を採用してみた

from math import *
import numpy as np
import random as rd

def rw3dS(N, model):

    num_step = 0
    x, y, z = 0, 0, 0
    x_list = [0]
    y_list = [0]
    z_list = [0]

    direction_list = ["xp", "xm", "yp", "ym", "zp", "zm"]    # 6方向をリスト化

    for n in range(N):
        if model == "S":    # square lattice model 
            direction = rd.choice(direction_list)
            if direction == "xp":
                theta = 0.5*np.pi
                phi = 0
            if direction == "xm":
                theta = 0.5*np.pi
                phi = np.pi
            if direction == "yp":
                theta = 0.5*np.pi
                phi = 0.5*np.pi
            if direction == "ym":
                theta = 0.5*np.pi
                phi = 1.5*np.pi                  
            if direction == "zp":
                theta = 0
                phi = 0           # 極座標としては不要だけど計算に必要なため追記
            if direction == "zm":
                theta = np.pi
                phi = 0           # 極座標としては不要だけど計算に必要なため追記  
        if model == "F":    # FJC Chain model 
            theta = 2*pi*rd.random()
            phi   = pi*rd.random()
        x = x + np.sin(theta)*np.cos(phi)
        y = y + np.sin(theta)*np.sin(phi)
        z = z + np.cos(theta)
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        num_step += 1

#    print("final num = {0}".format(num_step)) # to check the number of steps

    return x_list, y_list, z_list

def rw3dM(N, M, model):

    xt_list = []            # 終点のリスト
    yt_list = []
    zt_list = []
    r2_list = []            # r^2のリスト

    for m in range(M):
        if (m!=0 and m%10000 ==0):              # added to check the progress
            print("repeated cycle =", m)
        x_list, y_list, z_list = rw3dS(N, model)
        xt = x_list[-1]
        yt = y_list[-1]
        zt = z_list[-1]
        r2 = xt**2 + yt**2 + zt**2        
        xt_list.append(xt)
        yt_list.append(yt)
        zt_list.append(zt)
        r2_list.append(r2)

#        print("repeat num = {0}".format(m+1))

    return xt_list, yt_list, zt_list, r2_list
