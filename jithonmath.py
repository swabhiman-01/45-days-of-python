'''i am jithonmath module \n this module is a user define module used to test how module work'''
lit = 3.14

def Swap (no1,no2):
    '''swap function print swap between no1 and no2'''
    print (f'before swap no1={no1} and no2={no2}')
    no1 , no2 = no2 , no1
    print (f'after swap no1={no1} and no2={no2}')

def Add(x,y):
    '''Add function return addition of x and y'''
    return x+y

def Check(no):
    '''check function check no1 is even or odd'''
    return no if no%2 == 0 else no
class Py:
    '''Py is a predefine class'''
    def __init__(self):
        print("i am python constructer")
    def Pow(self,no):
        return no ** 2
