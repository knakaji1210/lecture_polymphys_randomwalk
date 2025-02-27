# Scaling of number of total distinct walks for 2d Random Walk 

import numpy as np
from math import *
import rw2dFuncS2 as rws
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

trials = 10**ex

start_time = time.process_time()

num = 0
num_list = []
totalNum_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)

    distinctWalks_list = rws.rw2dDistinctWalks(num, trials)

#    walks_list = distinctWalks_list[0]
    numDistinctWalks = distinctWalks_list[1]
    print('N = {0}, totalNum = {1:.0f}'.format(num,numDistinctWalks))
    totalNum_list.append(numDistinctWalks)


log_list = [ log10(x) for x in totalNum_list ]

# Least-squares fitting

fit_result, fit_error = np.polyfit(num_list, log_list, 1, cov=True)
exponent = fit_result[0]
intercept = fit_result[1]
exponent_error = np.sqrt(fit_error[0,0]) * 10**exponent
fit_func = np.poly1d(fit_result)(num_list)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total number of distinct walks = {0}'.format(numDistinctWalks))
print('total time = {0:.5f} s'.format(elapsed_time))

fig = plt.figure()

fig_title = "number of distinct walks (2d)"
result_text1 = "Total distinct walks = ({0:.2f}±{1:.2f})$^N$".format(10**exponent, exponent_error)
result_text2 = "$N_{{max}}$ = {0}, $T_{{comp}}$ = {1:.2f} s".format(N, elapsed_time)

ax = fig.add_subplot(111,title=fig_title, xlabel='$N$ steps', ylabel='Log(Total Number)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(num_list, log_list)
ax.plot(num_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text1)
fig.text(0.5, 0.16, result_text2)

savefile = "./png/randomWalk_2d_scaling_totalNum_N{0}.png".format(N)

fig.savefig(savefile, dpi=300)

plt.show()
