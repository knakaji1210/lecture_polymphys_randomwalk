# Function to draw animation of 2d Random Walk (Square Lattice model)
# pythonのリストで書いたオリジナルをnp.ndarrayに置き換える試み（250211）

from math import *
import numpy as np
import matplotlib.pyplot as plt

def randomWalk_2d_S(N):

    num_step = 0
    nan = np.nan

    ini_array = np.full(N, nan)         # nanからなる配列を作成
    ini_array = np.append(0, ini_array) # 原点の0を加える
    x_array = np.copy(ini_array)        # x_arrayとしてコピー    
    y_array = np.copy(ini_array)        # y_arrayとしてコピー
    x, y = 0, 0                         # x,yの初期値

    x_array_steps = []
    y_array_steps = []

    direction = np.array([0,0.5*np.pi, np.pi, 1.5*np.pi])     # x軸からの角度

    for n in range(N):
        step = np.random.choice(direction)
        x = x + np.cos(step)            # (x, y) = (1, 0), (0, 1), (-1, 0), (-1, -1)
        y = y + np.sin(step)
        np.put(x_array, n+1, x)         # x_arrayの(n+1)番目をxの値で更新
        np.put(y_array, n+1, y)         # y_arrayの(n+1)番目をyの値で更新
        x_array_steps = np.append(x_array_steps, x_array)
        y_array_steps = np.append(y_array_steps, y_array)
        num_step += 1

    x_array_steps = np.insert(x_array_steps, 0, ini_array)  # 初期状態を先頭に追加
    y_array_steps = np.insert(y_array_steps, 0, ini_array)
#    x_array_steps = np.reshape(x_array_steps, [N+1, N+1])  # 各ステップごとの配列に整形
#    y_array_steps = np.reshape(y_array_steps, [N+1, N+1])  # reshapeはrandomWalk_1d_Mの方で対応することにした

    '''
    x_array_stepsは以下のような二次元配列になる。
    [[ 0. nan nan nan nan nan nan nan nan nan nan]
    [ 0. -1. nan nan nan nan nan nan nan nan nan]
    [ 0. -1. -2. nan nan nan nan nan nan nan nan]
    [ 0. -1. -2. -1. nan nan nan nan nan nan nan]
    [ 0. -1. -2. -1.  0. nan nan nan nan nan nan]
    [ 0. -1. -2. -1.  0. -1. nan nan nan nan nan]
    [ 0. -1. -2. -1.  0. -1.  0. nan nan nan nan]
    [ 0. -1. -2. -1.  0. -1.  0.  1. nan nan nan]
    [ 0. -1. -2. -1.  0. -1.  0.  1.  2. nan nan]
    [ 0. -1. -2. -1.  0. -1.  0.  1.  2.  1. nan]
    [ 0. -1. -2. -1.  0. -1.  0.  1.  2.  1.  0.]]
    このとき、最後の位置はこの配列の対角成分になる。
    [ 0. -1. -2. -1.  0. -1.  0.  1.  2.  1.  0.]
    そのため
    np.diag(x_array_steps)
    でそれを抽出する
    '''

    print("final num = {0}".format(num_step)) # to check the number of steps

    return x_array_steps, y_array_steps

def randomWalk_2d_M(N,M):

    nan = np.nan

    ini_array = np.full(N, nan)
    x_array_steps_m = []    # 座標全体
    y_array_steps_m = []
    x_front_m = []          # 各ステップの最後の座標
    y_front_m = []
    x_end_m = []            # 各トライアルの最後の座標
    y_end_m = []

    for m in range(M):
        x_array_steps, y_array_steps = randomWalk_2d_S(N)
        x_array_steps_m = np.append(x_array_steps_m, x_array_steps)
        y_array_steps_m = np.append(y_array_steps_m, y_array_steps)
        x_front = np.diag(x_array_steps.reshape(N+1,N+1))   # ここでreshapeするのは上のx_array_stepsは二次元配列になっていないから
        y_front = np.diag(y_array_steps.reshape(N+1,N+1))
        x_front_copy = x_front.copy()                       # コピーするのは何故かわからないがx_frontがread-onlyだから
        y_front_copy = y_front.copy()
        np.put(x_front_copy, N, nan)                        # 最後の要素だけnanに変換（xは最後の座標にはつけたくないから）
        np.put(y_front_copy, N, nan)
        x_front_m = np.append(x_front_m, x_front_copy)      # 最後だけnanに置換したものを追加していく
        y_front_m = np.append(y_front_m, y_front_copy)
        x_end = x_front[-1]                                 # 各トライアルの最後の座標を抽出
        y_end = y_front[-1]
        x_end_m = np.append(x_end_m, ini_array)
        x_end_m = np.append(x_end_m, x_end)
        y_end_m = np.append(y_end_m, ini_array)
        y_end_m = np.append(y_end_m, y_end)

        print("repeat num = {0}".format(m+1))

    x_array_steps_m = np.reshape(x_array_steps_m, [M*(N+1), N+1])  # 各ステップごとの配列に整形
    y_array_steps_m = np.reshape(y_array_steps_m, [M*(N+1), N+1])
    x_front_m = np.reshape(x_front_m, [M*(N+1), 1])
    y_front_m = np.reshape(y_front_m, [M*(N+1), 1])
    x_end_m = np.reshape(x_end_m, [M*(N+1), 1])
    y_end_m = np.reshape(y_end_m, [M*(N+1), 1])

    return x_array_steps_m, y_array_steps_m, x_front_m, y_front_m, x_end_m, y_end_m

def timeArray(N,M):

    timeArray = []

    for m in range(M):
        t = np.linspace(0, N, N+1)
        timeArray = np.append(timeArray, t)

    return timeArray