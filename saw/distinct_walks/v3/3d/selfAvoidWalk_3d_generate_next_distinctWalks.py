# Generation of a list of distinct 3d Self-Avoiding walks from the previous ones

import saw3dFuncS_v3 as saws
import time

try:
    N = int(input('Current Max DP: '))
except ValueError:
    N = 1

start_time = time.process_time()

numWalks_Last = saws.saw3dDistinctWalks(N)


end_time = time.process_time()
elapsed_time = end_time - start_time

print('N_next = {0}, numWalks = {1}'.format(N+1, numWalks_Last))
print('t = {0:.5f} s'.format(elapsed_time))