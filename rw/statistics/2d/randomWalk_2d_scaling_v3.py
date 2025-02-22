# Scaling of 2d Random Walk (all models)
# square lattice, trianglar lattice, FJC chain全てをまとめることにした（250222）

import numpy as np
from math import *
import rw2dFunc_v3 as rw
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

model = input('Square lattice, Triangular lattice, Freely-jointed chain models (S or T or F): ')
if model != "S" and model != "T" and model != "F":
    model = "S"

logM = log10(M)

start_time = time.process_time()

log_list = np.logspace(0, ex, 2*ex+1, base=10)
n_list = [ int(x) for x in log_list ]
x_list = [ log10(x) for x in n_list ]
R_list = []

# Calculation of Sqrt of R２mean

for n in n_list:
    xt_list, yt_list, r2_list = rw.rw2dM(n, M, model)
    r2_mean = np.mean(r2_list)
    R = np.sqrt(r2_mean)       # (平均)末端間距離
    R_list.append(R)
    # 進行ごとに時間を計測するように変更
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    print('N = {0}, R = {1:.5f}, t = {2:.5f} s'.format(n,R,elapsed_time))

y_list = [ log10(x) for x in R_list ]

# Least-squares fitting

fit_result, fit_error = np.polyfit(x_list, y_list, 1, cov=True)
exponent = fit_result[0]
intercept = fit_result[1]
exponent_error = np.sqrt(fit_error[0,0])
fit_func = np.poly1d(fit_result)(x_list)

# Plot of R-N relationship

if model == "S":
    model_title = "Square Lattice Model"
    model_fname = "square"
if model == "T":
    model_title = "Triangular Lattice Model"
    model_fname = "triangle"
if model == "F":
    model_title = "Freely-jointed Chain Model"
    model_fname = "fjc"

end_time = time.process_time()
elapsed_time = end_time - start_time

print('exponent for R = {0:.3f}±{1:.3f}'.format(exponent,exponent_error))
print('total time = {0:.5f} s'.format(elapsed_time))

fig_title = "Scaling of $R$ for 2-d Random Walk ({0})".format(model_title)
result_text1 = "$R$ = <$r^2>^{{1/2}}$ ~ $N^{{{{{0:.3f}}}±{{{1:.3f}}}}}$".format(exponent,exponent_error)
result_text2 = "$M$ = 10$^{{{0:.0f}}}$, $T_{{comp}}$ = {1:.2f} s".format(logM, elapsed_time)

fig = plt.figure()
ax = fig.add_subplot(111,title=fig_title, xlabel='Log($N$)', ylabel='Log($R$)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(x_list, y_list)
ax.plot(x_list, fit_func, color="black")
fig.text(0.55, 0.20, result_text1)
fig.text(0.55, 0.15, result_text2)

savefile = "./png/randomWalk_2d_{0}_scaling_R_N{1:.0f}M{2:.0f}.png".format(model_fname, ex, logM)

fig.savefig(savefile, dpi=300)

plt.show()