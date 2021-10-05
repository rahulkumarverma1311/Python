import numpy as np
from numpy.core.fromnumeric import reshape 
arr_3d = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(arr_3d)
print(arr_3d.T)
print(arr_3d.ravel())
add_arra_01 = np.arange(1,10)
add_arra_02 = np.arange(11,20)
print("sum of tow numpy array")
sum = np.add(add_arra_01,add_arra_02)
print(sum)
sub = np.subtract(add_arra_02,add_arra_01)
print(sub)

div = np.divide(add_arra_02,add_arra_01)
print(div)

multy = np.multiply(add_arra_02,add_arra_01)
print(multy)
print("dit")
metrix_pro =np.dot(add_arra_01,add_arra_02)
print(metrix_pro)

print("max value in array")
max = np.max(add_arra_02)
print(max)
print(arr_3d)
print("max in row") 
max_in_row = np.max(arr_3d,axis =1)
print(max_in_row)
sum_of_array_element = np.sum(add_arra_01)
print(sum_of_array_element)
mean_of_array = np.mean(add_arra_02)
print(mean_of_array)

arr = np.arange(1,16)
print(arr)
arr1 = np.reshape(arr,(3,5))
print(arr1)
print(np.reshape(arr1,(5,3)))
print("the square root of each lelment of array")

sqr_root = np.sqrt(arr1)
print(sqr_root)
print(np.std(arr1))

print("ecponential of each element")
print(np.exp(arr))

print("log value of each element of array where the log base is 2")

print(np.log(arr1))

print("for log base 10 you have to use this function")
print(np.log10(arr1))
