#Globalkeyword
x = 10

def Test():
    global x
    x = x + 10
    print("Inside Test()")
    print("x =", x)

Test()

print("Outside Function")
print("x =", x)
