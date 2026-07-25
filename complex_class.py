obj = complex()
print("1.", obj, type(obj))
obj = complex(3)
print("2.", obj, type(obj))

obj = complex(3, 9)
print("3.", obj, type(obj))
obj = complex(real=37, imag=98)
print("4.", obj, type(obj))

obj = 71 + 120j
print("5.", obj, type(obj))
x = 3 + 7j
y = 8 + 4j

print("x =", x)
print("y =", y)
print("Addition       :", x + y)
print("Subtraction    :", x - y)
print("Multiplication :", x * y)
print("Division       :", x / y)
print("Power          :", x ** 2)
z = x
print("Assignment (z=x):", z)

print("x is z :", x is z)
print("x is y :", x is y)
print("x == z :", x == z)
print("x == y :", x == y)
