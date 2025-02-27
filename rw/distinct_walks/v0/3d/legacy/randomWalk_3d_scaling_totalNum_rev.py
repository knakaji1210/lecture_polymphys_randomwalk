# Function to list up distinct 3d Random Walks

import numpy as np
from math import *
import rw3dFuncS2 as rws
import matplotlib.pyplot as plt
import time

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

try:
    ex = int(input('Max power exponent (default=5): '))
except ValueError:
    ex = 5

trials = 10**ex

start_time = time.process_time()

num = 0
num_list = []
totalNum_list = []

for n in range(N):
    num = num + 1
    num_list.append(num)

    distinctWalks_list = rws.rw3dDistinctWalks(num, trials)

#    walks_list = distinctWalks_list[0]
    numDistinctWalks = distinctWalks_list[1]
    totalNum_list.append(numDistinctWalks)

    # 進行ごとに時間を計測するように変更
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    print('n = {0}, t = {1:.5f} s'.format(n,elapsed_time))

log_list = [ log10(x) for x in totalNum_list ]

# Least-squares fitting

fit_result = np.polyfit(num_list, log_list, 1)
exponent = fit_result[0]
intercept = fit_result[1]
fit_func = np.poly1d(fit_result)(num_list)

fig = plt.figure()

fig_title = "number of distinct walks (3d)"
result_text1 = "Total distinct walks = "+str(round(10**exponent, 3))+"^N"

ax = fig.add_subplot(111,title=fig_title, xlabel='N steps', ylabel='Log(Total Number)')
ax.grid(axis='both', color="gray", lw=0.5)
ax.scatter(num_list, log_list)
ax.plot(num_list, fit_func, color="black")
fig.text(0.5, 0.20, result_text1)

fig.savefig("./png/randomWalk_3d_totalNum.png", dpi=300)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total number of distinct walks = {0}'.format(totalNum_list[-1]))
print('total time = {0:.5f} s'.format(elapsed_time))

plt.show()
