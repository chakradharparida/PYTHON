'''try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e :
    print(e)   
try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e :
    print(e)  
try:
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e :
    print(e)
    
print("Thank You !!")'''

#problem 02 

'''l=[2,3,4,5,6,7,8,9]

for i,item in enumerate(l):
    if i==1 or i==3 or i==5:
        print(item*item)'''
        
#Problem 03

'''n=int(input("Enter a number :"))

table=[n*i for i in range (1,11)]
print(table)'''

#Problem 04

'''try:
    a=int(input("Enter the 1st number :"))
    b=int(input("Enter the 2nd number :"))
    print(f"a/b = {a/b}")
except ZeroDivisionError as v :
    print("Infinite...")'''
    
#Problem 05

n=int(input("Enter a number :"))

table=[n*i for i in range (1,11)]
with open ("Table.txt","a") as T:
    T.write(f"Table of {n} : {str(table)}\n")