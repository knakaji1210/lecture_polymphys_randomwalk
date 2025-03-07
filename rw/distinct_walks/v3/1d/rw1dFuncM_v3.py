#calculation of statistics of 1d random walk

import numpy as np
import csv

def rw1dCountDistinctWalks(file_num):
    import_file_x = "./data/distinctWalks_1d_N{0}_x.csv".format(file_num)   # 読み込むcsvファイルの名前（1次元だけ読めば十分）
    fi = open(import_file_x, 'r', encoding = "utf-8-sig")               # csvファイルを読み込み、そこに含まれるwalkの数を数える
    reader = csv.reader(fi)
    totalNum = 0
    for row in reader:
        totalNum += 1
    fi.close()

    return totalNum

def rw1dCalcR(file_num):
    x_list = []
    y_list = []
    import_file_x = "./data/distinctWalks_1d_N{0}_x.csv".format(file_num)   # 読み込むcsvファイルの名前
    import_file_y = "./data/distinctWalks_1d_N{0}_y.csv".format(file_num)
    fi_x = open(import_file_x, 'r', encoding = "utf-8-sig")
    fi_y = open(import_file_y, 'r', encoding = "utf-8-sig")
    reader_x = csv.reader(fi_x)
    reader_y = csv.reader(fi_y)
    num_x = 0                            
    for row_x in reader_x:
        x_end = int(row_x[-1])
        x_list.append(x_end)
        num_x += 1
    fi_x.close()
    num_y = 0                            
    for row_y in reader_y:
        y_end = int(row_y[-1])
        y_list.append(y_end)
        num_y += 1
    fi_y.close()

    r2_list = [ x**2 + y**2 for x, y in zip(x_list, y_list) ]
    r2_mean = np.mean(r2_list)
    R = np.sqrt(r2_mean)

    return R