class Payment:
    def Pay(self):
        print("Payment made by COD")

class UPI (Payment):
    def Pay(self):  #override
        super().Pay()  #using super() method we access parent class override method
        print("Payment made by using UPI")

Uobj = UPI()
Uobj.Pay()









