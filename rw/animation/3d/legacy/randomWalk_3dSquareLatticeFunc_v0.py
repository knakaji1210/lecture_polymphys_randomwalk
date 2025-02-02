# Function to draw animation of 3d Random Walk (Square Lattice model)

import random as rd
from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randomWalk_3dSquareLattice(N):

    num = 0
    x, y, z = 0, 0, 0
    x_list = [0]
    y_list = [0]
    z_list = [0]
    coordinate_list = [[0,0,0]]
    imgs = []

    direction_list = ([1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1])

    for n in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y + step[1]
        z = z + step[2]
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        coordinate = [x, y, z]
        coordinate_list.append(coordinate)
        num = num + 1
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