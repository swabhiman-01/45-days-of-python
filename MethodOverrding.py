class Payment:
    def Pay(self):
        print("Payment made by COD")

class UPI (Payment):
    def Pay(self): #override
        print("Payment made by using UPI")

class Card(Payment):
    def Pay(self):#override
        print("Payment made by using Card")
Uobj = UPI()
Uobj.Pay()
Cobj = Card()
Cobj.Pay()









