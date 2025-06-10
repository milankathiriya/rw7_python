'''
class class_name:
    attributes
    methods
    constructor
    destructor
'''

'''
class_name()
'''

class Student:
    # constructor
    def __init__(self):
        self.__grid = int(input("Enter GRID: "))
        self.__name = input("Enter Name: ")
        self.__age = int(input("Enter Age: "))
        self.__course = input("Enter Course: ")

    # getter
    def getData(self):
        if self.__course == "C++":
            print(f"GRID: {self.__grid}, Name: {self.__name}, Age: {self.__age}, Course: {self.__course}")


# Array of Objects
all_students = []

n = int(input("How many students: "))

for i in range(n):
    all_students.append(Student())

# for i in range(n):
#     all_students[i].getData()

for stu in all_students:
    stu.getData()
