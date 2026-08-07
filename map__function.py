def square(no):
    return no ** 2

l = [2, 5, 67, 12, 4, 56, 6, 7, 78, 978, 90, 64, 16, 33, 23]

obj = map(square, l)

print(type(obj))
print(list(obj))

print("====================using lambda function=====================================")

l = [2, 5, 67, 12, 4, 56, 6, 7, 78, 978, 90, 64, 16, 33, 23]

obj = map(lambda no: no ** 2, l)

print(list(obj))

