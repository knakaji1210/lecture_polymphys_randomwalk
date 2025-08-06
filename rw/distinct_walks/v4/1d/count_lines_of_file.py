# https://magazine.techacademy.jp/magazine/20625
# をベースに作成

'''
How to use
% python3 count_lines_of _file.py args[1] args[2]
args[1] current DP
args[2] x or y or z
'''

import sys
import math

args = sys.argv

n = args[1]
c = args[2]

# 分割したいファイルとそのファイルのエンコードを設定
input_file_name = "./data/distinctWalks_1d_N{0}_{1}.txt".format(n,c)
file_encode = "shift_jis"
# file_encode = "utf-8"

input_file = open(input_file_name, encoding=file_encode)

numWalks = sum([1 for _ in input_file])

numSteps = math.log(numWalks, 4)


print("numWalks = {0} = 4^{1:.0f}".format(numWalks, numSteps))

input_file.close()