# 3d Random Walk (all models)
# square lattice, FJC chainをまとめることにした（250222）
# そのために球面座標系を採用してみた

import numpy as np
from math import *
from scipy.stats import norm
from scipy.optimize import curve_fit
import rw3dFunc_v3 as rw
import figDraw_v0 as fd
import histDraw_v1 as hist
import matplotlib.pyplot as plt
import time

# Calculation of 3d Random Walk

try:
    N = int(input('Degree of polymerization (default=1000): '))
except ValueError:
    N = 1000

try:
    M = int(input('Number of repetition (default=1000): '))
except ValueError:
    M = 1000

model = input('Square lattice, Freely-jointed chain models (S or F): ')
if model != "S" and model != "F":
    model = "S"

start_time = time.process_time()

logN = log10(N)
logM = log10(M)

# ax1 data（１つだけランダムウォークを例示的に表示するため）
x_list, y_list, z_list = rw.rw3dS(N, model)
xi = x_list[0]     # 初期位置
yi = y_list[0]
zi = y_list[0]
xt = x_list[-1]    # 最終位置
yt = y_list[-1]
zt = z_list[-1]
r  = np.sqrt(xt**2 + yt**2 + zt**2)

# ax2-6 data（統計データを表示、計算するため）
xt_list, yt_list, zt_list, r2_list = rw.rw3dM(N, M, model)
r_list = [ np.sqrt(r2_list[i]) for i in range(M)]

# ax2-6 statistical data（統計データを表示するため）
x_max  = np.max(xt_list)
y_max  = np.max(yt_list)
z_max  = np.max(zt_list)
r2_max = np.max(r2_list)
r_max  = np.max(r_list)

x_mean  = np.mean(xt_list)
y_mean  = np.mean(yt_list)
z_mean  = np.mean(zt_list)
r2_mean = np.mean(r2_list)
r_mean  = np.mean(r_list)

x_std  = np.std(xt_list)
y_std  = np.std(yt_list)
z_std  = np.std(zt_list)
r2_std = np.std(r2_list)
r_std  = np.std(r_list)  

R = np.sqrt(r2_mean)       # (平均)末端間距離

# Least-squares fitting

GaussX_mean,GaussX_std = norm.fit(xt_list)
GaussY_mean,GaussY_std = norm.fit(yt_list)
GaussZ_mean,GaussZ_std = norm.fit(zt_list)

def fitFunc_r(x, a, b):    # r分布のためのフィッティング関数
    return  b * x*x * np.exp(-3*x*x/a/2)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total time = {0:.5f} s'.format(elapsed_time))

# Plot of 3d Random Walk

if model == "S":
    model_title = "Square Lattice Model"
    model_fname = "square"
if model == "F":
    model_title = "Freely-jointed Chain Model"
    model_fname = "fjc"

x_range = x_max / sqrt(2)
y_range = y_max / sqrt(2)
z_range = z_max / sqrt(2)

ax1_title = "3D Random Walk ({0})".format(model_title)
ax2_title = "Distribution of $r$"
ax3_title = "X-Y plane projection ($N$ = $10^{0:.0f}$)".format(logN)
ax4_title = "Distribution of $X$ ($M$ = $10^{0:.0f}$)".format(logM)
ax5_title = "Y-Z plane projection ($N$ = $10^{0:.0f}$)".format(logN)
ax6_title = "Distribution of $Y$ ($M$ = $10^{0:.0f}$)".format(logM)
ax7_title = "Z-X plane projection ($N$ = $10^{0:.0f}$)".format(logN)
ax8_title = "Distribution of $Z$ ($M$ = $10^{0:.0f}$)".format(logM)

resultText_NM = "$N$ = $10^{1:.0f}$, $M$ = $10^{2:.0f}$".format(model_title, logN, logM)
resultText_r = "$r$ = {0:.1f}".format(r)
resultText_R = "$R$ = <$r^2>^{{1/2}}$ = {0:.1f}".format(R)
resultText_xmean = "$\mu_x$ = <$x$> = {0:.1f}".format(x_mean)
resultText_xstd = "$\sigma_x$ = {0:.1f}".format(x_std)
resultText_ymean = "$\mu_y$ = <$y$> = {0:.1f}".format(y_mean)
resultText_ystd = "$\sigma_y$ = {0:.1f}".format(y_std)
resultText_zmean = "$\mu_z$ = <$z$> = {0:.1f}".format(z_mean)
resultText_zstd = "$\sigma_z$ = {0:.1f}".format(z_std)

