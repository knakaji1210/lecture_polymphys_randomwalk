# Function to calculate properties of 1d Self-Avoiding Walk
# 1dを2dをベースに新たに作成（あまり意味ないけど・・・一応ね）（250224）

import random as rd
from math import *
import numpy as np

def saw1dS(N):

    num_step = 0

    theta_s = np.array([0,np.pi])   # x軸からの角度

    while num_step < N:
        num_step = 0
        num_rep = 0         # 袋小路に入ったときに繰り返す試行回数
        x, y = 0, 0
        x_list = [0]
        y_list = [0]
        coordinate_list = [[0,0]]   # 通過した点の記録
        num_step_list = []

        while num_rep < 20 and num_step < N:        # 試行は20回までで諦める
            theta = np.random.choice(theta_s)
            x_temp = x + np.rint(np.cos(theta))     # 一致不一致をチェックするため、整数化を行う
            y_temp = y
            coordinate_temp = [x_temp, y_temp]      # まず仮の新座標を設定
            if coordinate_temp in coordinate_list:  # もし新座標が既に占有されていたらという条件
#                x = x            #試行中でステイしていることを示す部分、最終経路示すだけなら不要
#                y = y
#                x_list.append(x) #試行中でステイしていることを示す部分、最終経路示すだけなら不要
#                y_list.append(y)
                num_step = num_step
                num_step_list.append(num_step)
                num_rep = num_step_list.count(num_step_list[-1])    # .countメソッドで試行回数を計算
#                print("failure: num = {0}".format(num_step)) 
            else:                                   # もし新座標が非占有だったらという条件
                x = x + np.rint(np.cos(theta))
                y = y
                x_list.append(x)
                y_list.append(y)
                coordinate = [x, y]
                coordinate_list.append(coordinate)  # 新座標を登録
                num_step += 1
#                print("success: num = {0}".format(num_step))

#        print("final num = {0}".format(num_step)) # to check the number of steps

    return x_list, y_list

def saw1dM(N,M):

    xt_list = []            # 終点のリスト
    yt_list = []
    r2_list = []            # r^2のリスト

    for m in range(M):
        if (m!=0 and m%10000 ==0):              # added to check the progress
            print("repeated cycle =", m)
        x_list, y_list = saw1dS(N)
        xt = x_list[-1]
        yt = y_list[-1]
        r2 = xt**2 + yt**2        
        xt_list.append(xt)
        yt_list.append(yt)
        r2_list.append(r2)

#        print("repeat num = {0}".format(m+1))

    return xt_list, yt_list, r2_list