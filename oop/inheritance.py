'''
Parent Class == Base Class    == Super Class
Child Class  == Derived Class == Sub Class
'''

class A:
    # Default Constructor / Non-Parameterized Constructor
    def __init__(self):
        print("Class A")

class B(A):
    # Parameterized Constructor
    def __init__(self, x, y):
        self.a = x
        self.b = y
        super().__init__()
        print(f"Class B: {self.a + self.b}")


obj = B(45, 5)
