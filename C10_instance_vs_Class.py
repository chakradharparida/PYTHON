class employee :
    language = "Python"
    salary = 12000
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def gm():
        print("Good morning,")


chandan=employee()
chandan.gm()
chandan.getInfo()