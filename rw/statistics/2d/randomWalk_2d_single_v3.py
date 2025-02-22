# 2d Random Walk (all models) single shot
# square lattice, trianglar lattice, FJC chain全てをまとめることにした（250222）
# コンフォメーションのシングルショットを画像化するために作成

import numpy as np
from math import *
from scipy.stats import norm
from scipy.optimize import curve_fit
import rw2dFunc_v3 as rw
import histDraw_v1 as hist
import matplotlib.pyplot as plt
import time

# Calculation of 2d Random Walk

try:
    N = int(input('Degree of polymerization (default=1000): '))
except ValueError:
    N = 1000

model = input('Square lattice, Triangular lattice, Freely-jointed chain models (S or T or F): ')
if model != "S" and model != "T" and model != "F":
    model = "S"

start_time = time.process_time()

logN = log10(N)

# ax1 data（１つだけランダムウォークを例示的に表示するため）
x_list, y_list = rw.rw2dS(N, model)
xi = x_list[0]     # 初期位置
yi = y_list[0]
xt = x_list[-1]    # 最終位置
yt = y_list[-1]
r  = np.sqrt(xt**2 + yt**2)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total time = {0:.5f} s'.format(elapsed_time))

# Plot of 2d Random Walk

if model == "S":
    model_title = "Square Lattice Model"
    model_fname = "square"
if model == "T":
    model_title = "Triangular Lattice Model"
    model_fname = "triangle"
if model == "F":
    model_title = "Freely-jointed Chain Model"
    model_fname = "fjc"

x_range = 60
y_range = 60

ax1_title = "2D Random Walk ({0}) ($N$ = $10^{1:.0f}$)".format(model_title, logN)

resultText_r = "$r$ = {0:.1f}".format(r)

fig = plt.figure(figsize=(5.0, 5.0))

ax1 = fig.add_subplot(111,title=ax1_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax1.grid(axis='both', color="gray", lw=0.5)
ax1.plot(x_list, y_list)
ax1.plot(xi, yi, marker=".", color="red")
ax1.plot(xt, yt, marker=".", color="red")

fig.text(0.15, 0.80, resultText_r)

savefile = "./png/randomWalk_2d_{0}_N{1:.0f}_single.png".format(model_fname, logN)

fig.savefig(savefile, dpi=300, bbox_inches='tight')

#plt.tight_layout()
plt.show()
