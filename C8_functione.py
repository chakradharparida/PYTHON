'''
def avg():
    a=int(input("Enter the NO. 1 :"))
    b=int(input("Enter the NO. 2 :"))
    c=int(input("Enter the NO. 3 :"))
    d=int(input("Enter the NO. 4 :"))
    n=4
    avarage=(a+b+c+d)/n
    print(avarage)
avg()
avg()
avg()
avg()
avg()
avg()
avg()
'''


# FUNCTIONS WITH ARGUMENTS


'''def goodDay(name,ending):
    print("Good day, "+ name)
    print(ending)
    return "ok"
a=goodDay("Chandan","Thank You !")
print(a)
b=goodDay("Sambit","Thank You !")
print(b)
c=goodDay("Abhinash","Thanks !")
print(c)'''


#DEFAULT ARGUMENTS 

'''def goodDay(name,ending="Thank You "):
    print(f"Good Day,{name}")
    print(ending)
goodDay("chandan","Thanks")
goodDay("Aditya")'''

#RECURSION

'''
factorial (0)=1
factorial (1)=1
factorial (2)=1X2
factorial (3)=1X2X3
factorial (4)=1X2X3X4
factorial (5)=1X2X3X4X5
.
.
.
factorial (n)=nX(n-1)X(n-2)


factorial (n)=n*factorial(n-1)
'''
'''def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n=int(input("Enter a Number :"))
print(f"The factorial of this no. is :{factorial(n)}")'''







