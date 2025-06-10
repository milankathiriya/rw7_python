# Take Nothing, Return Nothing (TNRN)
# Without Parameters, No Return Value

# Function Definition
# def het():
#     print("Hello, I am Het")


# Function Calling
# het()






# Take Something, Return Nothing (TSRN)
# With Parameters, No Return Value

# Function Definition
# def het(n):
#     print("Hello, I am Het")
#     print(f"I recieved {n} rupees")


# Function Calling
# het(5000)
# het(8000)


# def addition(a, b):
#     print(a+b)

# addition(12, 34)
# addition(789, 125)











# Take Nothing, Return Something (TNRS)
# Without Parameters, With Return Value

# Function Definition
# def addition():
#     return 45 + 5


# Function Calling
# print(addition())

# ans = addition()

# print(ans)






# Take Something, Return Something (TSRS)
# With Parameters, With Return Value

# Function Definition
# def addition(a, b):
#     return a+b


# Function Calling
# print(addition(12, 45))

# ans = addition(48, 89)
# print(ans)







# Types of Function Arguments
'''
    1. Positional/Simple/Required Arguments
    2. Default Arguments
    3. Arbitrary Arguments
    4. Keyword Arguments
'''

# Keyword Arguments
# def addition(**kwargs):
#     print(f"My Dict: {kwargs}")


# addition()
# addition(a=12, b=10)
# addition(nidhi=78)
# addition(raju=78, golu=56, chandu=23)








# Documentation of a Function/Class/Module/Package
'''
    - We can create a documentation using a docstring.
    - A docstring can be denoted using triple quotes at the very first line of a body 
      of function/class/module/package.
    - A docstring can be accessed by using __doc__ (dunder doc).
      For example, functionName.__doc__
'''

# def addition(a, b):
#     '''
#     addition function performs the sum operation between given args.

#     arguments:
#     ---------
#     a -> int
#     b -> int

#     return type:
#     -----------
#     None
#     '''
#     print(a + b)


# print(addition.__doc__)
# print(help(addition))








# def calculation(a, b):
#     return (a+b, a-b, a*b)

# a, b, c = calculation(10, 2) 
# print(a)
# print(b)
# print(c)