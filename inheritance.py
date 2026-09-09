class Emp:
    CompName = 'HCL'

    def __init__(self):
        self.Eid = int(input("Enter  Employee id:"))
        self.EmpName = input("Enter Employee Name:")
        self.BSal = float(input("Enter Employee Salary:"))
    def SalDetails(self):
        self.TA = (self.BSal*30)/100
        self.DA = (self.BSal*25)/100
        self.HRA = (self.BSal*10)/100
        self.ESI = (self.BSal*8)/100
class CalSal(Emp):
    def Gross(self):
        self.Gross = self.BSal + self.TA + self.DA + self.HRA + self.ESI
    def Display(self):
        print(f"Comp Name:\t {CalSal.CompName}")
        print(f"EID:\t {self.Eid}")
        print(f"Emp Name:\t {self.EmpName}")
        print(f"Emp BSal:\t Rs.{self.BSal}")
        print(f"Emp Gross:\t Rs.{self.Gross}")
no = int(input("Enter numbers of Emp:"))
for i in range (1,no+1):
    Cobj= CalSal()
    Cobj.SalDetails()
    Cobj.Gross()
    Cobj.Display()
    print("*"*35)
    








