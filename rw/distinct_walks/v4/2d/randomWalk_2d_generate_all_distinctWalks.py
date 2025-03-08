# Generation of lists of all distinct 2d Random Walks 

import rw2dFuncS_v4 as rws
import time

try:
    N = int(input('Degree of polymerization (default=10): '))
except ValueError:
    N = 10

start_time = time.process_time()

fileNum = 1

for n in range(N-1):
    numWalks_Last = rws.rw2dDistinctWalks(fileNum)
    fileNum += 1

end_time = time.process_time()
elapsed_time = end_time - start_time

print('N_max = {0}, numWalks = {1}'.format(N, numWalks_Last))
print('t = {0:.5f} s'.format(elapsed_time))