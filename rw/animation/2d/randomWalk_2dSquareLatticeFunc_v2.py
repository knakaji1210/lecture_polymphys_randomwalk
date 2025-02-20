# Function to draw animation of 1d Random Walk
# matplotlibのanimationからanimatplotに置き換える試み（250219）

import random as rd
from math import *
import numpy as np

def randomWalk_1d_S(N):

    num_step = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]

    direction = np.array([0,0.5*np.pi, np.pi, 1.5*np.pi])      # x軸からの角度

    for n in range(N):
        step = np.random.choice(direction)
        x = x + np.cos(step)
        y = y + np.sin(step)
        x_list.append(x)
        y_list.append(y)

        num_step += 1

    print("final num = {0}".format(num_step)) # to check the number of steps

    x_list_steps = [ x_list[:i+1] for i in range(N+1) ]
    y_list_steps = [ y_list[:i+1] for i in range(N+1) ]
    x_front = [ [x_list[i]] for i in range(N+1) ]       # x_listをamp.blocks.Scatterで使える形への変換
    y_front = [ [y_list[i]] for i in range(N+1) ]

    return x_front, y_front, x_list_steps, y_list_steps

def randomWalk_1d_M(N,M):

    nan = np.nan
    nan_list = [ [nan] for i in range(N)]

    x_list_steps_m = []     # 座標全体
    y_list_steps_m = []
    x_front_m = []          # 各ステップの最後の座標
    y_front_m = []
    x_end_m = []            # 各トライアルの最後の座標
    y_end_m = []

    for m in range(M):
        x_front, y_front, x_list_steps, y_list_steps = randomWalk_1d_S(N)
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

        print("repeat num = {0}".format(m+1))

    return x_list_steps_m, y_list_steps_m, x_front_m, y_front_m, x_end_m, y_end_m

def timeList(N,M):

    timeList = []

    for m in range(M):
        t = np.linspace(0, N, N+1).tolist()
        timeList += t

    return timeList