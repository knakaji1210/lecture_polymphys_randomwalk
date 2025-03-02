# Scaling of end-to-end distance for 2d Random Walk 

import numpy as np
from math import *
import rw2dFuncS4 as rws
import rw2dFuncM4 as rwm
import matplotlib.pyplot as plt
import time

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

start_time = time.process_time()

walks_list = [[[0, 0]]]
num = 0
num_list = []
R_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)
    walks_list = rws.rw2dDistinctWalks(walks_list)
    result_list = rwm.rw2dCalcR(walks_list)
    R = result_list[1]
    print('N = {0}, R = {1:.3f}'.format(num,R))
    R_list.append(R)

log_n_list = [ log10(x) for x in num_list ]
log_R_list = [ log10(x) for x in R_list ]

# Least-squares fitting

fit_result = np.polyfit(log_n_list, log_R_list, 1)
exponent = fit_result[0]
intercept = fit_result[1]
fit_func = np.poly1d(fit_result)(log_n_list)

end_time = time.process_time()
elapsed_time = end_time - start_time
print('N_max = {0}, t = {1:.5f} s'.format(N,elapsed_time))

fig = plt.figure()

fig_title = "Scaling of $R$ for 2-d Random Walk"
result_text1 = "$R$ = <$r^2>^{{1/2}}$ ~ $N^{{{:.3f}}}$".format(exponent)
result_text2 = "$N_{{max}}$ = {0}, $T_{{comp}}$ = {1:.5f} s".format(N, elapsed_time)

ax = fig.add_subplot(111,title=fig_title, xlabel='Log($N$)', ylabel='Log($R$)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(log_n_list, log_R_list)
ax.plot(log_n_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text1)
fig.text(0.5, 0.16, result_text2)

savefile = "./png/randomWalk_2d_scaling_R_N{0}.png".format(N)

fig.savefig(savefile, dpi=300)

plt.show()
