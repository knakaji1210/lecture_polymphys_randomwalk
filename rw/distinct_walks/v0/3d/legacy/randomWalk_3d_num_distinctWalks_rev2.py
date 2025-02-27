# Calculation to necessary steps to list up total number of distinct 3d random walks

import numpy as np
from math import *
import rw3dFuncS2 as rws
import matplotlib.pyplot as plt
import time

try:
    N = int(input('Degree of polymerization (default=5): '))
except ValueError:
    N = 5

try:
    ex = int(input('Max power exponent (default=4): '))
except ValueError:
    ex = 4

start_time = time.process_time()

totalNum_list = []

log_list = np.logspace(0, ex, 2*ex+1, base=10)
n_list = [ int(x) for x in log_list ]
x_list = [ log10(x) for x in n_list ]

# 無駄な計算をしないようにforからwhileに変更してみたバージョン
i = 0
numDistinctWalks = 0
diff_numDistinctWalks = 1

while (i < len(n_list)) and (diff_numDistinctWalks > 0):
    n = n_list[i]
    distinctWalks_list = rws.rw3dDistinctWalks(N, n)

#    walks_list = distinctWalks_list[0]
    prev_numDistinctWalks = numDistinctWalks
    numDistinctWalks = distinctWalks_list[1]
    totalNum_list.append(numDistinctWalks)
    diff_numDistinctWalks = numDistinctWalks - prev_numDistinctWalks
    i += 1

    # 進行ごとに時間を計測するように変更
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    print('n = {0}, t = {1:.5f} s'.format(n,elapsed_time))

diff = len(x_list) - len(totalNum_list)
if diff != 0:
    del n_list[-diff:]
    del x_list[-diff:]

logTotalNum = log(numDistinctWalks, 6)
n_min = n_list[-1]
x_min = ceil(x_list[-1])

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total number of distinct walks = {0}'.format(numDistinctWalks))
print('total time = {0:.5f} s'.format(elapsed_time))
print('number of necessary trials = {0:.0f}'.format(n_min))

fig = plt.figure()

fig_title = "number of trials"
result_text1 = "N = {}".format(N)
result_text2 = "Total distinct walks = {0:.0f} = 6$^{{{1:.0f}}}$".format(numDistinctWalks, logTotalNum)
result_text3 = "$n_{{min}}$ = {0} < 10$^{{{1:.0f}}}$, $T_{{comp}}$ = {2:.2f} s".format(n_min, x_min, elapsed_time)

ax = fig.add_subplot(111,title=fig_title, xlabel='log($n$)', ylabel='total num')
ax.grid(axis='both', color="gray", lw=0.5)
ax.plot(x_list, totalNum_list, marker="o")
fig.text(0.2, 0.80, result_text1)
fig.text(0.2, 0.76, result_text2)
fig.text(0.2, 0.72, result_text3)

savefile = "./png/randomWalk_3d_numberTrials_N{0}.png".format(N)

fig.savefig(savefile, dpi=300)

plt.show()
