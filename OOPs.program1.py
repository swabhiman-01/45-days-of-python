class Student:
    '''this student class is user define class,i am a doc string describe details about student class'''
    
    ClgName = 'NIT'

    def __init__(self):
        ''' init collect student attribute details '''
        self.Rollno = int(input("Enter student Rollno:"))
        self.Name = input("Enter student Name:")
        self.Dept = input("Enter student Dept:")

    def GetMark(self):
        ''' GetMark describe details about student mark '''
        self.Math = float(input("Enter student Mathmark:"))
        self.Phy = float(input("Enter student Phymark:"))
        self.eng = float(input("Enter student Engmark:"))

    def Display(self):
        ''' Display show all attribute about Student class '''
        print("Student ClgName ", Student.ClgName)
        print("Student Rollno ", self.Rollno)
        print("Student Name ", self.Name)
        print("Student Total Mark= ", self.Math + self.Phy + self.eng)
no = int(input("Enter numbers of student:"))
for i in range(1,no+1):
     obj = Student()  # obj is object of Student class
     obj.GetMark()
     obj.Display()
     print("="*30)













