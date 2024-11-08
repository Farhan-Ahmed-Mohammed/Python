import numpy as np

a=np.array([1,2,3,4])
print(a)
print(f"The dimentions of given array is :",a.ndim)  # gives dimentions of array 
b=np.array([5,6,7,8])
print(b)
print("The 2D array is :")
c=np.array([[10,11,12],[13,14,15],[16,17,18]])   #creating a 2d array 
print(c)
print("The element at position c[1,2] is :")
print(c[1,2])
print(c.shape) # gives (no of 1d arrays, no of elements in 1d array)
print(f"The no of elements in c is :",c.size) # gives the no of elements 
d=np.arange(100)
print(d)  #prints nos form 0 to 99
d=np.arange(80,100)
print(d)  #prints nos form 80 to 99
e=np.array([1,2,3,4,5,6,7,8,9,10])
f=e.reshape(2,5)   #it becomes a 2 by 5 matrix 
print(f)
g=np.random.rand(10)   # prints 10 random values form between 0 and 1
print(g)
h=np.random.rand(2,3)  # gives a 2 by 3 matrix of random values between 0 and 1
print(h)
i=np.random.permutation(np.arange(10))
print(i)
