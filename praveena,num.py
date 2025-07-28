import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3],[4,5,6]])
zeros=np.zeros([3,3])
ones=np.ones([2,2])
identity=np.eye(3)
random_arr=np.random.rand(3,3)
print(arr1)
print(arr2)
print(zeros)
print(ones)
print(identity)
print(random_arr)


print("shape:",arr2.shape)
print("size:",arr2.size)
print("datatype:",arr2.dtype)
print("dimensions:",arr2.ndim)
