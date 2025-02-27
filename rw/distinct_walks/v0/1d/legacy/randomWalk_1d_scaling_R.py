# Scaling of 1d Random Walk

import numpy as np
from math import *
import rw1dFuncM2 as rwm
import matplotlib.pyplot as plt

N = 10
trials = 10**5

num = 0
num_list = []
R_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)

    result = rwm.rw1dCalcR(num,trials)
    R = result[1]
    R_list.append(R)

log_n_list = [ log10(x) for x in num_list ]
log_R_list = [ log10(x) for x in R_list ]

# Least-squares fitting

fit_result = np.polyfit(log_n_list, log_R_list, 1)
exponent = fit_result[0]
intercept = fit_result[1]
fit_func = np.poly1d(fit_result)(log_n_list)

fig = plt.figure()

fig_title = "Scaling of R for 1-d Random Walk"
result_text = "Sqrt(<R2>) ~ N^("+str(round(exponent, 3))+")"

ax = fig.add_subplot(111,title=fig_title, xlabel='Log(N)', ylabel='Log(R)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(log_n_list, log_R_list)
ax.plot(log_n_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text)

fig.savefig("./png/randomWalk_1d_scaling_R.png", dpi=300)

plt.show()
