'''
Method Overloading

    - Single Class
    - Multiple Methods
    - Methods name must be same, but parameters are different
'''

# class Vehicle:
#     def truck(self, *args):
#         if len(args) == 0:
#             print("Truck is running empty....")
#         elif len(args) == 1:
#             print(f"Truck is running with {args[0]} passengers....")
#         elif len(args) == 2:
#             print(f"Truck is running with {args[0]} passengers & {args[1]} goats....")


# obj = Vehicle()

# obj.truck()
# obj.truck(10)
# obj.truck(5, 17)

'''
Method Overriding

    - Multiple Classes, Inheritance is required
    - Multiple Methods
    - Methods name must be same, parameters are also same
'''

# class India:
#     def wearing(self):
#         print("Dhoti-Kurta")
    

# class Pak(India):
#     def wearing(self):
#         print("Pathani-Kurta")
#         super().wearing()


# aman = Pak()
# aman.wearing()


'''
Operator Overloading
'''

# class Het:
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b

#     def getData(self):
#         print(f"{self.x}, {self.y}")

#     def __add__(self, n):
#         return Het(self.x + n.x, self.y + n.y)


# o1 = Het(3, 5)
# o2 = Het(2, 3)


# o1.getData()
# o2.getData()


# o3 = o1 + o2    # o3 = o1.__add__(o2)
# o3.getData()





class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def getData(self):
        print(f"{self.name}, {self.age}, {self.salary}")

    def __lt__(self, n):
        return True if self.salary < n.salary else False


bob = Employee("Bob", 29, 18000)
dev = Employee("Dev", 32, 15000)

print(bob < dev)