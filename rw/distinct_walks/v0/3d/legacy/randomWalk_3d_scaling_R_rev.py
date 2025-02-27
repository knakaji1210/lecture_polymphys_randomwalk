# Scaling of 3d Random Walk

import numpy as np
from math import *
import rw3dFuncM2 as rwm
import matplotlib.pyplot as plt
import time

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

try:
    ex = int(input('Max power exponent (default=5): '))
except ValueError:
    ex = 5

trials = 10**ex

start_time = time.process_time()

num = 0
num_list = []
R_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)

    result = rwm.rw3dCalcR(num,trials)
    R = result[1]
    R_list.append(R)

    # 進行ごとに時間を計測するように変更
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    print('n = {0}, t = {1:.5f} s'.format(n,elapsed_time))

log_n_list = [ log10(x) for x in num_list ]
log_R_list = [ log10(x) for x in R_list ]

# Least-squares fitting

fit_result = np.polyfit(log_n_list, log_R_list, 1)
exponent = fit_result[0]
intercept = fit_result[1]
fit_func = np.poly1d(fit_result)(log_n_list)

fig = plt.figure()

fig_title = "Scaling of R for 3-d Random Walk"
result_text = "Sqrt(<R2>) ~ N^("+str(round(exponent, 3))+")"

ax = fig.add_subplot(111,title=fig_title, xlabel='Log(N)', ylabel='Log(R)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(log_n_list, log_R_list)
ax.plot(log_n_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text)

fig.savefig("./png/randomWalk_3d_scaling_R.png", dpi=300)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total time = {0:.5f} s'.format(elapsed_time))

plt.show()
