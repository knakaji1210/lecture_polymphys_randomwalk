# 2d Random Walk (Triangular Lattice model)

import numpy as np
import random as rd
from scipy.stats import norm
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from math import *

# Calculation of 2d Random Walk

N = 1000
M = 1000

direction_list = (0, 2/3, 4/3)

xend_list = []
yend_list = []
r2_list = []
r_list = []

for m in range(M):
    x, y = 0, 0
    x_list = [0]
    y_list = [0]
    for n in range(N):
        theta = pi*rd.choice(direction_list)
        x = x+cos(theta)
        y = y+sin(theta)
        x_list.append(x)
        y_list.append(y)
    xend_list.append(x)
    yend_list.append(y)

    r2 = x*x + y*y
    r = np.sqrt(r2)
    r2_list.append(r2)
    r_list.append(r)


x_mean = np.mean(xend_list)
y_mean = np.mean(yend_list)
r2_mean = np.mean(r2_list)
r_mean = np.mean(r_list)
x_std = np.std(xend_list)
y_std = np.std(yend_list)
r_std = np.std(r_list)
r2_std = np.std(r2_list)
x_max = np.max(xend_list)
y_max = np.max(yend_list)
r_max = np.max(r_list)

# Least-squares fitting

gmean_x,gstd_x = norm.fit(xend_list)
gmean_y,gstd_y = norm.fit(yend_list)

def fitFunc(x, a, b):
    return  b * x * np.exp(-x*x/a)

# Plot of 2d Random Walk

num_bins = 50

x_range = x_max / sqrt(2)
y_range = y_max / sqrt(2)

fig_title = "2-dimensional Random Walk"+" (N = "+str(N)+")"
fig_titleR = "Distribution of R"
fig_titleX = "Distribution of X"
fig_titleY = "Distribution of Y"
result_text = "R = "+str(round(r, 1))
result_textR1 = "R_ave (M = "+str(M)+") = "+str(round(r_mean, 1))
result_textR2 = "Sqrt(R2_ave) (M = "+str(M)+") = "+str(round(sqrt(r2_mean), 1))
result_textX1 = "X_ave (M = "+str(M)+") = "+str(round(x_mean, 1))
result_textX2 = "X_std (M = "+str(M)+") = "+str(round(x_std, 1))
#result_textX2 = "X_std (M = "+str(M)+") = "+str(round(gstd_x, 1))
result_textY1 = "Y_ave (M = "+str(M)+") = "+str(round(y_mean, 1))
result_textY2 = "Y_std (M = "+str(M)+") = "+str(round(y_std, 1))
#result_textY2 = "Y_std (M = "+str(M)+") = "+str(round(gstd_y, 1))

fig = plt.figure(figsize=(12.0, 12.0))
ax = fig.add_subplot(221,title=fig_title, xlabel='X', ylabel='Y',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax.grid(axis='both', color="gray", lw=0.5)
ax.plot(x_list, y_list)
ax.plot(x_list[0], y_list[0], marker=".", color="red")
ax.plot(x_list[N], y_list[N], marker=".", color="red")

ax_R = fig.add_subplot(222,title=fig_titleR)
hist_R = plt.hist(r_list, bins=num_bins, color="orange", density=True)
histRmin, histRmax = plt.xlim()
bin_width = (histRmax - histRmin) / num_bins
hist_RY = np.array(hist_R[0])
#hist_RY = bin_width * hist_R[0]
hist_RY = np.append(hist_RY, 0)
hist_RX = np.array(hist_R[1])
np.savetxt("./data/hist_R_triangle_x.txt", hist_RX)
np.savetxt("./data/hist_R_triangle_y.txt", hist_RY)

param, cov = curve_fit(fitFunc, hist_RX, hist_RY)

fx_R = np.linspace(max(histRmin, 0), histRmax, 100)
fy_R = []
for num in fx_R:
    fy_R.append( param[1]*num*np.exp(-num*num/param[0]))

plt.plot(fx_R, fy_R)

result_textR3 = "R_fit = "+str(round(np.sqrt(param[0]), 1))

ax_X = fig.add_subplot(223,title=fig_titleX)
hist_X = plt.hist(xend_list, bins=num_bins, color="green", density=True)
histXmin, histXmax = plt.xlim()
gx_X = np.linspace(histXmin, histXmax, 100)
gy_X = norm.pdf(gx_X, gmean_x, gstd_x)
plt.plot(gx_X, gy_X, color="red")
bin_width = (histXmax - histXmin) / 20.0
hist_XY = bin_width * hist_X[0]
hist_XX = hist_X[1]
np.savetxt("./data/hist_X_triangle_x.txt", hist_XX)
np.savetxt("./data/hist_X_triangle_y.txt", hist_XY)

ax_Y = fig.add_subplot(224,title=fig_titleY)
hist_Y = plt.hist(yend_list, bins=num_bins, color="green", density=True)
histYmin, histYmax = plt.xlim()
gx_Y = np.linspace(histYmin, histYmax, 100)
gy_Y = norm.pdf(gx_Y, gmean_y, gstd_y)
plt.plot(gx_Y, gy_Y, color="red")

# Plot of statistical results

fig.text(0.28, 0.60, result_text)
fig.text(0.28, 0.58, result_textR1)
fig.text(0.28, 0.56, result_textR2)
fig.text(0.74, 0.85, result_textR3)
fig.text(0.32, 0.43, result_textX1)
fig.text(0.32, 0.41, result_textX2)
fig.text(0.74, 0.43, result_textY1)
fig.text(0.74, 0.41, result_textY2)

fig.savefig("./png/triangle.png", dpi=300)

plt.show()
