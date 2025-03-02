# Functions to generate distinct 3d Random Walk

def rw3dAddStep(coordinate_list, num_branch):

# Functions to add a step to coordinate_list of 3d Random Walk

    len_coordinate = len(coordinate_list)

    updated_coordinate_list = [ coordinate_list[x] for x in range(len_coordinate)]
    coordinate_end = coordinate_list[-1]

    x, y, z = coordinate_end[0], coordinate_end[1], coordinate_end[0]

    direction_list = ([1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1])

    step = direction_list[num_branch]
    x = x + step[0]
    y = y + step[1]
    z = z + step[2]
    coordinate = [x, y, z]
    updated_coordinate_list.append(coordinate)

    return updated_coordinate_list



def rw3dDistinctWalks(walks_list):

# Function to obtain distinct 3d Random Walks of (n+1) steps from n steps

    lenWalks = len(walks_list)
#    print(lenWalks)

    num_branch = 6
    updated_walks_list = []

    for i in range(lenWalks):
        checked_walks = walks_list[i]
        for n in range(num_branch):
            walks_temp = rw3dAddStep(checked_walks, n)
            updated_walks_list.append(walks_temp)

#    numDistinctWalks = len(updated_walks_list)
#    distinctWalks_list = [updated_walks_list, numDistinctWalks]

#    return distinctWalks_list
    return updated_walks_list

