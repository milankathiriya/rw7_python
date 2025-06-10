def findFact(n):
    if n<=1:
        return 1
    else:
        return n*findFact(n-1)


n = int(input("Enter any number: ")) 
print(findFact(n))
