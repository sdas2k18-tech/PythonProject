from numpy import *
#
# arr1 = array([1,3,5,7,8])
# arr2 = arr1 # normal copy, same address, just an impression is created
# arr3 = arr1.view() # new address creaded but still interlinked, shalllow copy
#
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))
#
# arr1.append(5)
# # print(arr1)
#
# arr1 = array([[1,3,5,7,8,9], [5,6,7,8,7,3]])
#
# arr2 = arr1.flatten()
# arr3 = arr1.reshape(3,4)
# arr4 = arr1.reshape(1,2,2,3)
# arr5 = arr1.reshape(2,2,3)
# print(arr4)
# print("array 5", arr5)

m= matrix('1 2 3;4 5 6; 7 8 9')


print(diagonal(m))
