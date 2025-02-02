# Scaling of 2d Random Walk (Triangular Lattice model)

import numpy as np
import matplotlib.pyplot as plt
from math import *
import rwFunc_triangle

log_list = np.logspace(1, 5, 19, base=10)
n_list = [ int(x) for x in log_list ]
x_list = [ log10(x) for x in n_list ]
r_list = []

for n in n_list:
    r = rwFunc_triangle.calc_rmean(n)
    r_list.append(r)

y_list = [ log10(x) for x in r_list ]

# Least-squares fitting

fit_result = np.polyfit(x_list, y_list, 1)
exponent = fit_result[0]
intercept = fit_result[1]
fit_func = np.poly1d(fit_result)(x_list)

# Plot of R-N relationship

fig_title = "Scaling of R for 2-d Random Walk (triangle lattice model)"
result_text = "Sqrt(<R2>) ~ N^("+str(round(exponent, 3))+")"

fig = plt.figure()
ax = fig.add_subplot(111,title=fig_title, xlabel='Log(N)', ylabel='Log(R)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(x_list, y_list)
ax.plot(x_list, fit_func)
fig.text(0.6, 0.20, result_text)
#fig.text(0.6, 0.15, round(intercept, 3))

fig.savefig("./png/scaling_triangle.png", dpi=300)

plt.show()