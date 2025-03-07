# Generation of a list of distinct 2d Random Walks from the previous ones

import rw2dFuncS_v3 as rws
import time

try:
    N = int(input('Current Max DP: '))
except ValueError:
    N = 1

start_time = time.process_time()

rws.rw2dDistinctWalks(N)
N_max = N + 1

end_time = time.process_time()
elapsed_time = end_time - start_time

print('N_max = {0}, t = {1:.5f} s'.format(N_max,elapsed_time))