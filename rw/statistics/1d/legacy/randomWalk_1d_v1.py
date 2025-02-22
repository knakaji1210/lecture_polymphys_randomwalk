# 1d Random Walk

import numpy as np
from math import *
from scipy.stats import norm
import rw1dFuncS_v1 as rws
import rw1dFuncM_v1 as rwm
import matplotlib.pyplot as plt
import histDraw_v1 as hist
from scipy.optimize import curve_fit
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

logN = log10(N)
logM = log10(M)

coordinateS_list, resultS_list = rws.rw1dFuncS(N)
coordinateM_list, resultM_list = rwm.rw1dFuncM(N, M)

x_list = coordinateS_list[0]
y_list = coordinateS_list[1]

r2 = resultS_list[0]
r = resultS_list[1]

xt_list = coordinateM_list[0]
yt_list = coordinateM_list[1]
r_list = coordinateM_list[3]

x_max = np.max(xt_list)
y_max = np.max(yt_list)
r_max = np.max(r_list)

r2_mean = resultM_list[0]
r2_std = resultM_list[1]
r_mean = resultM_list[2]
r_std = resultM_list[3]
x_mean = resultM_list[4]
x_std = resultM_list[5]
y_mean = resultM_list[6]
y_std = resultM_list[7]

R = np.sqrt(r2_mean)

# Least-squares fitting

GaussX_mean,GaussX_std = norm.fit(xt_list)
GaussY_mean,GaussY_std = norm.fit(yt_list)

def fitFunc(x, a, b):
    return  b * np.exp(-x*x/a/2)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total time = {0:.5f} s'.format(elapsed_time))

# Plot of 1d Random Walk

x_range = x_max / sqrt(2)
y_range = 1

ax1_title = "1D Random Walk ($N$ = $10^{0:.0f}$, $M$ = $10^{1:.0f}$)".format(logN, logM)
ax2_title = "Distribution of $R$ = <$r^2>^{{1/2}}$"
ax3_title = "Distribution of $X$"
ax4_title = "Distribution of $Y$"

resultText_r = "$r$ = {0:.1f}".format(r)
resultText_rmean = "<$r$> = {1:.1f}".format(logM, r_mean)
resultText_R = "$R$ = {1:.1f}".format(M, R)
resultText_xmean = "<$x$> = {1:.1f}".format(M, x_mean)
resultText_xstd = "$\sigma_x$ = {1:.1f}".format(M, x_std)
resultText_ymean = "<$y$> = {1:.1f}".format(M, y_mean)
resultText_ystd = "$\sigma_y$ = {1:.1f}".format(M, y_std)

fig = plt.figure(figsize=(8.0, 9.5))

ax1 = fig.add_subplot(221,title=ax1_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax1.grid(axis='both', color="gray", lw=0.5)
ax1.plot(x_list, y_list)
ax1.plot(x_list[0], y_list[0], marker=".", color="red")
ax1.plot(x_list[N], y_list[N], marker=".", color="red")

hist_RX, hist_RY, histInfo_R = hist.histDraw(fig, 2, 2, 2, ax2_title, "$R$", "orange", r_list)
np.savetxt("./data/hist_RX.txt", hist_RX)
np.savetxt("./data/hist_RY.txt", hist_RY)
np.savetxt("./data/histInfo_R.txt", histInfo_R)
hist_RY = np.append(hist_RY, 0)

param, cov = curve_fit(fitFunc, hist_RX, hist_RY, p0=[N, 1e-3])

R_fit = np.sqrt(param[0])

resultText_Rfit = "$R_{{fit}}$ = {0:.1f}".format(R_fit)

fit_RX = np.linspace(max(histInfo_R[0], 0), histInfo_R[1], 100)
fit_RY = []
for x in fit_RX :
        fit_RY.append( param[1]*np.exp(-x*x/param[0]/2))
plt.plot(fit_RX, fit_RY)

hist_XX, hist_XY, histInfo_X = hist.histDraw(fig, 2, 2, 3, ax3_title, "$X$", "green", xt_list)
GaussXX = np.linspace(histInfo_X[0], histInfo_R[1], 100)
GaussXY = norm.pdf(GaussXX, GaussX_mean, GaussX_std)
plt.plot(GaussXX, GaussXY, color="red")
np.savetxt("./data/hist_XX.txt", hist_XX)
np.savetxt("./data/hist_XY.txt", hist_XY)
np.savetxt("./data/histInfo_X.txt", histInfo_X)

hist_YX, hist_YY, histInfo_Y = hist.histDraw(fig, 2, 2, 4, ax4_title, "$Y$", "green", yt_list)







fig.text(0.15, 0.60, resultText_r)
fig.text(0.15, 0.58, resultText_rmean)
fig.text(0.15, 0.56, resultText_R)
fig.text(0.15, 0.43, resultText_xmean)
fig.text(0.15, 0.41, resultText_xstd)
fig.text(0.57, 0.43, resultText_ymean)
fig.text(0.57, 0.41, resultText_ystd)

fig.text(0.74, 0.85, resultText_Rfit)

savefile = "./png/randomWalk_1d_N{0:.0f}M{1:.0f}.png".format(logN, logM)

fig.savefig(savefile, dpi=300, bbox_inches='tight')

#plt.tight_layout()
plt.show()
