# Scaling of number of total distinct walks for 1d Self-Avoiding Walk 

import numpy as np
from math import *
import saw1dFuncM_v3 as sawm
import matplotlib.pyplot as plt
import time

try:
    N = int(input('Current Max DP: '))
except ValueError:
    N = 10

start_time = time.process_time()

num = 0
num_list = []
numWalks_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)
    numWalks = sawm.saw1dCountDistinctWalks(num)
    print('N = {0}, n_tot = {1:.0f}'.format(num,numWalks))
    numWalks_list.append(numWalks)

log_list = [ log10(x) for x in numWalks_list ]

# Least-squares fitting

fit_result, fit_error = np.polyfit(num_list, log_list, 1, cov=True)
exponent = fit_result[0]
intercept = fit_result[1]
exponent_error = np.sqrt(fit_error[0,0]) * 10**exponent
fit_func = np.poly1d(fit_result)(num_list)

end_time = time.process_time()
elapsed_time = end_time - start_time
print('N_max = {0}, t = {1:.5f} s'.format(N,elapsed_time))

fig = plt.figure()

fig_title = "Number of Distinct Walks for 1-d Self-Avoiding Walk"
result_text1 = "$n_{{tot}}$ = {0:.1f} x ({1:.2f}±{2:.2f})$^N$".format(10**intercept, 10**exponent, exponent_error)
result_text2 = "$N_{{max}}$ = {0}, $T_{{comp}}$ = {1:.2f} s".format(N, elapsed_time)

ax = fig.add_subplot(111,title=fig_title, xlabel='$N$', ylabel='Log($n_{{tot}}$)', xlim=(0, 1.05*N))
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(num_list, log_list)
ax.plot(num_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text1)
fig.text(0.5, 0.16, result_text2)

savefile = "./png/selfAvoidingWalk_1d_scaling_totalNum_N{0}.png".format(N)

fig.savefig(savefile, dpi=300)

plt.show()
