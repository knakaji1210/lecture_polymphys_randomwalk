# Scaling of end-to-end distance for 2d Random Walk 

import numpy as np
from math import *
import rw2dFuncM_v4 as rwm
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import time

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

start_time = time.process_time()

num = 0
n_list = []
R_list = []

for n in range(N):
    num = num + 1
    n_list.append(num)
    R = rwm.rw2dCalcR(num)
    print('N = {0}, R = {1:.3f}'.format(num,R))
    R_list.append(R)

n_list.insert(0, 0)
R_list.insert(0, 0)

R_max = np.max(R_list)

# Least-squares fitting
def fitFunc(x, a, b):
    return  a * x**b

param, cov = curve_fit(fitFunc, n_list, R_list, p0=[0.4, 0.5])
param_err = np.sqrt(np.diag(cov))

exponent = param[1]
exp_err = param_err[1]

n_fit_list = np.linspace(0, np.max(n_list), 10*len(n_list))
fit_func = [ param[0] * x ** param[1] for x in n_fit_list ]

end_time = time.process_time()
elapsed_time = end_time - start_time
print('N_max = {0}, t = {1:.5f} s'.format(N,elapsed_time))

fig = plt.figure()

fig_title = "Scaling of $R$ for 2-d Random Walk"
result_text1 = "$R$ = <$r^2>^{{1/2}}$ ~ $N^{{{{{0:.3f}}}±{{{1:.3f}}}}}$".format(exponent,exp_err)
result_text2 = "$N_{{max}}$ = {0}, $T_{{comp}}$ = {1:.2f} s".format(N, elapsed_time)

ax = fig.add_subplot(111,title=fig_title, xlabel='$N$', ylabel='$R$', xlim=(-0.5, 1.05*N), ylim=(-0.5, 1.05*R_max))
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(n_list, R_list)
ax.plot(n_fit_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text1)
fig.text(0.5, 0.16, result_text2)

savefile = "./png/randomWalk_2d_scaling_R_N{0}.png".format(N)

fig.savefig(savefile, dpi=300)

plt.show()