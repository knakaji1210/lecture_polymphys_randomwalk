#calculation of statistics of 2d random walk

import numpy as np
import rw2dFuncS2 as rws

def rw2dCalcR(N, M):

    r2_list = []

    distinctWalks_list = rws.rw2dDistinctWalks(N,M)

    walks_list = distinctWalks_list[0]
    numDistinctWalks = distinctWalks_list[1]


    if numDistinctWalks == 4**N:
        for x in range(numDistinctWalks):
            walk_list = walks_list[x]
#            print(walk_list)
            walk_end = walk_list[-1]
#            print(walk_end)
            r2 = walk_end[0]*walk_end[0] + walk_end[1]*walk_end[1]
            r2_list.append(r2)
    else:
        pass

    r2_mean = np.mean(r2_list)
    r2_std = np.std(r2_list)
    R = np.sqrt(r2_mean)

    result_list = [r2_list, R]

    return result_list
