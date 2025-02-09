class Employee :
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def ShowDetails(self) :
        print(f"The name of the employee : {self.id}, is {self.name}")
class Coder :
    language="Java"
    def ShowLanguage(self):
        print = f"Out of all language here is your language : {self.language}"
class Programmer(Employee,Coder) :
    def ShowLanguage(self):
        print("The default language is Python.")
        
class Maa(Employee) :
    print("My Mother is best.")
        
e1=Employee("Chandan Parida",435)
e1.ShowDetails()
e2=Programmer("Sridhar Parida",320)
e2.ShowDetails()
e2.ShowDetails()
e2.ShowLanguage()
e3=Maa("Malati Parida",1)
e3.ShowDetails()

