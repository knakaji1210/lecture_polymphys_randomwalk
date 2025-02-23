import numpy as np
import random as rd
from math import *
from matplotlib import pyplot as plt
from matplotlib import animation

def rdwalk(N):
    x, y = 0, 0
    x_list = [0]
    y_list = [0]
    imgs = []
    mx, my = -14, 14
    mx_list = [-14]
    my_list = [14]

    direction_list = ([1,0],[-1,0],[0,1],[0,-1])

    for n in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y + step[1]
        x_list.append(x)
        y_list.append(y)
        mx = mx + 0.1
        my = my
        mx_list.append(mx)
        my_list.append(my)
        plt.title("2-dimensional Random Walk (N = "+str(N)+")")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.xlim(-15, 15)
        plt.ylim(-15, 15)
        img1 = plt.plot(x_list, y_list, color="cyan")
        img2 = plt.plot(mx_list, my_list, marker=".", color="red")
        img3 = plt.plot(-4, 14, marker=".", color="blue")
        img = img1 + img2 + img3
        imgs.append(img)
    return imgs


fig = plt.figure()

M = 5
imgss =[]

for m in range(M):
    N = 100
    imgs = rdwalk(N)
    imgss = imgss + imgs

ani = animation.ArtistAnimation(fig, imgss, interval=50)
ani.save('2d_random_walk.gif', writer = 'pillow', fps = 30)
 
plt.show()
plt.close()