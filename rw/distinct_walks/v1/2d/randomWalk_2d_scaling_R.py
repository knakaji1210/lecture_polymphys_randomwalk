# Scaling of end-to-end distance for 2d Random Walk 

import numpy as np
from math import *
import rw2dFuncS3 as rws
import rw2dFuncM3 as rwm
import matplotlib.pyplot as plt

N = 6
trials = 30

walks_list = [[[0, 0]]]
num = 0
num_list = []
R_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)
    walks_list = rws.rw2dDistinctWalks(walks_list, trials)
    result_list = rwm.rw2dCalcR(walks_list)
    R = result_list[1]
    R_list.append(R)

log_n_list = [ log10(x) for x in num_list ]
log_R_list = [ log10(x) for x in R_list ]

# Least-squares fitting

fit_result = np.polyfit(log_n_list, log_R_list, 1)
exponent = fit_result[0]
intercept = fit_result[1]
fit_func = np.poly1d(fit_result)(log_n_list)

fig = plt.figure()

fig_title = "Scaling of R for 2-d Random Walk"
result_text = "Sqrt(<R2>) ~ N^("+str(round(exponent, 3))+")"

ax = fig.add_subplot(111,title=fig_title, xlabel='Log(N)', ylabel='Log(R)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(log_n_list, log_R_list)
ax.plot(log_n_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text)

fig.savefig("./png/randomWalk_2d_scaling_R.png", dpi=300)

plt.show()
