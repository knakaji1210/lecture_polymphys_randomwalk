# Generation of lists of all distinct 1d Random Walks 

import rw1dFuncS_v3 as rws
import time

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

start_time = time.process_time()

file_num = 1

for n in range(N-1):
    rws.rw1dDistinctWalks(file_num)
    file_num += 1

end_time = time.process_time()
elapsed_time = end_time - start_time
print('N_max = {0}, t = {1:.5f} s'.format(N,elapsed_time))