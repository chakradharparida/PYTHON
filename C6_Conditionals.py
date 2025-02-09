user=int(input("Enter Your Age : "))
if(user>=18):
    print("You are above the age of consent.")
    print("Now,you can make your own driving lisence ")
elif(user<0):
    print("You are entering an invalid Age.")
elif(user==0):
    print("You are entering 0.\nit is not an valid Age.")
else:
    print("You are below the age of consent.")
    print("Now,youcan't make your own driving lisence ")
print ("End The Program")