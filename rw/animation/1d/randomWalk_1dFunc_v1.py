# Function to draw animation of 1d Random Walk

import random as rd
from math import *
import matplotlib.pyplot as plt

def randomWalk_1d(N):

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