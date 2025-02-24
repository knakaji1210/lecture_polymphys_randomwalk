# Function to calculate properties of 3d Self-Avoiding Walk (square lattice model)
# matplotlibのanimationからanimatplotに置き換える試み（250223）
# saw2dFunc_square_v2をコピーして拡張（250224）
# rw3dFunc_v3で導入した球面座標系をここでも採用（ただし、FJCは「占有」の判定が難しいので保留）

import random as rd
from math import *
import numpy as np

def saw3dS(N):

    num_step = 0

    direction_list = ["xp", "xm", "yp", "ym", "zp", "zm"]    # 6方向をリスト化

    while num_step < N:
        num_step = 0
        num_rep = 0         # 袋小路に入ったときに繰り返す試行回数
        x, y, z = 0, 0, 0
        x_list = [0]
        y_list = [0]
        z_list = [0]
        coordinate_list = [[0,0,0]]   # 通過した点の記録
        num_step_list = []

        while num_rep < 20 and num_step < N:        # 試行は20回までで諦める
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
            x_temp = x + np.rint(np.sin(theta)*np.cos(phi))     # 一致不一致をチェックするため、整数化を行う
            y_temp = y + np.rint(np.sin(theta)*np.sin(phi))
            z_temp = z + np.rint(np.cos(theta))
            coordinate_temp = [x_temp, y_temp, z_temp]      # まず仮の新座標を設定
            if coordinate_temp in coordinate_list:  # もし新座標が既に占有されていたらという条件
                num_step = num_step
                num_step_list.append(num_step)
                num_rep = num_step_list.count(num_step_list[-1])    # .countメソッドで試行回数を計算
#                print("failure: num = {0}".format(num_step)) 
            else:                                   # もし新座標が非占有だったらという条件
                x = x + np.rint(np.sin(theta)*np.cos(phi))     # 一致不一致をチェックするため、整数化を行う
                y = y + np.rint(np.sin(theta)*np.sin(phi))
                z = z + np.rint(np.cos(theta))
                x_list.append(x)
                y_list.append(y)
                z_list.append(z)
                coordinate = [x, y, z]
                coordinate_list.append(coordinate)  # 新座標を登録
                num_step += 1
#                print("success: num = {0}".format(num_step))

#        print("final num = {0}".format(num_step)) # to check the number of steps

    return x_list, y_list, z_list

def saw3dM(N,M):

    xt_list = []            # 終点のリスト
    yt_list = []
    zt_list = []
    r2_list = []            # r^2のリスト

    for m in range(M):
        if (m!=0 and m%10000 ==0):              # added to check the progress
            print("repeated cycle =", m)
        x_list, y_list, z_list = saw3dS(N)
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