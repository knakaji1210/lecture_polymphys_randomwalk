# Generation of a list of distinct 3d Random Walks from the previous ones

import rw3dFuncS_v4 as rws
import time

try:
    N = int(input('Current Max DP: '))
except ValueError:
    N = 1

start_time = time.process_time()

numWalks_Last = rws.rw3dDistinctWalks(N)


end_time = time.process_time()
elapsed_time = end_time - start_time

print('N_next = {0}, numWalks = {1}'.format(N+1, numWalks_Last))
print('t = {0:.5f} s'.format(elapsed_time))