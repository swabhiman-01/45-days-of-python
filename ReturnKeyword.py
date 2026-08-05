def Test():
    return 10,20,30
    print("hello")
print(Test())
x,y,z = Test()#Catch by multiple value
x = Test()#Catch by single value
print(type(x),x)
print(x[0])
print(x[2])


