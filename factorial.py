# 4! = 4 * 3 * 2 * 1 => 24
# 1! = 1
# 0! = 1
# -2! = 1
# -3! = 1

def findFact(n):
    fact = 1

    for i in range(n, 0, -1):
        fact = fact * i

    return fact

n = int(input("Enter any number: "))
print(findFact(n))
