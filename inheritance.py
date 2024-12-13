class parent1:
    def add(self,a,b):
        return a+b

class parent2:
    def multi(self,a,b):
        return a*b

class child(parent1,parent2):   #multiple inheritance bcoz tow parent classes we are inheriting 
    def div(self,a,b):
        return a/b

c=child()
print(f"The sum of 10 and 20 is :{c.add(10,20)}")
print(f"The multiplication of 10 and 20 is :{c.multi(10,20)}")
print(f"The division of 10 and 20 is :{c.div(10,20)}")            