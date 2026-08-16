from csv import*
#===================================================
filename = 'student.csv'
def create():
    try:
       obj = open(filename,'w',newline ='\n')
       wobj = writer (obj)
       wobj.writerow (['Rollno','Name','Dept','Age','Gender','ClgName'])
       obj.close ()
    except FileExistsError:
        print("file is present")
#===================================================
def InsertRow():
    obj = open(filename,'a',newline ='\n')
    wobj = writer (obj)
    rollno = int(input("enter student Rollno"))
    name = (input("enter student Name"))
    dept = (input("enter student Dept Name"))
    age = int(input("enter student Age"))
    gender = (input("enter student Gender(M/F)"))
    cname = (input("enter student ClgName"))

    if obj.tell()==0:
        wobj.writerow (['Rollno','Name','Dept','Age','Gender','ClgName'])
    else:
        wobj.writerow ([rollno,name,dept,age,gender,cname])
        print("successfully added a new record")
    obj.close()

#==================================================
def Display():
    try:
        obj = open(filename,'r')
        records = reader(obj)
        for record in records:
            print(record)
    except FileNotFoundError:
        print("file not found")

while True :
    ch = input('''select C for create csv file \n I for insert data\n S for show data\n E for Exit ''')
    if ch == 'C':
        create()
    elif ch == 'I':
        InsertRow()
    elif ch == 'S':
        Display()
    elif ch == 'E':
        print("thank you")
        break
    else :
        print("sorry invalid choice")
        break
