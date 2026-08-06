x = 19
y = 56
res = x+y
print("sum=",res)

print("====================================")

res = lambda x,y:x+y
print(res(x=67,y=77))
res = lambda n1,n2:n1 if n1>n2 else n2
print(res(45,7))
