# Generation of lists of all distinct 1d Self-Avoiding walk

import saw1dFuncS_v3 as saws
import time

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

start_time = time.process_time()

fileNum = 1

for n in range(N-1):
    start_time_loop = time.process_time()
    numWalks_Last = saws.saw1dDistinctWalks(fileNum)
    end_time_loop = time.process_time()
    elapsed_time_loop = end_time_loop - start_time_loop
    print('t = {0:.5f} s'.format(elapsed_time_loop))
    fileNum += 1


end_time = time.process_time()
elapsed_time = end_time - start_time

print('N_max = {0}, numWalks = {1}'.format(N, numWalks_Last))
print('t_total = {0:.5f} s'.format(elapsed_time))