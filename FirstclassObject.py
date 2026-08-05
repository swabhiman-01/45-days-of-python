def Test():
    x = 10
    def Fun():
        print("i am nested/local Fun")
    Demo(x,Fun)#here we pass Fun as argument
def Demo(x,Fun):#here we catch Fun as argument
    print("i am Demo Fun x=",x)
    Fun()
Test()


