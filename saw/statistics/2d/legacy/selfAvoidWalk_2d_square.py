# 2d Self-Avoiding Walk

import numpy as np
from math import *
from scipy.stats import norm
import saw2dFuncS_square as saws
import saw2dFuncM_square as sawm
import matplotlib.pyplot as plt
import histDraw as hist
from scipy.optimize import curve_fit

# Calculation of 2d Self-Avoiding Walk

N = 100
M = 500

coordinateS_list, resultS_list = saws.saw2dFuncS(N)
coordinateM_list, resultM_list = sawm.saw2dFuncM(N, M)

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

#def fitFunc(x, a, b):
#    return  b * x * np.exp(-x*x/a)

# Plot of 2d Self-Avoiding Walk

x_range = x_max / sqrt(2)
y_range = y_max / sqrt(2)

ax1_title = "2-dimensional Self-Avoiding Walk (square lattice)"+" (N = "+str(N)+")"
ax2_title = "Distribution of R"
ax3_title = "Distribution of X"
ax4_title = "Distribution of Y"

resultText_r = "r = "+str(round(r, 1))
resultText_rmean = "r_mean (M = "+str(M)+") = "+str(round(r_mean, 1))
resultText_R = "R (M = "+str(M)+") = "+str(round(R, 1))
resultText_xmean = "x_mean (M = "+str(M)+") = "+str(round(x_mean, 1))
resultText_xstd = "x_std (M = "+str(M)+") = "+str(round(x_std, 1))
resultText_ymean = "y_mean (M = "+str(M)+") = "+str(round(y_mean, 1))
resultText_ystd = "y_std (M = "+str(M)+") = "+str(round(y_std, 1))

fig = plt.figure(figsize=(12.0, 12.0))

ax1 = fig.add_subplot(221,title=ax1_title, xlabel='X', ylabel='Y',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax1.grid(axis='both', color="gray", lw=0.5)
ax1.plot(x_list, y_list)
ax1.plot(x_list[0], y_list[0], marker=".", color="red")
ax1.plot(x_list[N], y_list[N], marker=".", color="red")

hist_RX, hist_RY, histInfo_R = hist.histDraw(fig, 2, 2, 2, ax2_title, "orange", r_list)
np.savetxt("./data/hist_RX.txt", hist_RX)
np.savetxt("./data/hist_RY.txt", hist_RY)
np.savetxt("./data/histInfo_R.txt", histInfo_R)
hist_RY = np.append(hist_RY, 0)

#param, cov = curve_fit(fitFunc, hist_RX, hist_RY)

#R_fit = np.sqrt(param[0])

#resultText_Rfit = "R_fit = "+str(round(R_fit, 1))

#fit_RX = np.linspace(max(histInfo_R[0], 0), histInfo_R[1], 100)
#fit_RY = []
#for x in fit_RX :
#    fit_RY.append( param[1]*x*np.exp(-x*x/param[0]))
#plt.plot(fit_RX, fit_RY)

hist_XX, hist_XY, histInfo_X = hist.histDraw(fig, 2, 2, 3, ax3_title, "green", xt_list)
GaussXX = np.linspace(histInfo_X[0], histInfo_X[1], 100)
GaussXY = norm.pdf(GaussXX, GaussX_mean, GaussX_std)
plt.plot(GaussXX, GaussXY, color="red")
np.savetxt("./data/hist_XX.txt", hist_XX)
np.savetxt("./data/hist_XY.txt", hist_XY)
np.savetxt("./data/histInfo_X.txt", histInfo_X)

hist_YX, hist_YY, histInfo_Y = hist.histDraw(fig, 2, 2, 4, ax4_title, "green", yt_list)
GaussYX = np.linspace(histInfo_Y[0], histInfo_Y[1], 100)
GaussYY = norm.pdf(GaussYX, GaussY_mean, GaussY_std)
plt.plot(GaussYX, GaussYY, color="red")
np.savetxt("./data/hist_YX.txt", hist_YX)
np.savetxt("./data/hist_YY.txt", hist_YY)
np.savetxt("./data/histInfo_Y.txt", histInfo_Y)

fig.text(0.28, 0.60, resultText_r)
fig.text(0.28, 0.58, resultText_rmean)
fig.text(0.28, 0.56, resultText_R)
fig.text(0.32, 0.43, resultText_xmean)
fig.text(0.32, 0.41, resultText_xstd)
fig.text(0.74, 0.43, resultText_ymean)
fig.text(0.74, 0.41, resultText_ystd)

#fig.text(0.74, 0.85, resultText_Rfit)

fig.savefig("./png/selfAvoidWalk_2d_square.png", dpi=300)

plt.show()
