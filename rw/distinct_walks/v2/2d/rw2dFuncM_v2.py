#calculation of statistics of 2d random walk

import numpy as np
import rw2dFuncS_v2 as rws

def rw2dCalcR(walks_list):

    numDistinctWalks = len(walks_list)

    r2_list = []

    for i in range(numDistinctWalks):
            coordinate_list = walks_list[i]
#            print(coordinate_list)
            coordinate_list_end = coordinate_list[-1]
            r2 = coordinate_list_end[0]*coordinate_list_end[0] + coordinate_list_end[1]*coordinate_list_end[1]
            r2_list.append(r2)
    else:
        pass

    r2_mean = np.mean(r2_list)
    r2_std = np.std(r2_list)
    R = np.sqrt(r2_mean)

    result_list = [r2_list, R]

    return result_list
