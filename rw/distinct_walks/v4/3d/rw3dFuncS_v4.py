# Functions to generate distinct 3d Random Walk
# np.savetxtでtxt書き出しを行うバージョン、完全に書き換え（250307）
# distinctWalks_1d_N1_x.txtとdistinctWalks_1d_N1_y.txtを用意する必要がある（N0をスタートにすると動かない）
# csvを使ったv3よりも圧倒的に速い

import numpy as np

def rw3dDistinctWalks(N):                                      # Degree of polymerizationが唯一の変数

# Function to obtain distinct 3d Random Walks of (n+1) steps from n steps

    fileNum = N                                                # 何番目のtxtファイルを読み込むか

    direction = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
    numDirections = direction.shape[0]                                 # 可能な移動ステップの数

    import_file_x = "./data/distinctWalks_3d_N{0}_x.txt".format(fileNum)    # 読み込むcsvファイルの名前  
    import_file_y = "./data/distinctWalks_3d_N{0}_y.txt".format(fileNum)
    import_file_z = "./data/distinctWalks_3d_N{0}_z.txt".format(fileNum)
    export_file_x = "./data/distinctWalks_3d_N{0}_x.txt".format(fileNum+1)  # 次のステップのcsvファイルの名前
    export_file_y = "./data/distinctWalks_3d_N{0}_y.txt".format(fileNum+1)
    export_file_z = "./data/distinctWalks_3d_N{0}_z.txt".format(fileNum+1)

    import_array = np.loadtxt(import_file_x, dtype=int)
    
    numWalks = import_array.shape[0]
    numSteps = import_array.shape[1]

    print('N = {0}, numWalks = '.format(fileNum), numWalks)

    export_array_x = []
    export_array_y = []
    export_array_z = []

    for i in range(numWalks):                                  # 数えたwalkの数だけ繰り返す
        if (i!=0 and i%1000 ==0):                               # 進行を確認するために追加
            print("repeated cycle =", i)       
        import_array_x = np.loadtxt(import_file_x, dtype=int, skiprows=i, max_rows=1)
        x_end = import_array_x[-1]
        import_array_y = np.loadtxt(import_file_y, dtype=int, skiprows=i, max_rows=1)
        y_end = import_array_y[-1]
        import_array_z = np.loadtxt(import_file_z, dtype=int, skiprows=i, max_rows=1)
        z_end = import_array_z[-1]
        for n in range(numDirections):                      # 可能な移動ステップの数だけ繰り返す
            step = direction[n]                    # num_stepsで選ばれた移動ステップを選ぶ
            x = x_end + step[0]                         # 新x座標を作成
            y = y_end + step[1]                         # 新y座標を作成
            z = z_end + step[2]                         # 新z座標を作成
            updated_x_array = np.append(import_array_x, x)     # 新x座標を追加
            updated_y_array = np.append(import_array_y, y)
            updated_z_array = np.append(import_array_z, z)
            export_array_x = np.append(export_array_x, updated_x_array)
            export_array_y = np.append(export_array_y, updated_y_array)
            export_array_z = np.append(export_array_z, updated_z_array)
    
    export_array_x.resize(numWalks*numDirections,numSteps+1)
    export_array_y.resize(numWalks*numDirections,numSteps+1)
    export_array_z.resize(numWalks*numDirections,numSteps+1)
    np.savetxt(export_file_x, export_array_x, fmt ='%.0f')
    np.savetxt(export_file_y, export_array_y, fmt ='%.0f')
    np.savetxt(export_file_z, export_array_z, fmt ='%.0f')
    numWalks_Last = export_array_x.shape[0]

    return numWalks_Last

