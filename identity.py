# Python Identity Operators (is and is not)

x = [10, 20, 30]
y = [10, 20]
z = [10, 20, 30]

print("x is y :", x is y)
print("x is z :", x is z)
print("y is z :", y is z)

x = -5
y = -5
print("-5 :", x is y)

x = -6
y = -6
print("-6 :", x is y)

x = 256
y = 256
print("256 :", x is y)

x = 257
y = 257
print("257 :", x is y)

a = 10
b = 20

print("a is not b :", a is not b)
print("a is not a :", a is not a)
