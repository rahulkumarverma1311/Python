import numpy as np
from numpy.core.numeric import ones, ones_like 
print("iD array")
array_1d = np.array([1,2,3,4,5])
print(array_1d)
print("2D array")
array_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(array_2d)
print("how to find diamention of numpy array")
print("diamention of array_2d is :",array_2d.ndim)
print("how to find size of numpy array")
print("the size of numpy array is :",array_1d.size)
print("how to find the shape of numpy array")
print("the shape  of the umpy array is:",array_2d.shape)
print("how to find the data type of numpy array's element")
print("the data type of numpy array's element is:",array_1d.dtype)

print("how to creat zero metris")

zero_metr = np.zeros((4,4))
print(zero_metr)

print("how to creat ones metris")
ones_metrix = np.ones((3,3))
print(ones_metrix)

print("randam metrix ")
rand = np.empty((3,4))
print(rand)



print("NumPy arrange fuc")

arr1 = np.arange(1,13)
print(arr1)

inline = np.linspace(1,20,100)
print(inline)


print("reshape fun of numpy")
new_arr1 = np.reshape(arr1,(3,4))
print(new_arr1)

print(array_2d)
print("convert multidiamensional array to 1d array")
print(array_2d.ravel())
