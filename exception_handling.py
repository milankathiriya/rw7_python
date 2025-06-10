'''
Exception Handling
------------------

    1. try block
    2. except block
    3. else block
    4. finally block
    5. raise keyword
    6. assert keyword
'''

class AgeException(Exception):
    pass


age = int(input("Enter your age: "))

try:
    if age<18:
        raise AgeException("Age must be greater than or same as 18")
except AgeException as e:
    print(e)
else:
    print("You can vote")