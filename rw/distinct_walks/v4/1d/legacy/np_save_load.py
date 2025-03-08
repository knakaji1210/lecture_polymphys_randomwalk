import numpy as np

# https://labo-code.com/python/data-analysis/inputfile-all/

#data_array = np.arange(16, dtype=np.int8).reshape(4,4)

#print(data_array)

#np.save('./data/test', data_array)

#np.savetxt('./data/test.txt', data_array)

load_array = np.loadtxt('./data/test.txt', skiprows=1, max_rows=1)

print(load_array)



