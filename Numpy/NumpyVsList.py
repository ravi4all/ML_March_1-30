import numpy as np
import sys
import time

size = range(10000000)

# list_1 = [i for i in size]
#
# np_arr = np.array([i for i in size])
#
# print("Size taken by list",sys.getsizeof(list_1))
# print("Size taken by numpy",sys.getsizeof(np_arr))

list_1 = [i for i in size]
list_2 = list_1[:]

# final_list = list_1 + list_2
# print(final_list)

# final_list = []
#
# start = time.time()
#
# for i in size:
#     final_list.append(list_1[i] + list_2[i])
#
# end = time.time()
# total_time = end - start
# print("Total time taken is",total_time)
#print(final_list)

np_arr_1 = np.array([i for i in size])
np_arr_2 = np_arr_1.copy()

start = time.time()

final_numpy = np_arr_1 + np_arr_2

end = time.time()
total_time = end - start
print("Total time taken is",total_time)