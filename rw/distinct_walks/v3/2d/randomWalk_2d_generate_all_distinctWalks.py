# Generation of lists of all distinct 2d Random Walks 

import rw2dFuncS_v3 as rws
import time

try:
    N = int(input('Degree of polymerization (default=5): '))
except ValueError:
    N = 5

start_time = time.process_time()

file_num = 0

for n in range(N):
    rws.rw2dDistinctWalks(file_num)
    file_num += 1

end_time = time.process_time()
elapsed_time = end_time - start_time
print('N_max = {0}, t = {1:.5f} s'.format(N,elapsed_time))