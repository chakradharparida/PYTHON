class Employee:
    a=1
class Programmer(Employee):
    b=2
class Manager(Programmer):
    c=3
e=Employee()
print(e.a)
e=Programmer()
print(e.a,e.b)
e=Manager()
print(e.a,e.b,e.c)