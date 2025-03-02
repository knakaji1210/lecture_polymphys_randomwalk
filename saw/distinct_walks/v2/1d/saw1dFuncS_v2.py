
# Functions to generate distinct 1d Self-Avoiding Walk


def saw1dAddStep(coordinate_list, num_branch):

# Functions to add a step to coordinate_list of 1d Self-Avoiding Walk

    len_coordinate = len(coordinate_list)

    updated_coordinate_list = [ coordinate_list[x] for x in range(len_coordinate)]
    coordinate_end = coordinate_list[-1]

    x, y = coordinate_end[0], coordinate_end[1]

    direction_list = ([1,0],[-1,0])

    step = direction_list[num_branch]
    x_temp = x + step[0]
    y_temp = y + step[1]
    coordinate_temp = [x_temp, y_temp]
    if coordinate_temp in coordinate_list:
        #print("failure")
        pass
    else:
        #print("sucsess")
        x = x_temp
        y = y_temp
        coordinate = [x, y]
        updated_coordinate_list.append(coordinate)

    return updated_coordinate_list


def saw1dDistinctWalks(walks_list):

# Function to obtain distinct 1d Self-Avoiding Walks of (n+1) steps from n steps

    lenWalks = len(walks_list)
#    print(lenWalks)

    num_branch = 2
    updated_walks_list = []

    for i in range(lenWalks):
        checked_walks = walks_list[i]
        check_len = len(checked_walks)
        for n in range(num_branch):
            walks_temp = saw1dAddStep(checked_walks, n)
            if len(walks_temp) == check_len + 1:
                updated_walks_list.append(walks_temp)

    return updated_walks_list

