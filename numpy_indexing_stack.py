import numpy as np

a=np.round(10*np.random.rand(5))
print(a)
print(a[[1,2,4]])                       # prints values at index 1,4,6 of list a
print(a[[True,False,True,True,False]])  # where it is true it prints that value 
print(a[a<8])                           # prints all the values less than 8

#numpy boardcasting

b=np.round(10*np.random.rand(2,2))
print(b)
b=b+5
print(f"After adding 5 to whole matrix :\n{b}")

#numpy hstack,vstack

c=np.round(10*np.random.rand(2,2))
print(c)
d=np.hstack((b,c))                  #concating two matrices horizontally
print("After concatenating horizontally:")
print(d)
print("After concatenating vertically:")
e=np.vstack((b,c)) 
print(e)
print("After sorting :")
f=np.sort(a)                        #np.sort(a) is used to sort 
print(f)
