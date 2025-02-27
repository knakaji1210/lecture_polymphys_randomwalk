# Functions to calculate distinct 2d Random Walk

import random as rd

def rw2dCoordinate(N):

# Functions to calculate coordinate list of 2d Random Walk

    num = 0
    x, y = 0, 0
    coordinate_list = [[0,0]]

    direction_list = ([1,0],[-1,0],[0,1],[0,-1])

    for n in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y + step[1]
        coordinate = [x, y]
        coordinate_list.append(coordinate)
        num = num + 1
#    print("final num = "+str(num)) # to check the number of steps

    return coordinate_list



def rw2dDistinctWalks(N, M):

# Function to list up distinct 2d Random Walks

    walks_list = []

    for m in range(M):
        if (m!=0 and m%100000 ==0):
            print(m)
        walks_temp = rw2dCoordinate(N)
        if walks_temp in walks_list:
#            print("overlap")
            pass
        else:
#            print("new walk")
            walks_list.append(walks_temp)

    numDistinctWalks = len(walks_list)

    distinctWalks_list = [walks_list, numDistinctWalks]

    return distinctWalks_list
