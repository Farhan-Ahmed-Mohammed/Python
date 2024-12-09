n=int(input("Enter a number till where you want fibonacci series :"))
def fib(n):
    if(n<=1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(n):    
    print(fib(i))
    