#write a file program to write all number and there sum in number.txt file
obj = open("number.txt",'w')
res = 0
for no in range (1,1+10):
    obj.write (str(no) + " ")
    res+= no
obj.write("\n"+f"sum of all number = {res}")

obj .close ()



