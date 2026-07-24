obj = "hello Good Morning  All"
print (obj.split())
print (obj.split(" "))
print (obj.split(" ",2))
print (obj.split("Good"))
print (obj.rsplit ())
print (obj.rsplit(" ",2))
print(obj.partition(" "))
print(obj.rpartition(" "))
obj =" " " hello Good Morning All welcome to python world " " "
print (obj.split('\n'))
print (obj.splitlines())
obj = "hello\tGood\tMorning All\twelcome\tto\tpython\tworld"
print(obj)
print(obj.expandtabs())
print(obj.expandtabs(55))
print(obj.expandtabs(10000))
obj = "Good Morning"
print(obj)
newobj = obj.center(15)
print(newobj)
print (obj.ljust(15,"*"))
print (obj.ljust(15,"*"))
print(newobj.strip("*"))
print(newobj.rstrip("*"))
print(newobj.lstrip("*"))
obj = "hello my name is {} from{}"
print(obj.format("raj","BBSR"))
obj = "hello my name is {name} from{address}"
print(obj.format(address="CTC", name ="Amit"))
name , address = 'sony','puri'
print(f"hello iam {name} from{address}")
obj = "Python"
print(obj.replace("P","J"))
print(obj.replace("Py","Ji"))
obj = "How Are you?"
print(obj.endswith('.'))
print(obj.endswith('?'))
print(obj.startswith('A'))
print(obj.startswith('H'))































