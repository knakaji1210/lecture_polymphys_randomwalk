# Functions to calculate distinct 1d Random Walk

import random as rd

def rw1dAddStep(initial_coordinate_list):

# Functions to add a step to coordinate_list of 1d Random Walk

    len_initial = len(initial_coordinate_list)

    updated_coordinate_list = [ initial_coordinate_list[x] for x in range(len_initial)]
    coordinate_end = initial_coordinate_list[-1]

    x, y = coordinate_end[0], coordinate_end[1]

    direction_list = ([1],[-1])

    step = rd.choice(direction_list)
    x = x + step[0]
    y = y
    coordinate = [x, y]
    updated_coordinate_list.append(coordinate)

    return updated_coordinate_list



def rw1dCheckOverlap(coordinate_list, trials):

# Function to list up distinct 1d Random Walks

    walks_list = []

    for t in range(trials):
        walks_temp = rw1dAddStep(coordinate_list)
        if walks_temp in walks_list:
#           print("overlap")
            pass
        else:
#           print("new walk")
            walks_list.append(walks_temp)

    return walks_list