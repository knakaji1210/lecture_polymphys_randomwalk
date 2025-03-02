# Scaling of number of total distinct walks for 2d Self-Avoiding Walk 

import numpy as np
from math import *
import saw2dFuncS4 as saws
import matplotlib.pyplot as plt
import time
from scipy.optimize import curve_fit

start = time.time()

N = 14

walks_list = [[[0, 0]]]
num = 0
num_list = []
totalNum_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)
    walks_list = saws.saw2dDistinctWalks(walks_list)
    totalNum = len(walks_list)
    totalNum_list.append(totalNum)

print(totalNum_list)

log_list = [ log10(x) for x in totalNum_list ]

elapsed_time = time.time() - start
print(f"elapsed_time = {elapsed_time:6f} sec")

np.savetxt("./data/num_steps.txt", num_list, fmt='%5.f')
np.savetxt("./data/num_distinctwalks.txt", totalNum_list, fmt='%5.f')
np.savetxt("./data/loog_num_distinctwalks.txt", log_list, fmt='%.3e')

# Least-squares fitting

#fit_result = np.polyfit(num_list, log_list, 1)
#exponent = fit_result[0]
#intercept = fit_result[1]
#fit_func = np.poly1d(fit_result)(num_list)

def fitFunc(x, a, b):
    return  a * x + b * np.log10(x)

param, cov = curve_fit(fitFunc, num_list, log_list, p0=[0.4, 0.1])
param_err = np.sqrt(np.diag(cov))
print(param, param_err)

fit_func = [ param[0] * x + param[1] * np.log10(x) for x in num_list ]

fig = plt.figure()

fig_title = "number of distinct walks (2d)"
result_text = "Total distinct walks = "+str(round(10**param[0], 3))+"^N * N^("+str(round(param[1]+1, 3))+" - 1)"

ax = fig.add_subplot(111,title=fig_title, xlabel='N steps', ylabel='Log(Total Number)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(num_list, log_list)
ax.plot(num_list, fit_func, color="black")
fig.text(0.35, 0.20, result_text)

fig.savefig("./png/selfAvoidWalk_2d_totalNum.png", dpi=300)

plt.show()
