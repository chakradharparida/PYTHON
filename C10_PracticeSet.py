# problem 01


class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        
p=programmer("Chandan",120000,756182)
r=programmer("Rohan",120000,765000)
print(p.name,p.salary,p.company,p.pin)
print(r.name,r.salary,r.company,r.pin)


#problem 02 

class calculater:
    def __init__(self,n):
        self.n=n
    def Square(self):
        print(f"The square is : {self.n*self.n}")
    def Cube(self):
        print(f"The cube is : {self.n*self.n*self.n}")
    def SquareRoot(self):
        print(f"The SquareRoot is : {self.n**0.5}")


c=calculater(10)
c.Cube()
c.Square()
c.SquareRoot()


# problem 03


class Demo:
    a=4

o=Demo()
print(o.a) # Prints the class attribute because instance attribute is not present.
o.a=0  #Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present.
print(Demo.a) # Prints class attribute


# problem 04


