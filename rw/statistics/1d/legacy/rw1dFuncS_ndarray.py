# Function to calculate properties of 1d Random Walk (single run)
# pythonのリストで書いたオリジナルをnp.ndarrayに置き換える試み（250214）

import numpy as np
from math import *

def rw1dFuncS(N):

    num_step = 0
    nan = np.nan

    ini_array = np.full(N, nan)         # nanからなる配列を作成
    ini_array = np.append(0, ini_array) # 原点の0を加える
    x_array = np.copy(ini_array)        # x_arrayとしてコピー    
    y_array = np.copy(ini_array)        # y_arrayとしてコピー
    x, y = 0, 0                         # x,yの初期値

    direction = np.array([0,np.pi])     # x軸からの角度

    for n in range(N):
        step = np.random.choice(direction)
        x = x + np.cos(step)            # (+1 or -1)
#       y = y + np.sin(step)            # 正式にはこっちだけど、すごい小さい数字が入ってしまうので不採用
        y = y                           # 必ず0
        np.put(x_array, n+1, x)         # x_arrayの(n+1)番目をxの値で更新
        np.put(y_array, n+1, y)         # y_arrayの(n+1)番目をyの値で更新
        num_step += 1

    coordinateS_array = np.concatenate([x_array, y_array], 0).reshape(2,N+1)

    return coordinateS_array