# Functions to calculate distinct 1d Random Walk

import random as rd

def rw1dCoordinate(N):

# Functions to calculate coordinate list of 1d Random Walk

    num = 0
    x, y = 0, 0
    coordinate_list = [[0,0]]

    direction_list = ([1],[-1])

    for n in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y
        coordinate = [x, y]
        coordinate_list.append(coordinate)
        num = num + 1
#    print("final num = "+str(num)) # to check the number of steps

    return coordinate_list



def rw1dDistinctWalks(N, M):

# Function to list up distinct 1d Random Walks

    walks_list = []

    for m in range(M):
        walks_temp = rw1dCoordinate(N)
        if walks_temp in walks_list:
#            print("overlap")
            pass
        else:
#            print("new walk")
            walks_list.append(walks_temp)

    numDistinctWalks = len(walks_list)

    distinctWalks_list = [walks_list, numDistinctWalks]

    return distinctWalks_list
