import random as rd
import rw2dFuncS3 as rws
#import rw1dFuncM3 as rwm

trials = 10

coordinate_list = [[0, 0]]

#walks_list = [[[0, 0]]]
#walks_list = [[[0, 0], [1, 0]], [[0, 0], [-1, 0]]]
#walks_list = [[[0, 0], [1, 0], [0, 0]], [[0, 0], [1, 0], [2, 0]], [[0, 0], [-1, 0], [-2, 0]], [[0, 0], [-1, 0], [0, 0]]]
#walks_list = [[[0, 0], [1, 0], [0, 0], [-1, 0]], [[0, 0], [1, 0], [0, 0], [1, 0]], [[0, 0], [1, 0], [2, 0], [3, 0]], [[0, 0], [1, 0], [2, 0], [1, 0]], [[0, 0], [-1, 0], [-2, 0], [-1, 0]], [[0, 0], [-1, 0], [-2, 0], [-3, 0]], [[0, 0], [-1, 0], [0, 0], [-1, 0]], [[0, 0], [-1, 0], [0, 0], [1, 0]]]

#new_walks_list = saws.rw1dDistinctWalks(walks_list, 10)
#result_list = rwm.rw1dCalcR(new_walks_list)
#print(result_list[0])
#print(result_list[1])

new_coordinate_list = rws.rw2dAddStep(coordinate_list)
print(new_coordinate_list)