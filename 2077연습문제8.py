def add(a,b):
    print ("(%d+%d)"%(a,b),end=" ")
    return a+b

def subtract (a,b):
    print ("(%d-%d)"%(a,b),end=" ")
    return a-b

def multiply (a,b):
    print ("(%d*%d)"%(a,b),end=" ")
    return a*b

def divide (a,b):
    print ("(%d/%d)"%(a,b),end=" ")
    return a/b

what=add(20,10)
print("= ", what)
what=subtract(20,10)
print("= ", what)
what=multiply(20,10)
print("= ", what)
what=divide(20,10)
print("= ", what)
