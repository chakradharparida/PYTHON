#map example

l=[10,2,3,4,5,6]

square= lambda x:x*x 
sqliest=map(square,l)
print(list(sqliest))

# Filter Example

def even(n):
    if(n%2==0):
        return True
    return False
onlyEven=filter(even,l)
print(list(onlyEven))

#Reduce Example 

def sum(a,b):
    return a+b
mul=lambda x,y:x*y
print(reduce(sum,l))
print(reduce(sum,l))