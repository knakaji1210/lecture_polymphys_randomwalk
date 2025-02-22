# Function to draw animation of 1d Random Walk
# matplotlibのanimationからanimatplotに置き換える試み（250219）

import random as rd
from math import *
import numpy as np

def rw1dS(N):

    num_step = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]

    theta_s = np.array([0,np.pi])   # x軸からの角度

    for n in range(N):
        theta = np.random.choice(theta_s)
        x = x + np.cos(theta)       # (+1 or -1)
        y = y                       # 必ず0
        x_list.append(x)
        y_list.append(y)

        num_step += 1

    print("final num = {0}".format(num_step)) # to check the number of steps

    x_list_steps = [ x_list[:i+1] for i in range(N+1) ]
    y_list_steps = [ y_list[:i+1] for i in range(N+1) ]
    x_front = [ [x_list[i]] for i in range(N+1) ]       # x_listをamp.blocks.Scatterで使える形への変換
    y_front = [ [y_list[i]] for i in range(N+1) ]

    return x_front, y_front, x_list_steps, y_list_steps

def rw1dM(N,M):

    nan = np.nan
    nan_list = [ [nan] for i in range(N)]

    delay_step = 10

    x_list_steps_m = []     # 座標全体
    y_list_steps_m = []
    x_front_m = []          # 各ステップの最後の座標
    y_front_m = []
    x_end_m = []            # 各トライアルの最後の座標
    y_end_m = []

    for m in range(M):
        x_front, y_front, x_list_steps, y_list_steps = rw1dS(N)
        x_list_steps_m += x_list_steps
        y_list_steps_m += y_list_steps
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
    
    return x_list_steps_m, y_list_steps_m, x_front_m, y_front_m, x_end_m, y_end_m

def timeList(N,M):

    delay_step = 10

    timeList = []

    for m in range(M):
        t = np.linspace(0, N+delay_step, N+delay_step+1).tolist()
        timeList += t

    return timeList