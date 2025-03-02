# Scaling of number of total distinct walks for 2d Self-Avoiding Walk 

import numpy as np
from math import *
import saw2dFuncS_v2 as saws
import matplotlib.pyplot as plt
import time
from scipy.optimize import curve_fit

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

start_time = time.process_time()

walks_list = [[[0, 0]]]
num = 0
num_list = []
totalNum_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)
    walks_list = saws.saw2dDistinctWalks(walks_list)
    totalNum = len(walks_list)
    print('N = {0}, n_tot = {1:.0f}'.format(num,totalNum))
    totalNum_list.append(totalNum)

log_list = [ log10(x) for x in totalNum_list ]

np.savetxt("./data/num_steps.txt", num_list, fmt='%5.f')
np.savetxt("./data/num_distinctwalks.txt", totalNum_list, fmt='%5.f')
np.savetxt("./data/loog_num_distinctwalks.txt", log_list, fmt='%.3e')

# Least-squares fitting

#fit_result = np.polyfit(num_list, log_list, 1)
#exponent = fit_result[0]
#intercept = fit_result[1]
#fit_func = np.poly1d(fit_result)(num_list)

def fitFunc(x, a, b):
    return  a * x + (b - 1) * np.log10(x)

# N = 1, 2, 3を除外してフィッティングすることも試してみたが、係数はむしろ理論値から遠ざかった。
#num_list_sub = num_list[2:]
#log_list_sub = log_list[2:]
#param, cov = curve_fit(fitFunc, num_list_sub, log_list_sub, p0=[0.4, 1.3])

param, cov = curve_fit(fitFunc, num_list, log_list, p0=[0.4, 1.3])
param_err = np.sqrt(np.diag(cov))
#print(param, param_err)

fit_func = [ param[0] * x + (param[1] - 1) * np.log10(x) for x in num_list ]

end_time = time.process_time()
elapsed_time = end_time - start_time
print('N_max = {0}, t = {1:.5f} s'.format(N,elapsed_time))

fig = plt.figure()

fig_title = "Number of Distinct Walks for 2-d Self-Avoiding Walk"
result_text1 = "$n_{{tot}}$ = ({0:.2f}±{1:.2f})$^N$ $N^{{{{({2:.2f}±{3:.2f})}}-1}}$".format(10**param[0], 10**param_err[0], param[1], param_err[1])
result_text2 = "$N_{{max}}$ = {0}, $T_{{comp}}$ = {1:.2f} s".format(N, elapsed_time)

ax = fig.add_subplot(111,title=fig_title, xlabel='$N$', ylabel='Log($n_{{tot}}$)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(num_list, log_list)
ax.plot(num_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text1)
fig.text(0.5, 0.16, result_text2)

savefile = "./png/selfAvoidingWalk_2d_scaling_totalNum_N{0}.png".format(N)

fig.savefig(savefile, dpi=300)

plt.show()
