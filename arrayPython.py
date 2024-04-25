# import array
# from array import *
#
# vals = array('i',[1,4,-6,7,5])
# #
# # print(len(vals))
# # print(vals[::2])
#
# # I= unsigned integers 2
# # i= signed integers 4
#
# newArray = array(vals.typecode, (a for a in vals))
#
# print(newArray)
# # print(array.pop(self, 2)
# for i in newArray:
#     print(i)

from array import *

arr = array('i',[])
n = int(input("enter the length of array: "))

for i in range(n):
     x = int(input("enter the value: "))
     arr.append(x)
     # print(arr)
print(arr)

# search a no in an array
x = int(input("no to be search"))
k=0
for i in arr:
    if i == x:
        print("match found")
        print(k)
        # break
    k+=1
        # break; # break the loop after 1st  match is found
# else used outside if loop if match not found
# else:
#     print("match not found")
print(arr.index(x))
print(type(arr))