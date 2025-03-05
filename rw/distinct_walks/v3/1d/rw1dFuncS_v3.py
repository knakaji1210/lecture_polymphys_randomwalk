# Functions to generate distinct 1d Random Walk
# csv書き出しを行うバージョン、完全に書き換え（250304）
# distinctWalks_N0_x.csvとdistinctWalks_N0_y.csvを用意する必要がある
# 間違いない動作を確認している最終バージョン
# ただし、file I/Oの繰り返しが多いためかとても遅い

import csv
import numpy as np

def rw1dDistinctWalks(N):                                       # Degree of polymerizationが唯一の変数

# Function to obtain distinct 1d Random Walks of (n+1) steps from n steps

    file_num = N                                                # 何番目のcsvファイルを読み込むか

    direction_list = ([1,0],[-1,0])
    num_steps = len(direction_list)                             # 可能な移動ステップの数

    import_file_x = "./data/distinctWalks_N{0}_x.csv".format(file_num)    # 読み込むcsvファイルの名前  
    import_file_y = "./data/distinctWalks_N{0}_y.csv".format(file_num)
    export_file_x = "./data/distinctWalks_N{0}_x.csv".format(file_num+1)  # 次のステップのcsvファイルの名前
    export_file_y = "./data/distinctWalks_N{0}_y.csv".format(file_num+1)

    fi = open(import_file_x, 'r', encoding = "utf-8-sig")       # 準備としてcsvファイルを読み込み、そこに含まれるwalkの数を数える
    reader = csv.reader(fi)
    totalNum = 0
    for row in reader:
        totalNum += 1
    fi.close()

    print('N = {0}, totalNum = '.format(file_num), totalNum)

    for i in range(totalNum):                                  # 数えたwalkの数だけ繰り返す
        fi_x = open(import_file_x, 'r', encoding = "utf-8-sig")
        fi_y = open(import_file_y, 'r', encoding = "utf-8-sig")        
        reader_x = csv.reader(fi_x)
        reader_y = csv.reader(fi_y)
        num_x = 0                                               # 指定した行だけ読み込むためのインデックス                            
        for row_x in reader_x:
            if num_x == i:                                      # 指定行だけ読み込むための条件文
                x_list = [ int(x) for x in row_x ]
                x_end = x_list[-1]
            num_x += 1
        num_y = 0
        for row_y in reader_y:                 
            if num_y == i:
                y_list = [ int(y) for y in row_y ]
                y_end = y_list[-1]
            num_y += 1
        fi_x.close()
        fi_y.close()
        for n in range(num_steps):                      # 可能な移動ステップの数だけ繰り返す
            updated_x_list = np.copy(x_list).tolist()   # x_listのコピーを作成、tolistにしないと後ろのappendができない
            updated_y_list = np.copy(y_list).tolist()
            step = direction_list[n]                    # num_stepsで選ばれた移動ステップを選ぶ
            x = x_end + step[0]                         # 新x座標を作成
            y = y_end + step[1]                         # 新y座標を作成
            updated_x_list.append(x)                    # 新x座標を追加
            updated_y_list.append(y)
            fo_x = open(export_file_x, 'a')
            fo_y = open(export_file_y, 'a')
            writer_x = csv.writer(fo_x)
            writer_y = csv.writer(fo_y)
            writer_x.writerow(updated_x_list)           # 新x座標を含むupdated_x_listをcsvファイルに書き込み
            writer_y.writerow(updated_y_list)
            fo_x.close()
            fo_y.close()
