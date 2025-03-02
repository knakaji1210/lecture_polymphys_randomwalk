# Functions to calculate distinct 2d self-avoiding Walk

import random as rd

def saw2dCoordinate(N):

# Functions to calculate coordinate list of 2d self-avoiding Walk

    num = 0

    direction_list = ([1,0],[-1,0],[0,1],[0,-1])

    while num < N:
        num = 0
        rep = 0
        x, y = 0, 0
        x_list = [0]
        y_list = [0]
        coordinate_list = [[0,0]]
        num_list = []
        while rep < 20 and num < N:
            step = rd.choice(direction_list)
            x_temp = x + step[0]
            y_temp = y + step[1]
            coordinate_temp = [x_temp, y_temp]
            if coordinate_temp in coordinate_list:
                num = num
                num_list.append(num)
                rep = num_list.count(num_list[-1])
            else:
                x = x_temp
                y = y_temp
                x_list.append(x)
                y_list.append(y)
                coordinate = [x, y]
                coordinate_list.append(coordinate)
                num = num + 1
#        print("final num = "+str(num)) # to check the number of steps

    return coordinate_list


def saw2dDistinctWalks(N, M):

# Function to list up distinct 2d self-avoiding Walks

    walks_list = []

    for m in range(M):
        if (m!=0 and m%1000000 ==0):
            print(m)
        walks_temp = saw2dCoordinate(N)
        if walks_temp in walks_list:
#            print("overlap")
            pass
        else:
#            print("new walk")
            walks_list.append(walks_temp)

    numDistinctWalks = len(walks_list)

    distinctWalks_list = [walks_list, numDistinctWalks]

    return distinctWalks_list
