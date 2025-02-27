# Function to list up distinct 3d Random Walks

import numpy as np
from math import *
import rw3dFuncS2 as rws
import matplotlib.pyplot as plt

N = 5
trials = 10**5

num = 0
num_list = []
totalNum_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)

    distinctWalks_list = rws.rw3dDistinctWalks(num, trials)

#    walks_list = distinctWalks_list[0]
    numDistinctWalks = distinctWalks_list[1]
    totalNum_list.append(numDistinctWalks)

log_list = [ log10(x) for x in totalNum_list ]

# Least-squares fitting

fit_result = np.polyfit(num_list, log_list, 1)
exponent = fit_result[0]
intercept = fit_result[1]
fit_func = np.poly1d(fit_result)(num_list)

fig = plt.figure()

fig_title = "number of distinct walks (3d)"
result_text1 = "Total distinct walks = "+str(round(10**exponent, 3))+"^N"

ax = fig.add_subplot(111,title=fig_title, xlabel='N steps', ylabel='Log(Total Number)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(num_list, log_list)
ax.plot(num_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text1)

fig.savefig("./png/randomWalk_3d_totalNum.png", dpi=300)

plt.show()