fig = plt.figure(figsize=(12.0, 20.0))

ax1 = fig.add_subplot(421,title=ax1_title, xlabel='$X$', ylabel='$Y$', zlabel='$Z$',
                      xlim=[-0.7*x_range, 0.7*x_range], ylim=[-0.7*y_range , 0.7*y_range], zlim=[-0.7*z_range, 0.7*z_range],
                      projection='3d')
ax1.grid(axis='both', color="gray", lw=0.5)
ax1.plot(x_list, y_list, z_list)
ax1.plot(xi, yi, zi, marker=".", color="red")
ax1.plot(xt, yt, zt, marker=".", color="red")

fd.figDraw(fig, 4, 2, 3, ax3_title, '$X$', '$Y$', x_range, y_range, x_list, y_list, xi, yi, xt, yt)
fd.figDraw(fig, 4, 2, 5, ax5_title, '$Y$', '$Z$', y_range, z_range, y_list, z_list, yi, zi, yt, zt)
fd.figDraw(fig, 4, 2, 7, ax7_title, '$Z$', '$X$', z_range, x_range, z_list, x_list, zi, xi, zt, xt)

hist_RX, hist_RY, histInfo_R = hist.histDraw(fig, 4, 2, 2, ax2_title, "$r$", "orange", r_list)
hist_RY = np.append(hist_RY, 0)

param, cov = curve_fit(fitFunc_r, hist_RX, hist_RY, p0=[N, 1e-3])

R_fit = np.sqrt(param[0])
resultText_Rfit = "$R_{{fit}}$ = {0:.1f}".format(R_fit)

fit_RX = np.linspace(max(histInfo_R[0], 0), histInfo_R[1], 100)
fit_RY = [ param[1]*x*x*np.exp(-3*x*x/param[0]/2) for x in fit_RX ]
plt.plot(fit_RX, fit_RY)

hist_XX, hist_XY, histInfo_X = hist.histDraw(fig, 4, 2, 4, ax4_title, "$X$", "green", xt_list)
GaussXX = np.linspace(histInfo_X[0], histInfo_X[1], 100)
GaussXY = norm.pdf(GaussXX, GaussX_mean, GaussX_std)
plt.plot(GaussXX, GaussXY, color="red")

hist_YX, hist_YY, histInfo_Y = hist.histDraw(fig, 4, 2, 6, ax6_title, "$Y$", "green", yt_list)
GaussYX = np.linspace(histInfo_Y[0], histInfo_Y[1], 100)
GaussYY = norm.pdf(GaussYX, GaussY_mean, GaussY_std)
plt.plot(GaussYX, GaussYY, color="red")

hist_ZX, hist_ZY, histInfo_Z = hist.histDraw(fig, 4, 2, 8, ax8_title, "$Z$", "green", zt_list)
GaussZX = np.linspace(histInfo_Z[0], histInfo_Z[1], 100)
GaussZY = norm.pdf(GaussZX, GaussZ_mean, GaussZ_std)
plt.plot(GaussZX, GaussZY, color="red")

fig.text(0.15, 0.86, resultText_NM)
fig.text(0.15, 0.84, resultText_r)
fig.text(0.15, 0.82, resultText_R)
fig.text(0.57, 0.66, resultText_xmean)
fig.text(0.57, 0.64, resultText_xstd)
fig.text(0.57, 0.46, resultText_ymean)
fig.text(0.57, 0.44, resultText_ystd)
fig.text(0.57, 0.26, resultText_zmean)
fig.text(0.57, 0.24, resultText_zstd)
fig.text(0.74, 0.85, resultText_Rfit)

savefile = "./png/randomWalk_3d_{0}_N{1:.0f}M{2:.0f}.png".format(model_fname, logN, logM)

fig.savefig(savefile, dpi=300, bbox_inches='tight')

#plt.tight_layout()
plt.show()
