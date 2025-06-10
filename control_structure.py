# Types of control structure

'''
    1. Sequential
    2. Selection / Conditional
        a. if statement
        b. if else
        c. ladder
        d. nested
        e. short-hand syntax (ternary)
        f. match case (switch case)

    3. Iteration / Repeatative / Repeatation
        a. Entry-controlled loop
            i. while loop
            ii. for loop
        b. Exit-controlled loop
            i. do-while loop ❌
'''


# if condition:
#     body
# else:
#     body


# a = 3000
# b = 5000

# if a>b:
#     print("a is max")
# else:
#     print("b is max")


# WAP to check if a person is capable for vote or not using ladder if statement.


# if condition1:
#     body
# elif condition2:
#     body
# elif condition3:
#     body
# elif conditionN:
#     body
# else:
#     body

# age = int(input("Enter your age: "))

# if age > 18:
#     print("You can vote")
# elif age < 18:
#     print("You can't vote")
# else:
#     print("You can also vote")



# WAP to find maximum number from given two numbers.

# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))

# if a==b:
#     print("Both are same")
# else:
#     if a>b:
#         print("a is max")
#     else:
#         print("b is max")



# WAP to find maximum number from given three numbers.

# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
# c = int(input("Enter value of c: "))

# if a==b and b==c:
#     print("All are same")
# else:
#     if a==b:
#         print("a and b are same")
#     elif b==c:
#         print("b and c are same")
#     elif a==c:
#         print("a and c are same")
#     else:
#         if a>b:
#             if a>c:
#                 print("a is max")
#             else:
#                 print("c is max")
#         else:
#             if b>c:
#                 print("b is max")
#             else:
#                 print("c is max")


#  true_part if condition else false_part

# a = 3000
# b = 5000

# print("a is max") if a>b else print("b is max")


# WAP to print weekday based on user given character.

# c = input("Enter any character: ")

# match c:
#     case 'm': print("Monday")
#     case 'M': print("Monday")
#     case 't': print("Tuesday")
#     case 'w': print("Wednesday")
#     case 'W': print("Wednesday")
#     case 'T': print("Thursday")
#     case 'f': print("Friday")
#     case 'F': print("Friday")
#     case 's': print("Saturday")
#     case 'S': print("Sunday")
#     case _: print("Invalid choice...")



# WAP to create a Fast-food order system.

# print("Press 1 for Sandwich 🥪")
# print("Press 2 for Pizza 🍕")
# print("Press 3 for Burger 🍔")

# choice = int(input("Enter your choice: "))

# match choice:
#     case 1: print("You ordered a Sandwich 🥪")
#     case 2:
#         print("Press 1 for Fresh Dough Pizza 🍕")
#         print("Press 2 for Thin Crust Pizza 🍕")
#         print("Press 3 for Cheese Burst Pizza 🍕")

#         pizza_type = int(input("Enter your pizza type: "))

#         match pizza_type:
#             case 1: print("You ordered a Fresh Dough Pizza 🍕")
#             case 2: print("You ordered a Thin Crust Pizza 🍕")
#             case 3: print("You ordered a Cheese Burst Pizza 🍕")
#             case _: print("Pizza Type not available...")
#     case 3: print("You ordered a Burger 🍔")
#     case _: print("Invalid choice...")



'''
Three criterias must be satisfied to perform a while loop:
    1. Initialization
    2. Condition
    3. Increment/Decrement 
'''

# initialization
# while(condition):
#     body
#     increment/decrement


# WAP to print 1 to 10 numbers.

# i = 1
# while(i <= 10):
#     print(i)
#     i += 1


# WAP to print 10 to 1 numbers.

# i = 10
# while(i >= 1):
#     print(i, end=" ")
#     i -= 1


# WAP to print 1 to 10 numbers by skipping 1 number.

# i = 1
# while(i <= 10):
#     print(i)
#     i += 2


# WAP to print odd numbers from 1 to 10 numbers.

# i = 1
# while(i <= 10):
#     if i%2 == 1:
#         print(i)
#     i += 1


# WAP to print even numbers from 1 to 10 numbers.

# i = 1
# while(i <= 10):
#     if i%2 == 0:
#         print(i)
#     i += 1


# WAP to print all leap years from 2000 to 3000.

# i = 2000
# while(i <= 3000):
#     if i%4 == 0:
#         print(i)
#     i += 1


# WAP to print all numbers from 1 to N. Where, N is user given input.
# WAP to print all numbers from N to 1. Where, N is user given input.
# WAP to print all leap years from given range.
# WAP to print all numbers from M to N. Where, M, and N are user given inputs.


'''
for variable in sequence/collection:
    body
'''

# for i in "Python":
#     print(i)


''' 
range(start_value, end_value, step_value)

    - start_value: defaults 0
    - end_value: must be specified, and it is exclusive
    - step_value: defaults 1
'''

# range(10)         # 0 to 9
# range(0, 10)      # 0 to 9
# range(0, 10, 1)   # 0 to 9

# WAP to print all numbers from 1 to 10.
# for i in range(1, 11, 1):
#     print(i)

# WAP to print all numbers from 10 to 1.
# for i in range(10, 0, -1):
#     print(i)


# WAP to print all numbers from 1 to N. Where, N is user given input.
# WAP to print all numbers from N to 1. Where, N is user given input.
# WAP to print all leap years from given range.
# WAP to print all numbers from M to N. Where, M, and N are user given inputs.

# WAP to print a Multiplication table of N.

n = int(input("Enter value of n: "))

for i in range(1, 11):
    print(n, "x", i, "=", n*i)


# WAP to print Multiplication tables of given range.