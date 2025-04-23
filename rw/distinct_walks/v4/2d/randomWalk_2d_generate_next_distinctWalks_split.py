# Generation of a list of distinct 2d Random Walks from the previous ones

import rw2dFuncS_v4_split as rws
import time

try:
    N = int(input('Current Max DP: '))
except ValueError:
    N = 1

try:
    sp = int(input('File number: '))
except ValueError:
    sp = 1

start_time = time.process_time()

numWalks_Last = rws.rw3dDistinctWalks(N,sp)


end_time = time.process_time()
elapsed_time = end_time - start_time

print('N_next = {0}, numWalks = {1}'.format(N+1, numWalks_Last))
print('t = {0:.5f} s'.format(elapsed_time))