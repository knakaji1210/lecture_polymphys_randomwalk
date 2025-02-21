# 1d Random Walk

import numpy as np
from math import *
from scipy.stats import norm
from scipy.optimize import curve_fit
import rw1dFunc_v2 as rw
import histDraw_v1 as hist
import matplotlib.pyplot as plt
import time

# 計測結果
# N = 1000, M = 10000で
# v1 = 2.05559 s
# ndarray = 54.62519 s むしろ遅い！
# v2 = 39.95489 s これも遅いな・・・
# np.random.choiceが遅いからと判明
# rd.choiceに変更すると
# v2 = 5.99347 s
# と改善した

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

logN = log10(N)
logM = log10(M)

# ax1 data（１つだけランダムウォークを例示的に表示するため）
x_list, y_list = rw.rw1dS(N)
xi = x_list[0]     # 初期位置
yi = y_list[0]
xt = x_list[-1]    # 最終位置
yt = y_list[-1]
r  = np.sqrt(xt**2 + yt**2)

# ax2-4 data（統計データを表示、計算するため）
xt_list, yt_list, r2_list = rw.rw1dM(N,M)
r_list = [ np.sqrt(r2_list[i]) for i in range(M)]

# ax2-4 statistical data（統計データを表示するため）
x_max  = np.max(xt_list)
y_max  = np.max(yt_list)
r2_max = np.max(r2_list)
r_max  = np.max(r_list)

x_mean  = np.mean(xt_list)
y_mean  = np.mean(yt_list)
r2_mean = np.mean(r2_list)
r_mean  = np.mean(r_list)

x_std  = np.std(xt_list)
y_std  = np.std(yt_list)
r2_std = np.std(r2_list)
r_std  = np.std(r_list)  

R = np.sqrt(r2_mean)       # (平均)末端間距離

# Least-squares fitting

GaussX_mean,GaussX_std = norm.fit(xt_list)
GaussY_mean,GaussY_std = norm.fit(yt_list)

def fitFunc_r(x, a, b):    # r分布のためのフィッティング関数
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
ax1.plot(x_list, y_list)
ax1.plot(xi, yi, marker=".", color="red")
ax1.plot(xt, yt, marker=".", color="red")

hist_RX, hist_RY, histInfo_R = hist.histDraw(fig, 2, 2, 2, ax2_title, "$r$", "orange", r_list)
np.savetxt("./data/hist_RX_N{0:.0f}M{1:.0f}.txt".format(logN, logM), hist_RX)
np.savetxt("./data/hist_RY_N{0:.0f}M{1:.0f}.txt".format(logN, logM), hist_RY)
np.savetxt("./data/histInfo_R_N{0:.0f}M{1:.0f}.txt".format(logN, logM), histInfo_R)
hist_RY = np.append(hist_RY, 0)

param, cov = curve_fit(fitFunc_r, hist_RX, hist_RY, p0=[N, 1e-3])

R_fit = np.sqrt(param[0])
resultText_Rfit = "$R_{{fit}}$ = {0:.1f}".format(R_fit)

fit_RX = np.linspace(max(histInfo_R[0], 0), histInfo_R[1], 100)
fit_RY = [ param[1]*np.exp(-x*x/param[0]/2) for x in fit_RX ]
plt.plot(fit_RX, fit_RY)

hist_XX, hist_XY, histInfo_X = hist.histDraw(fig, 2, 2, 3, ax3_title, "$X$", "green", xt_list)
GaussXX = np.linspace(histInfo_X[0], histInfo_X[1], 100)
GaussXY = norm.pdf(GaussXX, GaussX_mean, GaussX_std)
plt.plot(GaussXX, GaussXY, color="red")
np.savetxt("./data/hist_XX_N{0:.0f}M{1:.0f}.txt".format(logN, logM), hist_XX)
np.savetxt("./data/hist_XY_N{0:.0f}M{1:.0f}.txt".format(logN, logM), hist_XY)
np.savetxt("./data/histInfo_X_N{0:.0f}M{1:.0f}.txt".format(logN, logM), histInfo_X)

hist_YX, hist_YY, histInfo_Y = hist.histDraw(fig, 2, 2, 4, ax4_title, "$Y$", "green", yt_list)

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
