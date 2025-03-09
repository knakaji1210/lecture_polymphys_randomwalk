#calculation of statistics of 3d Self-Avoiding walk

import numpy as np

def saw3dCountDistinctWalks(fileNum):    
    import_file_x = "./data/distinctWalks_3d_N{0}_x.txt".format(fileNum)   # 読み込むtxtファイルの名前（1次元だけ読めば十分）
    import_array = np.loadtxt(import_file_x, dtype=int)                    # txtファイルを読み込む
    numWalks = import_array.shape[0]                                       # そこに含まれるwalkの数を数える
    return numWalks

def saw3dCalcR(fileNum):
    numWalks = saw3dCountDistinctWalks(fileNum)
    x_list = []
    y_list = []
    z_list = []
    import_file_x = "./data/distinctWalks_3d_N{0}_x.txt".format(fileNum)   # 読み込むtxtファイルの名前
    import_file_y = "./data/distinctWalks_3d_N{0}_y.txt".format(fileNum)
    import_file_z = "./data/distinctWalks_3d_N{0}_z.txt".format(fileNum)
    for i in range(numWalks):                                  # 数えたwalkの数だけ繰り返す
        if (i!=0 and i%1000 ==0):                               # 進行を確認するために追加
            print("repeated cycle =", i) 
        import_array_x = np.loadtxt(import_file_x, dtype=int, skiprows=i, max_rows=1)
        import_array_y = np.loadtxt(import_file_y, dtype=int, skiprows=i, max_rows=1)
        import_array_z = np.loadtxt(import_file_z, dtype=int, skiprows=i, max_rows=1)
        x_end = import_array_x[-1]
        y_end = import_array_y[-1]
        z_end = import_array_y[-1]
        x_list.append(x_end)
        y_list.append(y_end)
        z_list.append(z_end)
                       
    r2_list = [ x**2 + y**2 + z**2 for x, y, z in zip(x_list, y_list, z_list) ]
    r2_mean = np.mean(r2_list)
    R = np.sqrt(r2_mean)

    return R