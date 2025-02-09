class Number :
    def __init__(self,n):
        self.n=n
    def __add__(self,add):
         return self.n+add.n
    def __mul__(self,mul):
        return self.n*mul.n

n=Number(2)
m=Number(9)
print(n+m)
print(n*m)