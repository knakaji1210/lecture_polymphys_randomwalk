# Function to draw animation of 2d Self-Avoiding Walk (Square Lattice model)
# matplotlibのanimationからanimatplotに置き換える試み（250223）

import random as rd
from math import *
import numpy as np

def saw2dS(N):

    num_step = 0

    theta_s = np.array([0,0.5*np.pi, np.pi, 1.5*np.pi])   # x軸からの角度

    x_list_steps = []
    y_list_steps = []
    x_front = []
    y_front = []

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
            y_temp = y + np.rint(np.sin(theta))
            coordinate_temp = [x_temp, y_temp]      # まず仮の新座標を設定
            if coordinate_temp in coordinate_list:  # もし新座標が既に占有されていたらという条件
                x = x
                y = y
                x_list.append(x) #試行中でステイしていることを示す部分
                y_list.append(y)
                num_step = num_step
                num_step_list.append(num_step)
                num_rep = num_step_list.count(num_step_list[-1])    # .countメソッドで試行回数を計算
#                print("failure: num = {0}".format(num_step)) 
            else:                                   # もし新座標が非占有だったらという条件
                x = x + np.rint(np.cos(theta))
                y = y + np.rint(np.sin(theta))
                x_list.append(x)
                y_list.append(y)
                coordinate = [x, y]
                coordinate_list.append(coordinate)  # 新座標を登録
                num_step += 1
#                print("success: num = {0}".format(num_step))

        print("final num = {0}".format(num_step)) # to check the number of steps

        len_list = len(x_list)  # 途中失敗などがあるため、x_listの長さが不定なので計測
        x_list_step = [ x_list[:i+1] for i in range(len_list) ] # x_listをamp.blocks.Scatterで使える形への変換
        y_list_step = [ y_list[:i+1] for i in range(len_list) ] # num_stepがNに満たない場合も含める
        x_front_s = [ [x_list[i]] for i in range(len_list) ]    # x_listをamp.blocks.Scatterで使える形への変換
        y_front_s = [ [y_list[i]] for i in range(len_list) ]
        x_list_steps += x_list_step                             # 失敗時も成功時も追加、これで全ての途中過程を追いかけている
        y_list_steps += y_list_step
        x_front += x_front_s
        y_front += y_front_s

    return x_front, y_front, x_list_steps, y_list_steps

def saw2dM(N,M):

    nan = np.nan

    delay_step = 10

    x_list_steps_m = []     # 座標全体
    y_list_steps_m = []
    x_front_m = []          # 各ステップの最後の座標
    y_front_m = []
    x_end_m = []            # 各トライアルの最後の座標
    y_end_m = []
    num_step_list = []      # 各トライアルのステップ数

    for m in range(M):
        x_front, y_front, x_list_steps, y_list_steps = saw2dS(N)
        x_list_steps_m += x_list_steps
        y_list_steps_m += y_list_steps
        num_step = len(x_front)                 # x_frontの長さが不定のため計測
#        print("l =",num_step)
        num_step_list.append(num_step)
        nan_list = [ [nan] for i in range(num_step-1)]
        x_end = nan_list + [x_front[-1]]        # x_frontの最後をnanにする前に抽出し"o"の座標を作成
        y_end = nan_list + [y_front[-1]]
        x_end_m += x_end
        y_end_m += y_end         
        x_front[-1] = [nan]                     # x_frontの最後を"x"ではなく"o"にするための変換
        y_front[-1] = [nan]
        x_front_m += x_front
        y_front_m += y_front

        for i in range(delay_step):     # "o"を表示している時間を伸ばすため
            x_list_steps_m.append(x_list_steps_m[-1])
            y_list_steps_m.append(y_list_steps_m[-1])
            x_front_m.append(x_front_m[-1])
            y_front_m.append(y_front_m[-1])
            x_end_m.append(x_end_m[-1])
            y_end_m.append(y_end_m[-1])

        print("repeat num = {0}".format(m+1))
    
    return x_list_steps_m, y_list_steps_m, x_front_m, y_front_m, x_end_m, y_end_m, num_step_list

def timeList(num_step_list,M):

    delay_step = 10

    timeList = []

    for m in range(M):
        num_step = num_step_list[m]
        t = np.linspace(0, num_step+delay_step-1, num_step+delay_step).tolist()
        timeList += t

    return timeList