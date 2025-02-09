#QUESTION 01
"""def greatest(a,b,c):
    if(a>b and a>c):
     return a
    elif(b>c and b>a):
     return b
    elif(c>b and c>a):
     return c
a=int(input("Enter The Number :"))
b=int(input("Enter The Number :"))
c=int(input("Enter The Number :"))
print("The greatest no. is :",greatest(a,b,c))"""

#QUESTION 02

'''def F_to_C(f):
    return 5*(f-32)/9

f=int(input("Enter temperature in F :"))
c=F_to_C(f)
print(f"{round(c,2)}°C")'''

#QUESTION 03
#end function Q

'''print("a")
print("b")
print("c",end="")
print("d",end="")
print("e",end="")'''

#QUESTION 04
#end recurtion Q
#SOME OF N NUMBERS

'''def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(3))'''

#QUESTION 05

'''def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
n=int(input("Ente a number :"))
pattern(n)'''

#QUESTION 06

'''def int_to_cm(inch):
    return inch*2.54
n=int(input("Enter value in inches :"))
print(f"the value in cms is {int_to_cm(n)}")'''

#QUESTION 07

'''def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=["chandan","rama","hari","harish","ma"]
print(rem(l,"ma"))'''

#QUESTION 08
n=int(input("Enter a number :"))
def multiply(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
multiply(n)