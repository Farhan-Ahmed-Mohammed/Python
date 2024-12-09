a,b=[int(x) for x in input("Enter two numbers :").split()]
def gcd(a,b):
    for x in range(1,a):
        if(a%x==0 and b%x==0):
            ans=x

    return ans
result=gcd(a,b)
print(f"The gcd of given {a} and {b} is :{result}")        