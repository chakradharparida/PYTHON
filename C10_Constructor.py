class employee :
    language = "Python"
    salary = 12000
    def __init__(self,name,salary,language):#dunder method which is automeically called.
        self.name = name
        self.salary=salary
        self.language=language
        print("I am creating an object.")
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def gm():
        print("Good morning,")

chandan=employee("Chandan",15000,"C++")
print(chandan.name,chandan.salary,chandan.language)
# chandan=employee()
# chandan.gm()
# chandan.getInfo()