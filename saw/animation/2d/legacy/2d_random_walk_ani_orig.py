# Animation of 2d Random Walk (Square Lattice model)

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation

def rd_walk(N):

    num = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]
    coordinate_list = [[0,0]]
    imgs = []

    direction_list = ([1,0],[-1,0],[0,1],[0,-1])

    for n in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y + step[1]
        x_list.append(x)
        y_list.append(y)
        coordinate = [x, y]
        coordinate_list.append(coordinate)
        num = num + 1
        plt.title("2-dimensional Random Walk (N = "+str(N)+")")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.xlim(-30, 30)
        plt.ylim(-30, 30)
        img1 = plt.plot(x_list, y_list, color="cyan")
        img2 = plt.plot(x_list[-1], y_list[-1], marker="x", color="black")
        img = img1 + img2
        imgs.append(img)    
    print("final num = "+str(num)) # to check the number of steps
    img1 = plt.plot(x_list, y_list, color="cyan")
    img2 = plt.plot(x_list[-1], y_list[-1], marker="o", color="red")
    img = img1 + img2
    for i in range(10):
        imgs.append(img)

    return imgs

fig = plt.figure()

M = 5
imgs_rep = []

for m in range(M):
    imgs = rd_walk(100)
    imgs_rep = imgs_rep + imgs
    print("repeat num = "+str(m+1))

ani = animation.ArtistAnimation(fig, imgs_rep, interval=10)
ani.save('2d_random_walk.gif', writer = 'pillow', fps = 30)

plt.show()
plt.close()
