from abc import ABC,abstractmethod
class ATM(ABC):
    Balance = 0.0
    @abstractmethod
    def Deposite(self):
        pass
    @abstractmethod
    def Withdraw(self):
        pass

class SBIATM(ATM):
    def Deposite(self,amount):
        print(f"By using SBIATM i Deposite Rs {amount}")
        SBIATM.Balance += amount
        print(f"After Withdraw Balance =Rs.{SBIATM.Balance}")
    def Withdraw(self,amount):
        print(f"By using SBIATM i Withdraw Rs {amount}")
        SBIATM.Balance -= amount
        print(f"After Withdraw Balance =Rs.{SBIATM.Balance}")

sbiobj = SBIATM()
while True:
    ch = input("select D for Deposite and W for Withdraw :")
    if ch == "D":
        amount = float(input("Enter Deposite amount Rs. :"))
        sbiobj.Deposite(amount)
    elif ch == "W":
        amount = float(input("Enter Withdraw amount Rs. :"))
        sbiobj.Withdraw(amount)
    else:
        print("Thank you")
        exit()
        
        
        
        
        
        
        
        
        
        
        
        
        


