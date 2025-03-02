#calculation of statistics of 1d Self-Avoiding walk

import numpy as np
import saw1dFuncS_v2 as saws

def saw1dCalcR(walks_list):

    numDistinctWalks = len(walks_list)

    r2_list = []

    for i in range(numDistinctWalks):
            coordinate_list = walks_list[i]
#           print(coordinate_list)
            coordinate_list_end = coordinate_list[-1]
            r2 = coordinate_list_end[0]*coordinate_list_end[0]
            r2_list.append(r2)
    else:
        pass

    r2_mean = np.mean(r2_list)
    r2_std = np.std(r2_list)
    R = np.sqrt(r2_mean)

    result_list = [r2_list, R]

    return result_list
