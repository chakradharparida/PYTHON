class Employee:
    language = "Python"
    salary = 1200000
    
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object.")
        
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
        
    @staticmethod
    def gm():
        print("Good Morning")
# Chandan=Employee()
# Chandan.name="Chandan Parida"
Aditya=Employee()
Aditya.name="Aditya Pradhan"
# Chandan = Employee("Chandan",120000000000,"C++")
# Chandan.language="Java"
# Chandan.gm()
# Chandan.getInfo()
# Employee.getInfo(Chandan)
# print(Chandan.name,Chandan.language,Chandan.salary)
#print("name :",Aditya.name,"| Language :",Aditya.language,"| Salary :",Aditya.salary)
Aditya.getInfo()
