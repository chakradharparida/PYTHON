marks1=int(input("Enter Your Marks in DSA :"))
marks2=int(input("Enter Your Marks in DBMS :"))
marks3=int(input("Enter Your Marks in OS :"))
marks4=int(input("Enter Your Marks in PYTHON :"))

total_percentage=((marks1+marks2+marks3)*100)/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print ("You are passed :",total_percentage,"%")
else:
    print("You are fail !,Try again next Year !!",total_percentage,"%")