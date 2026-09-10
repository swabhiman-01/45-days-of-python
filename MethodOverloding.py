print("=======================BY USING default arguments ======================")
class Operators:
        def Add(self,a=0,b=0,c=0,d=0,e=0,f=0):
            return a+b+c+d+e+f

obj = Operators()
print(obj.Add(2,3))
print(obj.Add(2,3,9))
print(obj.Add(2,3,9,78,45,12))
print("=======================BY USING *args ======================")
class Operators:
        def Add(self,*args):
            return ("argument list = ",args,"sum of all arguments=",sum(args))

obj = Operators()
print(obj.Add(2,3))
print(obj.Add(2,3,9))
print(obj.Add(2,3,9,78,45,12))
print(obj.Add(2,3,9,78,45,12,89,89,54,23,48,51,68,62,43,71,90,85,64,75))
















 