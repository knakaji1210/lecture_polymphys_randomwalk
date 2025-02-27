# Calculation to necessary steps to list up total number of distinct 1d random walks

import numpy as np
from math import *
import rw1dFuncS2 as rws
import matplotlib.pyplot as plt
import time

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

try:
    ex = int(input('Max power exponent (default=5): '))
except ValueError:
    ex = 5

start_time = time.process_time()

totalNum_list = []

log_list = np.logspace(0, ex, 2*ex+1, base=10)
n_list = [ int(x) for x in log_list ]
x_list = [ log10(x) for x in n_list ]

for n in n_list:

    distinctWalks_list = rws.rw1dDistinctWalks(N, n)

#    walks_list = distinctWalks_list[0]
    numDistinctWalks = distinctWalks_list[1]
    totalNum_list.append(numDistinctWalks)

    # 進行ごとに時間を計測するように変更
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    print('n = {0}, t = {1:.5f} s'.format(n,elapsed_time))

fig = plt.figure()

ax = fig.add_subplot(111,title="number of trials", xlabel='log(n)', ylabel='total num')
ax.grid(axis='both', color="gray", lw=0.5)
ax.plot(x_list, totalNum_list)

fig.savefig("./png/randomWalk_1d_numberTrials.png", dpi=300)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total number of distinct walks = {0}'.format(totalNum_list[-1]))
print('total time = {0:.5f} s'.format(elapsed_time))

plt.show()
