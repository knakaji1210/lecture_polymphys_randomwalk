# Function to calculate properties of 1d Random Walk (multiple run)
# pythonのリストで書いたオリジナルをnp.ndarrayに置き換える試み（250214）

import numpy as np
import rw1dFuncS_ndarray as rws

def rw1dFuncM(N, M):

    nan = np.nan

    ini_array = np.full(M, nan)         # nanからなる配列を作成
    xt_array = np.copy(ini_array)       # xt_arrayとしてコピー 
    yt_array = np.copy(ini_array)       # yt_arrayとしてコピー
    r2_array  = np.copy(ini_array)      # r_arrayとしてコピー 
        
    for m in range(M):
        if (m!=0 and m%10000 ==0):     # added to check the progress
            print("repeated cycle =", m)
        coordinateS_array = rws.rw1dFuncS(N)
        xt = coordinateS_array[0][-1]
        yt = coordinateS_array[1][-1]
        r2 = xt**2 + yt**2
        np.put(xt_array, m, xt)           # xt_arrayのm番目をxt（x_terminal）の値で更新
        np.put(yt_array, m, yt)
        np.put(r2_array, m, r2)

    coordinateM_array = np.concatenate([xt_array, yt_array, r2_array], 0).reshape(3,M)
    
    return coordinateM_array