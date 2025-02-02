# 3d Random Walk

import numpy as np
from math import *
from scipy.stats import norm
import rw3dFuncS_square as rws
import rw3dFuncM_square as rwm
import matplotlib.pyplot as plt
import histDraw as hist
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D

# Calculation of 3d Random Walk

N = 1000
M = 1000

coordinateS_list, resultS_list = rws.rw3dFuncS(N)
coordinateM_list, resultM_list = rwm.rw3dFuncM(N, M)

x_list = coordinateS_list[0]
y_list = coordinateS_list[1]
z_list = coordinateS_list[2]

r2 = resultS_list[0]
r = resultS_list[1]

xt_list = coordinateM_list[0]
yt_list = coordinateM_list[1]
zt_list = coordinateM_list[2]
r2_list = coordinateM_list[3]
r_list = coordinateM_list[4]

x_max = np.max(xt_list)
y_max = np.max(yt_list)
z_max = np.max(zt_list)
r_max = np.max(r_list)

r2_mean = resultM_list[0]
r2_std = resultM_list[1]
r_mean = resultM_list[2]
r_std = resultM_list[3]
x_mean = resultM_list[4]
x_std = resultM_list[5]
y_mean = resultM_list[6]
y_std = resultM_list[7]
z_mean = resultM_list[8]
z_std = resultM_list[9]

R = np.sqrt(r2_mean)

# Least-squares fitting

GaussX_mean,GaussX_std = norm.fit(xt_list)
GaussY_mean,GaussY_std = norm.fit(yt_list)
GaussZ_mean,GaussZ_std = norm.fit(zt_list)

def fitFunc(x, a, b):
    return  b * x*x * np.exp(-x*x/a)

# Plot of 3d Random Walk

x_range = x_max / sqrt(3)
y_range = y_max / sqrt(3)
z_range = z_max / sqrt(3)

ax1_title = "3-dimensional Random Walk (square lattice)"+" (N = "+str(N)+")"
ax2_title = "Distribution of R"
ax3_title = "X-Y plane projection"+" (N = "+str(N)+")"
ax4_title = "Distribution of X"
ax5_title = "Y-Z plane projection"+" (N = "+str(N)+")"
ax6_title = "Distribution of Y"
ax7_title = "Z-X plane projection"+" (N = "+str(N)+")"
ax8_title = "Distribution of Z"

resultText_r = "r = "+str(round(r, 1))
resultText_rmean = "r_mean (M = "+str(M)+") = "+str(round(r_mean, 1))
resultText_R = "R (M = "+str(M)+") = "+str(round(R, 1))
resultText_xmean = "x_mean (M = "+str(M)+") = "+str(round(x_mean, 1))
resultText_xstd = "x_std (M = "+str(M)+") = "+str(round(x_std, 1))
resultText_ymean = "y_mean (M = "+str(M)+") = "+str(round(y_mean, 1))
resultText_ystd = "y_std (M = "+str(M)+") = "+str(round(y_std, 1))
resultText_zmean = "z_mean (M = "+str(M)+") = "+str(round(z_mean, 1))
resultText_zstd = "z_std (M = "+str(M)+") = "+str(round(z_std, 1))

fig = plt.figure(figsize=(12.0, 24.0))

ax1 = fig.add_subplot(421,title=ax1_title, xlabel='X', ylabel='Y', zlabel='Z',
                      xlim=[-x_range/2, x_range/2], ylim=[-y_range/2 , y_range/2], zlim=[-z_range/2, z_range/2],
                      projection='3d')
ax1.grid(axis='both', color="gray", lw=0.5)
ax1.plot(x_list, y_list, z_list)
ax1.plot(x_list[0], y_list[0], z_list[0], marker=".", color="red")
ax1.plot(x_list[N], y_list[N], z_list[N], marker=".", color="red")

hist_RX, hist_RY, histInfo_R = hist.histDraw(fig, 4, 2, 2, ax2_title, "orange", r_list)
np.savetxt("./data/hist_RX.txt", hist_RX)
np.savetxt("./data/hist_RY.txt", hist_RY)
np.savetxt("./data/histInfo_R.txt", histInfo_R)
hist_RY = np.append(hist_RY, 0)

