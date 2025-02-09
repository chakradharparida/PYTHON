i={100, 200 , 300, 400, 500, 600}

# index = 0
# for item in i :
#     print(f"The item number {index} is {item} ")
#     index +=1 

# this can be simplified using enumerate function

for index, item in enumerate(i):
    print(f"The item number {index} is {item} ")