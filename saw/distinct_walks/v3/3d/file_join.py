# 分割されたファイルを結合するpythonプログラム
# https://pydocument.hatenablog.com/entry/2023/03/30/231011
# をベースに作成

'''
How to use
% python3 file_join.py args[1] args[2]
args[1] current DP
args[2] x or y or z
'''

import sys
import glob

args = sys.argv

n = args[1]
c = args[2]

input_file_name = "./data/distinctWalks_3d_N{0}_{1}_sp*.txt".format(n,c)
output_file_name = "./data/distinctWalks_3d_N{0}_{1}.txt".format(n,c)

# 結合対象ファイルリスト取得: 'input_file_name'で指定した全ての.txtファイルを取得
file_list = glob.glob(input_file_name)
file_list.sort()        # 何故かわからないが、globだけだとリストの順番が入れ替わってしまうため

# 出力ファイルを開く: 'output_file_name'で指定したファイルに書き込みモードで開く
with open(output_file_name, "w") as outfile:
    # 各ファイルを読み込み、出力ファイルに書き込む
    for file_name in file_list:
        with open(file_name, "r") as infile:
            outfile.write(infile.read())