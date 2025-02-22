# Function to calculate properties of 1d Random Walk (multiple run)

import numpy as np
import rw1dFuncS_v1 as rws

def rw1dFuncM(N, M):

    r2_list = []
    r_list = []
    xt_list = []
    yt_list = []
        
    for m in range(M):
        if (m!=0 and m%10000 ==0):     # added to check the progress
            print(m)
        coordinate_list, result_list = rws.rw1dFuncS(N)
        r2 = result_list[0]
        r = result_list[1]
        x_list = coordinate_list[0]
        y_list = coordinate_list[1]
        r2_list.append(r2)
        r_list.append(r)
        xt_list.append(x_list[-1])
        yt_list.append(y_list[-1])

    coordinateM_list = [xt_list, yt_list, r2_list, r_list]
    
    r2_mean = np.mean(r2_list)
    r2_std = np.std(r2_list)
    r_mean = np.mean(r_list)
    r_std = np.std(r_list)
    x_mean = np.mean(xt_list)
    x_std = np.std(xt_list)
    y_mean = np.mean(yt_list)
    y_std = np.std(yt_list)

    resultM_list = [r2_mean, r2_std, r_mean, r_std, x_mean, x_std, y_mean, y_std]

    return coordinateM_list, resultM_list