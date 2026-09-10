class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
    def Show(self):
        print(f"person name = {self.Name} and Age = {self.Age}")

    def __gt__(self,value):
        return self.Age > value.Age

P1 = Person("BAPU",20)
P2 = Person("DEVA",30)
P1.Show()
P2.Show()
P3 = P1 > P2
print("person 1 Age is max "if P3 == True else "person 2 Age is max")

























