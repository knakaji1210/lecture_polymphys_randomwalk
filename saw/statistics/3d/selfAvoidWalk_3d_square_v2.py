# 3d Self-Avoiding Walk (square lattice model)

import numpy as np
from math import *
from scipy.stats import norm
from scipy.optimize import curve_fit
import saw3dFunc_square_v2 as saw
import figDraw_v0 as fd
import histDraw_v1 as hist
import matplotlib.pyplot as plt
import time

# Calculation of 3d Self-Avoiding Walk

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
x_list, y_list, z_list = saw.saw3dS(N)
xi = x_list[0]     # 初期位置
yi = y_list[0]
zi = z_list[0]
xt = x_list[-1]    # 最終位置
yt = y_list[-1]
zt = z_list[-1]
r  = np.sqrt(xt**2 + zt**2)

# ax2-8 data（統計データを表示、計算するため）
xt_list, yt_list, zt_list, r2_list = saw.saw3dM(N, M)
r_list = [ np.sqrt(r2_list[i]) for i in range(M)]

# ax2-8 statistical data（統計データを表示するため）
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

GaussX_mean,GaussX_std = norm.fit(xt_list)  # 実際にはガウスではないがずれていることを示すのに使う
GaussY_mean,GaussY_std = norm.fit(yt_list)
GaussZ_mean,GaussZ_std = norm.fit(zt_list)

'''
分布関数について
de Gennes P40のp_N(r)（ここでx = r/R_F）
p_N(x) = (x^g * exp[-x^delta]
はrベクトルについての分布関数なのでr=|r|の分布については3次元ヤコビアンからrの次元を2つ増やす必要がある。
したがって、ここで定義すべきフィッティング関数は
x*p_N(x) = (x^(g+2) * exp[-x^delta]
となる。
p = g + 2
とすると
x*p_N(x) = (x^p * exp[-x^delta]

またフィッティングパラメータaとNの関係は
x^delta = (r/R_F)^delta = r^delta / N^(nu*delta) = r^delta / a
故に
a = N^(nu*delta)
R_F = N^nu = a^(1/delta)
となる
'''

def fitFunc_x(x, a, b, g, d):    # x分布のためのフィッティング関数・・・今回は使わないが、xやyの分布の解析に使えると思う
    return  b * x**g * np.exp(-x**d / a)

def fitFunc_r(r, a, b, p, d):    # r分布のためのフィッティング関数
    return  b * r**p * np.exp(-r**d / a)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total time = {0:.5f} s'.format(elapsed_time))

# Plot of 3d Self-Avoiding Walk

x_range = x_max
y_range = y_max
z_range = z_max

ax1_title = "3D Self-Avoiding Walk (Square Lattice Model)"
ax2_title = "Distribution of $r$"
ax3_title = "X-Y plane projection ($N$ = $10^{{{0:.1f}}}$)".format(logN)
ax4_title = "Distribution of $X$ ($M$ = $10^{0:.0f}$)".format(logM)
ax5_title = "Y-Z plane projection ($N$ = $10^{{{0:.1f}}}$)".format(logN)
ax6_title = "Distribution of $Y$ ($M$ = $10^{0:.0f}$)".format(logM)
ax7_title = "Z-X plane projection ($N$ = $10^{{{0:.1f}}}$)".format(logN)
ax8_title = "Distribution of $Z$ ($M$ = $10^{0:.0f}$)".format(logM)

resultText_NM = "$N$ = $10^{{{0:.1f}}}$, $M$ = $10^{1:.0f}$".format(logN, logM)
resultText_r = "$r$ = {0:.1f}".format(r)
resultText_R = "$R$ = <$r^2>^{{1/2}}$ = {0:.1f}".format(R)
resultText_xmean = "$\mu_x$ = <$x$> = {0:.1f}".format(x_mean)
resultText_xstd = "$\sigma_x$ = {0:.1f}".format(x_std)
resultText_ymean = "$\mu_y$ = <$y$> = {0:.1f}".format(y_mean)
resultText_ystd = "$\sigma_y$ = {0:.1f}".format(y_std)
resultText_zmean = "$\mu_z$ = <$z$> = {0:.1f}".format(z_mean)
resultText_zstd = "$\sigma_z$ = {0:.1f}".format(z_std)

fig = plt.figure(figsize=(12.0, 20.0))

ax1 = fig.add_subplot(421,title=ax1_title, xlabel='$X$', ylabel='$Y$',
                        xlim=[-x_range/2, x_range/2], ylim=[-y_range/2 , y_range/2], zlim=[-z_range/2, z_range/2],
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

nu = 3/5                # nu
g = 7/6                 # gamma
d_theo = (1 - nu)**(-1) # d_theoretical = 5/2
g_theo = (g - 1)/nu     # g_theoretical = 5/18
p_theo = g_theo + 2

param_r, cov_r = curve_fit(fitFunc_r, hist_RX, hist_RY, p0=[N**(nu*d_theo), 1e-1, p_theo, d_theo])

p_exp = param_r[2]
g_exp = p_exp - 2
d_exp = param_r[3]
nu_exp = 1 - 1/d_exp
R_fit = param_r[0]**(1/(d_exp))

resultText_gexp = "$g_{{exp}}$ = {0:.2f}".format(g_exp)
resultText_dexp = "$\delta_{{exp}}$ = {0:.1f}".format(d_exp)
resultText_nuexp = "$\u03BD_{{exp}}$ = {0:.2f}".format(nu_exp)
resultText_Rfit = "$R_{{fit}}$ = {0:.1f}".format(R_fit)

fit_RX = np.linspace(max(histInfo_R[0], 0), histInfo_R[1], 100)
fit_RY = []
for x in fit_RX :
    fit_RY.append( param_r[1]*x**param_r[2] * np.exp(-x**param_r[3] / param_r[0]))
plt.plot(fit_RX, fit_RY)

hist_XX, hist_XY, histInfo_X = hist.histDraw(fig, 4, 2, 4, ax4_title, "$X$", "green", xt_list)
GaussXX = np.linspace(histInfo_X[0], histInfo_X[1], 100)
GaussXY = norm.pdf(GaussXX, GaussX_mean, GaussX_std)
plt.plot(GaussXX, GaussXY, color="red")

hist_YX, hist_YY, histInfo_Y = hist.histDraw(fig, 4, 2, 6, ax6_title, "$Y$", "green", yt_list)
hist_YY = np.append(hist_YY, 0)
GaussYX = np.linspace(histInfo_Y[0], histInfo_Y[1], 100)
GaussYY = norm.pdf(GaussYX, GaussY_mean, GaussY_std)
plt.plot(GaussYX, GaussYY, color="red")

hist_ZX, hist_ZY, histInfo_Z = hist.histDraw(fig, 4, 2, 8, ax8_title, "$Z$", "green", zt_list)
hist_ZY = np.append(hist_ZY, 0)
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

fig.text(0.74, 0.85, resultText_gexp)
fig.text(0.74, 0.83, resultText_dexp)
fig.text(0.74, 0.81, resultText_nuexp)
fig.text(0.74, 0.79, resultText_Rfit)

savefile = "./png/selfAvoidingWalk_3d_square_N{0:.1f}M{1:.0f}.png".format(logN, logM)

fig.savefig(savefile, dpi=300, bbox_inches='tight')

#plt.tight_layout()
plt.show()
