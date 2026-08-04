def Test():
    x = 10
    def Fun():
         nonlocal x
         x += 10
         print("i am nested/local fun print x=",x)
    Fun()
Test()





