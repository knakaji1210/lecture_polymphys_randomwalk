# 1d Random Walk
# pythonのリストで書いたオリジナルをnp.ndarrayに置き換える試み（250214）

# 計測結果
# N = 1000, M = 5で
# v1 = 20.5 s
# v2 = 536 s むしろ遅い！

import numpy as np
from math import *
from scipy.stats import norm
from scipy.optimize import curve_fit
import rw1dFuncS_ndarray as rws
import rw1dFuncM_ndarray as rwm
import histDraw_ndarray as hist
import matplotlib.pyplot as plt
import time

# Calculation of 1d Random Walk

try:
    N = int(input('Degree of polymerization (default=1000): '))
except ValueError:
    N = 1000

try:
    M = int(input('Number of repetition (default=1000): '))
except ValueError:
    M = 1000

start_time = time.process_time()

logN = np.log10(N)
logM = np.log10(M)

# ax1 data（１つだけランダムウォークを例示的に表示するため）
coordinateS_array = rws.rw1dFuncS(N)
x_array = coordinateS_array[0]
y_array = coordinateS_array[1]
xi = x_array[0]     # 初期位置
yi = y_array[0]
xt = x_array[-1]    # 最終位置
yt = y_array[-1]
r  = np.sqrt(xt**2 + yt**2)

# ax2-4 data（統計データを表示、計算するため）
coordinateM_array = rwm.rw1dFuncM(N, M)
xt_array = coordinateM_array[0]
yt_array = coordinateM_array[1]
r2_array = coordinateM_array[2]
r_array  = np.sqrt(r2_array)

# ax2-4 statistical data（統計データを表示するため）
x_max  = np.max(xt_array)
y_max  = np.max(yt_array)
r2_max = np.max(r2_array)
r_max  = np.max(r_array)

x_mean  = np.mean(xt_array)
y_mean  = np.mean(yt_array)
r2_mean = np.mean(r2_array)
r_mean  = np.mean(r_array)

x_std  = np.std(xt_array)
y_std  = np.std(yt_array)
r2_std = np.std(r2_array)
r_std  = np.std(r_array)  

R      = np.sqrt(r2_mean)       # (平均)末端間距離

# Least-squares fitting

GaussX_mean,GaussX_std = norm.fit(xt_array)
GaussY_mean,GaussY_std = norm.fit(yt_array)

def fitFunc_r(x, a, b):           # r分布のためのフィッティング関数
    return  b * np.exp(-x*x/a/2)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total time = {0:.5f} s'.format(elapsed_time))

# Plot of 1d Random Walk

x_range = x_max / sqrt(2)
y_range = 1

ax1_title = "1D Random Walk ($N$ = $10^{0:.0f}$, $M$ = $10^{1:.0f}$)".format(logN, logM)
ax2_title = "Distribution of $r$"
ax3_title = "Distribution of $X$"
ax4_title = "Distribution of $Y$"

resultText_r = "$r$ = {0:.1f}".format(r)
resultText_R = "$R$ = <$r^2>^{{1/2}}$ = {0:.1f}".format(R)
resultText_xmean = "$\mu_x$ = <$x$> = {0:.1f}".format(x_mean)
resultText_xstd = "$\sigma_x$ = {0:.1f}".format(x_std)
resultText_ymean = "$\mu_y$ = <$y$> = {0:.1f}".format(y_mean)
resultText_ystd = "$\sigma_y$ = {0:.1f}".format(y_std)

fig = plt.figure(figsize=(8.0, 9.5))

ax1 = fig.add_subplot(221,title=ax1_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax1.grid(axis='both', color="gray", lw=0.5)
ax1.plot(x_array, y_array)
ax1.plot(xi, yi, marker=".", color="red")       # 始点の赤丸
ax1.plot(xt, yt, marker=".", color="red")       # 終点の赤丸

hist_RX, hist_RY, histInfo_R = hist.histDraw(fig, 2, 2, 2, ax2_title, "$r$", "orange", r_array)
np.savetxt("./data/hist_RX_N{0:.0f}M{1:.0f}.txt".format(logN, logM), hist_RX)
np.savetxt("./data/hist_RY_N{0:.0f}M{1:.0f}.txt".format(logN, logM), hist_RY)
np.savetxt("./data/histInfo_R_N{0:.0f}M{1:.0f}.txt".format(logN, logM), histInfo_R)
hist_RY = np.append(hist_RY, 0)

param, cov = curve_fit(fitFunc_r, hist_RX, hist_RY, p0=[N, 1e-3])

R_fit = np.sqrt(param[0])
resultText_Rfit = "$R_{{fit}}$ = {0:.1f}".format(R_fit)

fit_RX = np.linspace(max(histInfo_R[0], 0), histInfo_R[1], 100)
fit_RY = fitFunc_r(fit_RX, param[0], param[1])  # np.ndarrayを使うとこの形で良い
plt.plot(fit_RX, fit_RY)

hist_XX, hist_XY, histInfo_X = hist.histDraw(fig, 2, 2, 3, ax3_title, "$X$", "green", xt_array)
GaussXX = np.linspace(histInfo_X[0], histInfo_R[1], 100)
GaussXY = norm.pdf(GaussXX, GaussX_mean, GaussX_std)
plt.plot(GaussXX, GaussXY, color="red")
np.savetxt("./data/hist_XX_N{0:.0f}M{1:.0f}.txt".format(logN, logM), hist_XX)
np.savetxt("./data/hist_XY_N{0:.0f}M{1:.0f}.txt".format(logN, logM), hist_XY)
np.savetxt("./data/histInfo_X_N{0:.0f}M{1:.0f}.txt".format(logN, logM), histInfo_X)

hist_YX, hist_YY, histInfo_Y = hist.histDraw(fig, 2, 2, 4, ax4_title, "$Y$", "green", yt_array)

fig.text(0.15, 0.60, resultText_r)
fig.text(0.15, 0.58, resultText_R)
fig.text(0.15, 0.43, resultText_xmean)
fig.text(0.15, 0.41, resultText_xstd)
fig.text(0.57, 0.43, resultText_ymean)
fig.text(0.57, 0.41, resultText_ystd)
fig.text(0.74, 0.85, resultText_Rfit)

savefile = "./png/randomWalk_1d_N{0:.0f}M{1:.0f}.png".format(logN, logM)

fig.savefig(savefile, dpi=300, bbox_inches='tight')

#plt.tight_layout()
plt.show()
