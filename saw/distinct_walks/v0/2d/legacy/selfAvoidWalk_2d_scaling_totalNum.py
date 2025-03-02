# Function to list up distinct 2d Self-Avoiding Walks

import numpy as np
from math import *
import saw2dFuncS2 as saws
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

N = 8
trials = 10**5

num = 0
num_list = []
totalNum_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)

    distinctWalks_list = saws.saw2dDistinctWalks(num, trials)

#    walks_list = distinctWalks_list[0]
    numDistinctWalks = distinctWalks_list[1]
    totalNum_list.append(numDistinctWalks)

log_list = [ log10(x) for x in totalNum_list ]

# Least-squares fitting

#fit_result = np.polyfit(num_list, log_list, 1)
#exponent = fit_result[0]
#intercept = fit_result[1]
#fit_func = np.poly1d(fit_result)(num_list)

def fitFunc(x, a, b): # 理論に合わせて修正が必要
    return  a * x + b

param, cov = curve_fit(fitFunc, num_list, log_list)

z = 10**param[0]
print(z)

fit_func = [ param[0] * x + param[1] for x in num_list ]

fig = plt.figure()

fig_title = "number of distinct walks (2d)"
#result_text1 = "exponent = "+str(round(exponent, 3))+", intercept = "+str(round(intercept, 3))

ax = fig.add_subplot(111,title=fig_title, xlabel='N steps', ylabel='Log(Total Number)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(num_list, log_list)
ax.plot(num_list, fit_func, color="black")
#fig.text(0.5, 0.20, result_text1)

print(num_list)
print(log_list)

fig.savefig("./png/selfAvoidWalk_2d_totalNum.png", dpi=300)

plt.show()
