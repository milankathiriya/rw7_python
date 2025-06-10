'''
Syntax:

1. [value for var in seq/coll.]
2. [value for var in seq/coll. if cond.]
3. [value if cond. else value for var in seq/coll.]
'''

# WAP to create a list of squares of another list items.

numbers = [5, 9, 3, 4, 6, 8]

answers = ["Even" if i%2==0 else "Odd" for i in numbers]

print(answers)
