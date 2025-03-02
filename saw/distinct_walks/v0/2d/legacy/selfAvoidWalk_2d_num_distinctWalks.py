# Calculation to necessary steps to list up total number of distinct 2d self-avoiding walks

import numpy as np
from math import *
import saw2dFuncS2 as saws
import matplotlib.pyplot as plt

N = 5

totalNum_list = []

log_list = np.logspace(0, 5, 6, base=10)
n_list = [ int(x) for x in log_list ]
x_list = [ log10(x) for x in n_list ]

for n in n_list:

    distinctWalks_list = saws.saw2dDistinctWalks(N, n)

#    walks_list = distinctWalks_list[0]
    numDistinctWalks = distinctWalks_list[1]
    totalNum_list.append(numDistinctWalks)
    print("n = "+str(n))

fig = plt.figure()

ax = fig.add_subplot(111,title="number of trials", xlabel='log(n)', ylabel='total num')
ax.grid(axis='both', color="gray", lw=0.5)
ax.plot(x_list, totalNum_list)

fig.savefig("./png/selfAvoidWalk_2d_numberTrials.png", dpi=300)

plt.show()
