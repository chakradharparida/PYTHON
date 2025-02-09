a=34
def fun():
    global a
    a=50
    print(a)
    
fun()
print(a)