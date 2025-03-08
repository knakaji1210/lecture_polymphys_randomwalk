# Test of total distinct walks for 1d Self-Avoiding walk

import numpy as np
from math import *
import saw1dFuncS_v3 as saws

fileNum = 2
numWalks = 3

import_file_x = "./data/distinctWalks_1d_N{0}_x.txt".format(fileNum)    # 読み込むcsvファイルの名前  
import_file_y = "./data/distinctWalks_1d_N{0}_y.txt".format(fileNum)

for i in range(numWalks+1):
    import_array_x = np.loadtxt(import_file_x, dtype=int, skiprows=i, max_rows=1)
    import_array_y = np.loadtxt(import_file_y, dtype=int, skiprows=i, max_rows=1)
    print(import_array_x)
    print(import_array_y)
    coordinate_array = saws.xy2coordinate(import_array_x, import_array_y, numWalks)
    print(coordinate_array)