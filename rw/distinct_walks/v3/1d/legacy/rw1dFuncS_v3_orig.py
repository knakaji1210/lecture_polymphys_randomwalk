# Functions to generate distinct 1d Random Walk
# csv書き出しを行うバージョン、完全に書き換え（250304）
# file_0_x.csvとfile_0_y.csvを用意する必要がある

import csv
import numpy as np

def rw1dDistinctWalks(file_num):                                # 何番目のcsvファイルを読み込むかだけが変数

# Function to obtain distinct 1d Random Walks of (n+1) steps from n steps

    direction_list = ([1,0],[-1,0])
    num_steps = len(direction_list)                             # 可能な移動ステップの数

    import_file_x = "./data/file_{0}_x.csv".format(file_num)    # 読み込むcsvファイルの名前  
    import_file_y = "./data/file_{0}_y.csv".format(file_num)

    with open(import_file_x, encoding = "utf-8-sig") as fi:     # 準備としてcsvファイルを読み込み、そこに含まれるwalkの数を数える
        reader = csv.reader(fi)
        num_walks = 0
        for low in reader:
            num_walks += 1

    for i in range(num_walks):                                  # 数えたwalkの数だけ繰り返す
        with open(import_file_x, encoding = "utf-8-sig") as fi:
            reader = csv.reader(fi)
            num = 0                                             # 指定した行だけ読み込むためのインデックス
            for low in reader:
                if num == i:                                    # 上記のための条件文
                    x_list = [ int(x) for x in low ]
                    x_end = x_list[-1]                          # 最後のx座標を抽出
                    export_file_x = "./data/file_{0}_x.csv".format(file_num+1)  # 次のステップのcsvファイルの名前
                    for n in range(num_steps):                      # 可能な移動ステップの数だけ繰り返す
                        updated_x_list = np.copy(x_list).tolist()   # x_listのコピーを作成、tolistにしないと後ろのappendができない
                        step = direction_list[n]                    # num_stepsで選ばれた移動ステップを選ぶ
                        x = x_end + step[0]                         # 新x座標を作成
                        updated_x_list.append(x)                    # 新x座標を追加
                        with open(export_file_x, 'a', encoding = "utf-8-sig") as fo:
                            writer = csv.writer(fo)
                            writer.writerow(updated_x_list)         # 新x座標を含むupdated_x_listをcsvファイルに書き込み
                num += 1
        with open(import_file_y, encoding = "utf-8-sig") as fi:     # 同じことをy座標についても繰り返す
            reader = csv.reader(fi)
            num = 0
            for low in reader:
                if num == i:
                    y_list = [ int(y) for y in low ]
                    y_end = y_list[-1]
                    export_file_y = "./data/file_{0}_y.csv".format(file_num+1)
                    for n in range(num_steps):
                        updated_y_list = np.copy(y_list).tolist()
                        step = direction_list[n]
                        y = y_end + step[1]
                        updated_y_list.append(y)                         # 新y座標を作成
                        with open(export_file_y, 'a', encoding = "utf-8-sig") as fo:
                            writer = csv.writer(fo)
                            writer.writerow(updated_y_list)
                num += 1