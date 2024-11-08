import numpy as np

a=np.arange(100)
print(a)
b=a[3:10]  #start is 3 and till 9 it prints from a 
print(b)
b[0]=-1200
print(b)  #first element of b is now -1200
print(a)  #3rd element of a is -1200 now bcoz b is not a copy it changes in orginal also
c=a[::-1]
print(c)  #it takes step from last one 
d=np.round(10*np.random.rand(5,4))  #it round ups to nearest interger  multiply by 10 bcoz we get as 0. so to get interger
print(d)
print(d[0,2])
print(d[1,:]) #prints first row till last column
print(d[:,2]) #prints 3rd column elements
print(d[1:3,2:4])  #prints sub matrix
print(d.T)  #finds transpose of matrix
d.sort(axis=0)   #sorts columns
print(d)
d.sort(axis=1)
print(d)   #sorts rows
