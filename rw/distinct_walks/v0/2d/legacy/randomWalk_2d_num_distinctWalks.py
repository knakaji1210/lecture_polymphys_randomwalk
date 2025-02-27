# Calculation to necessary steps to list up total number of distinct 2d random walks

import numpy as np
from math import *
import rw2dFuncS2 as rws
import matplotlib.pyplot as plt

N = 5

totalNum_list = []

log_list = np.logspace(0, 6, 7, base=10)
n_list = [ int(x) for x in log_list ]
x_list = [ log10(x) for x in n_list ]

for n in n_list:

    distinctWalks_list = rws.rw2dDistinctWalks(N, n)

#    walks_list = distinctWalks_list[0]
    numDistinctWalks = distinctWalks_list[1]
    totalNum_list.append(numDistinctWalks)

fig = plt.figure()

ax = fig.add_subplot(111,title="number of trials", xlabel='log(n)', ylabel='total num')
ax.grid(axis='both', color="gray", lw=0.5)
ax.plot(x_list, totalNum_list)

fig.savefig("./png/randomWalk_2d_numberTrials.png", dpi=300)

plt.show()
