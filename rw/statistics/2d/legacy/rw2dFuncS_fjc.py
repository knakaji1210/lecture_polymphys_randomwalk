# Function to calculate properties of 2d Random Walk (freely-jointed chain model) (single run)

import numpy as np
import random as rd
from math import *
#import matplotlib.pyplot as plt

def rw2dFuncS(N):

    num = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]
#    coordinate_list = [[0,0]]
#    imgs = []

    for n in range(N):
        theta = 2*pi*rd.random()
# 以下の１行は一時的な修正（海岸線的な絵を描くための）
#       theta = pi*rd.random()
        x = x+cos(theta)
        y = y+sin(theta)
        x_list.append(x)
        y_list.append(y)
#        coordinate = [x, y]
#        coordinate_list.append(coordinate)
        num = num + 1
#        img1 = plt.plot(x_list, y_list, color="cyan")
#        img2 = plt.plot(x_list[-1], y_list[-1], marker="x", color="black")
#        img = img1 + img2
#        imgs.append(img)    
#    print("final num = "+str(num)) # to check the number of steps
#    img1 = plt.plot(x_list, y_list, color="cyan")
#    img2 = plt.plot(x_list[-1], y_list[-1], marker="o", color="red")
#    img = img1 + img2
#    for i in range(10):
#        imgs.append(img)

#    print(x_list[-1], y_list[-1])
    coordinateS_list = [x_list, y_list]
    r2 = x_list[-1]*x_list[-1] + y_list[-1]*y_list[-1]
    r = np.sqrt(r2)
    resultS_list = [r2, r]


    return coordinateS_list, resultS_list