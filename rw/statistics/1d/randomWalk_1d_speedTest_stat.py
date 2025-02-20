# listとnp.ndarrayの速さを比べるテスト（statの方）

'''
結果
list =  2.901617500028806e-05
array =  0.0005281143708001764
でlistの方が圧倒的に速い
'''

import numpy as np
import random as rd
from math import *
import timeit

def rw1dFuncS_list(N):

    num = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]

    direction_list = ([1],[-1])

    for n in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y
        x_list.append(x)
        y_list.append(y)
        num = num + 1

    coordinateS_list = [x_list, y_list]
    r2 = x_list[-1]*x_list[-1] + y_list[-1]*y_list[-1]
    r = np.sqrt(r2)
    resultS_list = [r2, r]


    return coordinateS_list, resultS_list

def rw1dFuncS_array(N):

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

N = 100
loop = 10000

result_l = timeit.timeit(lambda: rw1dFuncS_list(N), number=loop)
result_a = timeit.timeit(lambda: rw1dFuncS_array(N), number=loop)

print("list = ",result_l / loop)
print("array = ",result_a / loop)