i = 1
while i :
    print(i)
    if i ==4:
           break
    i += 1
print("i am outside of loop")
print("=================================")
i = 1
while i<4:
    print(i)
    j = 1
    while j < 3:
        print("\t",j)
        if j==2:
             break
        j+=1
    i+=1
    print("i am outside of inner loop")
print("i am outside of loop")
        
