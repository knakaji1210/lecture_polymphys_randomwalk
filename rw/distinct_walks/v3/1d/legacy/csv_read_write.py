# csvの読み書きをテスト

import csv

file_num = 1

inport_file_x = "./data/file_{0}_x.csv".format(file_num)
inport_file_y = "./data/file_{0}_y.csv".format(file_num)

for i in range(2):
    with open(inport_file_x, encoding = "utf-8-sig") as fi:
        reader = csv.reader(fi)
        num = 0
        for low in reader:
            if num == i:
                print(low)
                x_list = [ int(x) for x in low ]
                print(x_list)
                x_list.append(2)
                export_file_x = "./data/file_{0}_x.csv".format(file_num+1)
                with open(export_file_x, 'a', encoding = "utf-8-sig") as fo:
                    writer = csv.writer(fo)
                    writer.writerow(x_list)
            num += 1
    with open(inport_file_y, encoding = "utf-8-sig") as fi:
        reader = csv.reader(fi)
        num = 0
        for low in reader:
            if num == i:
                print(low)
                y_list = [ int(x) for x in low ]
                print(y_list)
                y_list.append(5)
                export_file_y = "./data/file_{0}_y.csv".format(file_num+1)
                with open(export_file_y, 'a', encoding = "utf-8-sig") as fo:
                    writer = csv.writer(fo)
                    writer.writerow(y_list)
            num += 1