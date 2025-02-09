# Problem 01

"""class TwoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
            print(f"The vector is {self.i}i + {self.j}j")
class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
            print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
a=TwoDvector(1,2)
a.show()
b=ThreeDvector(5,2,3)
b.show()"""

#Problem 02

"""class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark() :
        print ("Bhaw Bhaw !")
d=Dog()
d.bark()"""

#Problem 03

'''class Employee :
    salary = 244
    inicrement=20
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.inicrement=((salary/self.salary)-1)*100
e=Employee()
#print(e.salaryAfterIncrement)
e.salaryAfterIncrement=1000
print(e.inicrement)'''

#Problem 04
import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    a=int(input("Guess The Number : "))
    if(a>n):
        print("Lower Number Please,")
    else:
        print("Higher Number Please,")
print(f"You Have Guessed the Number {n} Correctly in {guesses} Attempts !")
print("")
print("Thanks For Playing !!")
print("")
