a,b=int(input("Enter two numbers :")), int(input())
print("Enter 1 for Addition")
print("Enter 2 for subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
i=int(input("Enter a operator from above statements :"))
if(i==1):
    print(a+b)
elif(i==2):
    print(a-b)
elif(i==3):
    print(a*b)
elif(i==4):
    print(a/b)
else:
    print("Invalid operator ")           
