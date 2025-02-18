# listとnp.ndarrayの速さを比べるテスト（anim）

'''
結果
list =  0.029663904100016226
array =  0.0016563124998356215
でarrayの方が圧倒的に速いが、no_imgでやると
list_noimg =  3.56917007593438e-05
でlistの方が圧倒的に速い。
'''

import random as rd
from math import *
import numpy as np
import matplotlib.pyplot as plt
import timeit

def randomWalk_1d_list(N):

    num = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]
    coordinate_list = [[0,0]]
    imgs = []

    direction_list = ([1],[-1])

    for n in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y
        x_list.append(x)
        y_list.append(y)
        coordinate = [x, y]
        coordinate_list.append(coordinate)
        num = num + 1
        img1 = plt.plot(x_list, y_list, color="cyan")
        img2 = plt.plot(x_list[-1], y_list[-1], marker="x", color="black")
        img = img1 + img2
        imgs.append(img)    
    print("final num = {0}".format(num)) # to check the number of steps
    img1 = plt.plot(x_list, y_list, color="cyan")
    img2 = plt.plot(x_list[-1], y_list[-1], marker="o", color="red")
    img = img1 + img2
    for i in range(10):
        imgs.append(img)

    return imgs

def randomWalk_1d_list_No_img(N):

    num = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]
    coordinate_list = [[0,0]]
    imgs = []

    direction_list = ([1],[-1])

    for n in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y
        x_list.append(x)
        y_list.append(y)
        coordinate = [x, y]
        coordinate_list.append(coordinate)
        num = num + 1
    print("final num = {0}".format(num)) # to check the number of steps

    return coordinate_list

def randomWalk_1d_array(N):

    num_step = 0
    nan = np.nan

    ini_array = np.full(N, nan)         # nanからなる配列を作成
    ini_array = np.append(0, ini_array) # 原点の0を加える
    x_array = np.copy(ini_array)        # x_arrayとしてコピー    
    y_array = np.copy(ini_array)        # y_arrayとしてコピー
    x, y = 0, 0                         # x,yの初期値

    x_array_steps = []
    y_array_steps = []

    direction = np.array([0,np.pi])     # x軸からの角度

    for n in range(N):
        step = np.random.choice(direction)
        x = x + np.cos(step)            # (+1 or -1)
        y = y + np.sin(step)            # 必ず0
        np.put(x_array, n+1, x)         # x_arrayの(n+1)番目をxの値で更新
        np.put(y_array, n+1, y)         # y_arrayの(n+1)番目をyの値で更新
        x_array_steps = np.append(x_array_steps, x_array)
        y_array_steps = np.append(y_array_steps, y_array)
        num_step += 1

    x_array_steps = np.insert(x_array_steps, 0, ini_array)  # 初期状態を先頭に追加
    y_array_steps = np.insert(y_array_steps, 0, ini_array)

    print("final num = {0}".format(num_step)) # to check the number of steps

    return x_array_steps, y_array_steps

N = 100
loop = 10

result_l = timeit.timeit(lambda: randomWalk_1d_list(N), number=loop)
result_l_noimg = timeit.timeit(lambda: randomWalk_1d_list_No_img(N), number=loop)
result_a = timeit.timeit(lambda: randomWalk_1d_array(N), number=loop)

print("list = ",result_l / loop)
print("list_noimg = ",result_l_noimg / loop)
print("array = ",result_a / loop)