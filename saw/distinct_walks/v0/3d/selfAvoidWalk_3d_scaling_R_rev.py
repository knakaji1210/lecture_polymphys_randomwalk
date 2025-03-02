# Scaling of 3d Self-Avoiding Walk

import numpy as np
from math import *
import saw3dFuncM2 as sawm
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
R_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)

    result = sawm.saw3dCalcR(num,trials)
    R = result[1]
    print('N = {0}, R = {1:.3f}'.format(num,R))
    R_list.append(R)

log_n_list = [ log10(x) for x in num_list ]
log_R_list = [ log10(x) for x in R_list ]

# Least-squares fitting

fit_result, fit_error = np.polyfit(log_n_list, log_R_list, 1, cov=True)
exponent = fit_result[0]
intercept = fit_result[1]
exponent_error = np.sqrt(fit_error[0,0])
fit_func = np.poly1d(fit_result)(log_n_list)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('N_max = {0}, t = {1:.5f} s'.format(N,elapsed_time))

fig = plt.figure()

fig_title = "Scaling of $R$ for 3-d Self-Avoiding Walk"
result_text1 = "$R$ = <$r^2>^{{1/2}}$ ~ $N^{{{{{0:.3f}}}±{{{1:.3f}}}}}$".format(exponent,exponent_error)
result_text2 = "$N_{{max}}$ = {0}, $T_{{comp}}$ = {1:.2f} s".format(N, elapsed_time)

ax = fig.add_subplot(111,title=fig_title, xlabel='Log($N$)', ylabel='Log($R$)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(log_n_list, log_R_list)
ax.plot(log_n_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text1)
fig.text(0.5, 0.16, result_text2)

savefile = "./png/selfAvoidingWalk_3d_scaling_R_N{0}.png".format(N)

fig.savefig(savefile, dpi=300)

plt.show()
