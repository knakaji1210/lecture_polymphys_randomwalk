
# Functions to generate distinct 3d Self-Avoiding Walk


def saw3dAddStep(coordinate_list, num_branch):

# Functions to add a step to coordinate_list of 3d Self-Avoiding Walk

    len_coordinate = len(coordinate_list)

    updated_coordinate_list = [ coordinate_list[x] for x in range(len_coordinate)]
    coordinate_end = coordinate_list[-1]

    x, y, z = coordinate_end[0], coordinate_end[1], coordinate_end[2]

    direction_list = ([1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1])

    step = direction_list[num_branch]
    x_temp = x + step[0]
    y_temp = y + step[1]
    z_temp = z + step[2]
    coordinate_temp = [x_temp, y_temp, z_temp]
    if coordinate_temp in coordinate_list:
#       print("failure")
        pass
    else:
#       print("sucsess")
        x = x_temp
        y = y_temp
        z = z_temp
        coordinate = [x, y, z]
        updated_coordinate_list.append(coordinate)

    return updated_coordinate_list


def saw3dDistinctWalks(walks_list):

# Function to obtain distinct 3d Self-Avoiding Walks of (n+1) steps from n steps

    lenWalks = len(walks_list)
#    print(lenWalks)

    num_branch = 6
    updated_walks_list = []

    for i in range(lenWalks):
        checked_walks = walks_list[i]
        check_len = len(checked_walks)
        for n in range(num_branch):
            walks_temp = saw3dAddStep(checked_walks, n)
            if len(walks_temp) == check_len + 1:
                updated_walks_list.append(walks_temp)

    return updated_walks_list