param, cov = curve_fit(fitFunc, hist_RX, hist_RY)

R_fit = np.sqrt(param[0])

resultText_Rfit = "R_fit = "+str(round(R_fit, 1))

fit_RX = np.linspace(max(histInfo_R[0], 0), histInfo_R[1], 100)
fit_RY = []
for x in fit_RX :
    fit_RY.append( param[1]*x*x*np.exp(-x*x/param[0]))
plt.plot(fit_RX, fit_RY)


ax3 = fig.add_subplot(423,title=ax3_title, xlabel='X', ylabel='Y',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax3.grid(axis='both', color="gray", lw=0.5)
ax3.plot(x_list, y_list)
ax3.plot(x_list[0], y_list[0], marker=".", color="red")
ax3.plot(x_list[N], y_list[N], marker=".", color="red")

hist_XX, hist_XY, histInfo_X = hist.histDraw(fig, 4, 2, 4, ax4_title, "green", xt_list)
GaussXX = np.linspace(histInfo_X[0], histInfo_X[1], 100)
GaussXY = norm.pdf(GaussXX, GaussX_mean, GaussX_std)
plt.plot(GaussXX, GaussXY, color="red")
np.savetxt("./data/hist_XX.txt", hist_XX)
np.savetxt("./data/hist_XY.txt", hist_XY)
np.savetxt("./data/histInfo_X.txt", histInfo_X)

ax5 = fig.add_subplot(425,title=ax5_title, xlabel='Y', ylabel='Z',
                      xlim=[-y_range, y_range], ylim=[-z_range , z_range])
ax5.grid(axis='both', color="gray", lw=0.5)
ax5.plot(y_list, z_list)
ax5.plot(y_list[0], z_list[0], marker=".", color="red")
ax5.plot(y_list[N], z_list[N], marker=".", color="red")

hist_YX, hist_YY, histInfo_Y = hist.histDraw(fig, 4, 2, 6, ax5_title, "green", yt_list)
GaussYX = np.linspace(histInfo_Y[0], histInfo_Y[1], 100)
GaussYY = norm.pdf(GaussYX, GaussY_mean, GaussY_std)
plt.plot(GaussYX, GaussYY, color="red")
np.savetxt("./data/hist_YX.txt", hist_YX)
np.savetxt("./data/hist_YY.txt", hist_YY)
np.savetxt("./data/histInfo_Y.txt", histInfo_Y)

ax7 = fig.add_subplot(427,title=ax7_title, xlabel='Z', ylabel='X',
                      xlim=[-z_range, z_range], ylim=[-x_range , x_range])
ax7.grid(axis='both', color="gray", lw=0.5)
ax7.plot(z_list, x_list)
ax7.plot(z_list[0], x_list[0], marker=".", color="red")
ax7.plot(z_list[N], x_list[N], marker=".", color="red")

hist_ZX, hist_ZY, histInfo_Z = hist.histDraw(fig, 4, 2, 8, ax8_title, "green", zt_list)
GaussZX = np.linspace(histInfo_Z[0], histInfo_Z[1], 100)
GaussZY = norm.pdf(GaussZX, GaussZ_mean, GaussZ_std)
plt.plot(GaussZX, GaussZY, color="red")
np.savetxt("./data/hist_ZX.txt", hist_ZX)
np.savetxt("./data/hist_ZY.txt", hist_ZY)
np.savetxt("./data/histInfo_Z.txt", histInfo_Z)

fig.text(0.22, 0.76, resultText_r)
fig.text(0.22, 0.75, resultText_rmean)
fig.text(0.22, 0.74, resultText_R)
fig.text(0.74, 0.66, resultText_xmean)
fig.text(0.74, 0.65, resultText_xstd)
fig.text(0.74, 0.46, resultText_ymean)
fig.text(0.74, 0.45, resultText_ystd)
fig.text(0.74, 0.26, resultText_zmean)
fig.text(0.74, 0.25, resultText_zstd)

fig.text(0.74, 0.86, resultText_Rfit)

fig.savefig("./png/randomWalk_3d_square.png", dpi=300)

plt.show()
