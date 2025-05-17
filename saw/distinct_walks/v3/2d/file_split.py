# 大容量ファイルを分割するpythonプログラム
# https://zenn.dev/t_takaji/articles/d29814d01a8555
# をベースに作成

'''
How to use
% python3 file_split.py args[1] args[2]
args[1] current DP
args[2] x or y or z
'''

import sys

args = sys.argv

n = args[1]
c = args[2]

# 分割したいファイルとそのファイルのエンコードを設定
input_file_name = "./data/distinctWalks_2d_N{0}_{1}.txt".format(n,c)
output_file_name = "./data/distinctWalks_2d_N{0}_{1}_sp%d.txt".format(n,c)
file_encode = "shift_jis"
# file_encode = "utf-8"

# １ファイルあたりの行数
line_max = 1000000

# 初期化
line_index = 1
file_seqno = 1

# ファイルを読み込んでwhileで1行ずつ見ていく
input_file = open(input_file_name, encoding=file_encode)
output_file = open(output_file_name % file_seqno, "w", encoding=file_encode)
line = input_file.readline()

while line:
    if line_index > line_max:
        output_file.close()
        line_index = 1
        file_seqno += 1
        output_file = open(output_file_name % file_seqno, "w", encoding=file_encode)
    output_file.write(line)
    line_index += 1
    line = input_file.readline()

input_file.close()
output_file.close()