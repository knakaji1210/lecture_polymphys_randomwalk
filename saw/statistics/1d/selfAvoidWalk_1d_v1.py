# 1d Self-Avoiding Walk
# 1dを2dをベースに新たに作成（あまり意味ないけど・・・一応ね）（250224）

import numpy as np
from math import *
from scipy.stats import norm
from scipy.optimize import curve_fit
import saw1dFunc_v1 as saw
import histDraw_v1 as hist
import matplotlib.pyplot as plt
import time

# Calculation of 1d Self-Avoiding Walk

try:
    N = int(input('Degree of polymerization (default=100): '))
except ValueError:
    N = 100

try:
    M = int(input('Number of repetition (default=1000): '))
except ValueError:
    M = 1000

start_time = time.process_time()

logN = log10(N)
logM = log10(M)

# ax1 data（１つだけランダムウォークを例示的に表示するため）
x_list, y_list = saw.saw1dS(N)
xi = x_list[0]     # 初期位置
yi = y_list[0]
xt = x_list[-1]    # 最終位置
yt = y_list[-1]
r  = np.sqrt(xt**2 + yt**2)

# ax2-4 data（統計データを表示、計算するため）
xt_list, yt_list, r2_list = saw.saw1dM(N, M)
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

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total time = {0:.5f} s'.format(elapsed_time))

# Plot of 1d Self-Avoiding Walk

x_range = 1.5*x_max
y_range = x_range

ax1_title = "1D Self-Avoiding Walk"
ax2_title = "Distribution of $r$"
ax3_title = "Distribution of $X$"
ax4_title = "Distribution of $Y$"

resultText_NM = "$N$ = $10^{0:.0f}$, $M$ = $10^{1:.0f}$".format(logN, logM)
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

hist_XX, hist_XY, histInfo_X = hist.histDraw(fig, 2, 2, 3, ax3_title, "$X$", "green", xt_list)

hist_YX, hist_YY, histInfo_Y = hist.histDraw(fig, 2, 2, 4, ax4_title, "$Y$", "green", yt_list)

fig.text(0.15, 0.85, resultText_NM)
fig.text(0.15, 0.60, resultText_r)
fig.text(0.15, 0.58, resultText_R)
fig.text(0.15, 0.43, resultText_xmean)
fig.text(0.15, 0.41, resultText_xstd)
fig.text(0.57, 0.43, resultText_ymean)
fig.text(0.57, 0.41, resultText_ystd)

savefile = "./png/selfAvoidingWalk_1d_square_N{0:.0f}M{1:.0f}.png".format(logN, logM)

fig.savefig(savefile, dpi=300, bbox_inches='tight')

#plt.tight_layout()
plt.show()
