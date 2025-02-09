class calculater:
    def __init__(self,n):
        self.n=n
    def Square(self):
        print(f"The square is : {self.n*self.n}")
    def Cube(self):
        print(f"The cube is : {self.n*self.n*self.n}")
    def SquareRoot(self):
        print(f"The SquareRoot is : {self.n**0.5}")
    @staticmethod
    def hello():
        print("Hello There !")


c=calculater(10)
c.hello()
c.Cube()
c.Square()
c.SquareRoot()

# Problem 05


