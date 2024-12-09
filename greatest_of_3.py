a,b,c=[int(x) for x in input("Enter 3 numbers :").split()]
l1=[a if a>=b and a>=c  b elif b>=a and b>=c else c]
print(f"The greatest of given 3 numbers {a},{b},{c} is :{l1}")