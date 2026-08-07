l = [32, 5, 67, 12, 4, 56, 6, 7, 78, 978, 90, 64, 16, 33, 23]

def check(no):
    if no % 2 == 0:
        return True

obj = filter(check, l)

print(list(obj))

print("===================using lambda function=================")

l = [32, 5, 67, 12, 4, 56, 6, 7, 78, 978, 90, 64, 16, 33, 23]

obj = filter(lambda no: no % 2 == 0, l)

print(list(obj))
