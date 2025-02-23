# Function to draw animation of 3d Self-Avoiding Walk (Square Lattice model)

import random as rd
from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def selfAvoidWalk_3dSquareLattice(N):

    num = 0
    x, y, z = 0, 0, 0
    x_list = [0]
    y_list = [0]
    z_list = [0]
    coordinate_list = [[0,0,0]]
    imgs = []

    direction_list = ([1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1])

    while num < N:
        num = 0
        rep = 0
        x, y, z = 0, 0, 0
        x_list = [0]
        y_list = [0]
        z_list = [0]
        coordinate_list = [[0,0,0]]
        num_list = []
        while rep < 20 and num < N:
            step = rd.choice(direction_list)
            x_temp = x + step[0]
            y_temp = y + step[1]
            z_temp = z + step[2]
            coordinate_temp = [x_temp, y_temp, z_temp]
            if coordinate_temp in coordinate_list:
                x = x
                y = y
                z = z
                x_list.append(x) #ここに追加したのは重要
                y_list.append(y) #ここに追加したのは重要
                z_list.append(z) #ここに追加したのは重要
                num = num
                num_list.append(num)
                rep = num_list.count(num_list[-1])
                img = plt.plot(x_list, y_list, z_list, color="blue")
                imgs.append(img)
                #print("failure: num= "+str(num))                
            else:
                x = x + step[0]
                y = y + step[1]
                z = z + step[2]
                x_list.append(x)
                y_list.append(y)
                z_list.append(z)
                coordinate = [x, y, z]
                coordinate_list.append(coordinate)
                num = num + 1
                img = plt.plot(x_list, y_list, z_list, color="blue")
                imgs.append(img)
                #print("success: num= "+str(num)) 
            img1 = plt.plot(x_list, y_list, z_list, color="blue")
            img2 = plt.plot(x_list[-1], y_list[-1], z_list[-1], marker="x", color="black")
            img = img1 + img2
            imgs.append(img)    
        print("final num = "+str(num)) # to check the number of steps
    img1 = plt.plot(x_list, y_list, z_list, color="blue")
    img2 = plt.plot(x_list[-1], y_list[-1], z_list[-1], marker="o", color="red")
    img = img1 + img2
    for i in range(10):
        imgs.append(img)

    return imgs