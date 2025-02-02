# Scaling of 3d Random Walk (square lattice model)

import numpy as np
from math import *
import rw3dFuncM_square as rwm
import matplotlib.pyplot as plt

log_list = np.logspace(1, 5, 17, base=10)
n_list = [ int(x) for x in log_list ]
x_list = [ log10(x) for x in n_list ]
R_list = []

# Calculation of Sqrt of R２mean

M = 100

for n in n_list:
    coordinateM_list, resultM_list = rwm.rw3dFuncM(n, M)
    r2_mean = resultM_list[0]
    R = np.sqrt(r2_mean)
    R_list.append(R)

y_list = [ log10(x) for x in R_list ]

# Least-squares fitting

fit_result = np.polyfit(x_list, y_list, 1)
exponent = fit_result[0]
intercept = fit_result[1]
fit_func = np.poly1d(fit_result)(x_list)

# Plot of R-N relationship

fig_title = "Scaling of R for 3-d Random Walk (square lattice model)"
result_text1 = "Sqrt(<R2>) ~ N^("+str(round(exponent, 3))+")"
result_text2 = "M = "+str(M)

fig = plt.figure()
ax = fig.add_subplot(111,title=fig_title, xlabel='Log(N)', ylabel='Log(R)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(x_list, y_list)
ax.plot(x_list, fit_func, color="black")
fig.text(0.6, 0.20, result_text1)
fig.text(0.6, 0.15, result_text2)

fig.savefig("./png/randomWalk_3d_square_scaling.png", dpi=300)

plt.show()