# numpy

# not a part of python library. import it with an alias
# array in numpy called ndarray

import numpy as np

numpy_arr=np.array([10,20,30,40,50])
print(type(numpy_arr))

# why python need array if list is there


# arithmatic opertions 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(f"Sum of 2 array is f{arr1 + arr2}")
print(f"diff of array is {arr2-arr1}")
print("arr size : {arr1.size}")

# 2d array
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d)


# print shape
print(arr_2d.shape)

# special array all are zero
special=np.zeros(3)
print(special)
print(special[1],special[0],special[2])

