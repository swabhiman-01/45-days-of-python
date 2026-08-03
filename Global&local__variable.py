#Global Variable

print("Global variable")

x = 10

def Test():
    print("Inside Test()")
    print("x =", x)

Test()

print("Outside Function")
print("x =", x)

#local variable

print("Local variable")


x = 10

def Test():
    x = 100
    print("Inside Test()")
    print("x =", x)

Test()

print("Outside Function")
print("x =", x)
