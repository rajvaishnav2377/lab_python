def sqr(num,exp=2):
    return num ** exp
print(sqr(3))
print(sqr(3,3))
print(sqr(2,4))

def greet(name = "guest"):
    print("hello",name)
greet("alice")
greet()

def add(a,b=5):
    print("sum:",a+b)
    add(10,20)
    add(10)