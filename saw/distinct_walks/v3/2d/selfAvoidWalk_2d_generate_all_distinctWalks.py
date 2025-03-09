# Generation of lists of all distinct 2d Self-Avoiding walk

import saw2dFuncS_v3 as saws
import time

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

start_time = time.process_time()

fileNum = 1

for n in range(N-1):
    numWalks_Last = saws.saw2dDistinctWalks(fileNum)
    fileNum += 1

end_time = time.process_time()
elapsed_time = end_time - start_time

print('N_max = {0}, numWalks = {1}'.format(N, numWalks_Last))
print('t = {0:.5f} s'.format(elapsed_time))