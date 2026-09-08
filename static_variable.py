class Test:

    def __init__(self):
        self.A = 10       # Instance variable
        Test.B = 20       # Static/Class variable

T1 = Test()   # T1 is object of Test
T2 = Test()   # T2 is object of Test

print(f"Using object 1 instance var={T1.A}\n static var={Test.B}")      # 10 20

print(f"Using object 2 instance var={T2.A}\n static var={T1.B}")        # 10 20

T1.A = 1000   # Update instance variable using object 1

Test.B = 2000  # Update static variable

print(f"Using object 1 instance var={T1.A}\n static var={Test.B}")      # 1000 2000

print(f"Using object 2 instance var={T2.A}\n static var={T2.B}")        # 10 2000




















