# Functions to generate distinct 3d Self-Avoiding Walk

import random as rd

def saw3dAddStep(coordinate_list):

# Functions to add a step to coordinate_list of 2d Random Walk

    len_coordinate = len(coordinate_list)

    updated_coordinate_list = [ coordinate_list[x] for x in range(len_coordinate)]
    coordinate_end = coordinate_list[-1]

    x, y, z = coordinate_end[0], coordinate_end[1], coordinate_end[2]

    direction_list = ([1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1])

    num = 0
    rep = 0
    num_list = []

    #for i in range(1):
    while rep < 10 and num < 1:
        step = rd.choice(direction_list)
        x_temp = x + step[0]
        y_temp = y + step[1]
        z_temp = z + step[2]
        coordinate_temp = [x_temp, y_temp, z_temp]
        if coordinate_temp in coordinate_list:
#            print("failure")
            num = num
            num_list.append(num)
            rep = num_list.count(num_list[-1])
        else:
#            print("sucsess")
            x = x_temp
            y = y_temp
            z = z_temp
            coordinate = [x, y, z]
            updated_coordinate_list.append(coordinate)
            num = num + 1

    return updated_coordinate_list



def saw3dDistinctWalks(walks_list, trials):

# Function to obtain distinct 3d Self-Avoiding Walks of (n+1) steps from n steps

    lenWalks = len(walks_list)
#    print(lenWalks)

    updated_walks_list = []

    for i in range(lenWalks):
        checked_walks = walks_list[i]
        for t in range(trials):
            walks_temp = saw3dAddStep(checked_walks)
            if walks_temp in updated_walks_list:
#               print("overlap")
                pass
            else:
#               print("new walk")
                updated_walks_list.append(walks_temp)

#    numDistinctWalks = len(updated_walks_list)
#    distinctWalks_list = [updated_walks_list, numDistinctWalks]

#    return distinctWalks_list
    return updated_walks_list

