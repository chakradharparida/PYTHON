mark=int(input("Enter Your Mark :"))

if(mark<=100 and mark>=90):
    grade="O"
elif(mark<90 and mark>=80):
    grade="E"
elif(mark<80 and mark>=70):
    grade="A"
elif(mark<70 and mark>=60):
    grade="B"
elif(mark<60 and mark>=50):
    grade="C"
elif(mark<50 and mark>=35):
    grade="D"
elif(mark<35):
    grade="F"

print("Your Grade is :",grade)