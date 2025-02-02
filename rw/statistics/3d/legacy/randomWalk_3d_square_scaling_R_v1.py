# Scaling of 3d Random Walk (square lattice model)

import numpy as np
from math import *
import rw3dFuncM_square as rwm
import matplotlib.pyplot as plt
import time

try:
    ex = int(input('Max power exponent (default=5): '))
except ValueError:
    ex = 5

try:
    M = int(input('Number of repetition (default=100): '))
except ValueError:
    M = 100

logM = log10(M)

start_time = time.process_time()

log_list = np.logspace(0, ex, 2*ex+1, base=10)
n_list = [ int(x) for x in log_list ]
x_list = [ log10(x) for x in n_list ]
R_list = []

# Calculation of Sqrt of R２mean

for n in n_list:
    coordinateM_list, resultM_list = rwm.rw3dFuncM(n, M)
    r2_mean = resultM_list[0]
    R = np.sqrt(r2_mean)
    R_list.append(R)
    # 進行ごとに時間を計測するように変更
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    print('n = {0}, t = {1:.5f} s'.format(n,elapsed_time))

y_list = [ log10(x) for x in R_list ]

# Least-squares fitting

fit_result = np.polyfit(x_list, y_list, 1)
exponent = fit_result[0]
intercept = fit_result[1]
fit_func = np.poly1d(fit_result)(x_list)

# Plot of R-N relationship

end_time = time.process_time()
elapsed_time = end_time - start_time

print('exponent for R = {0:.3f}'.format(exponent))
print('total time = {0:.5f} s'.format(elapsed_time))

fig_title = "Scaling of $R$ for 3-d Random Walk (square lattice model)"
result_text1 = "$R$ = <$r^2>^{{1/2}}$ ~ N$^{{{:.3f}}}$".format(exponent)
result_text2 = "$M$ = 10$^{{{0:.0f}}}$, $T_{{comp}}$ = {1:.2f} s".format(logM, elapsed_time)

fig = plt.figure()
ax = fig.add_subplot(111,title=fig_title, xlabel='Log($N$)', ylabel='Log($R$)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(x_list, y_list)
ax.plot(x_list, fit_func, color="black")
fig.text(0.55, 0.20, result_text1)
fig.text(0.55, 0.15, result_text2)

savefile = "./png/randomWalk_3d_square_scaling_N{0:.0f}M{1:.0f}.png".format(ex, logM)

fig.savefig(savefile, dpi=300)

plt.show()