'''
Write a recursive function to find the sum of all digits of a given number until a single-digit number remains.
'''

def sumOfDigits(n): # 0
    if n == 0:
        return 0
    return (n % 10) + sumOfDigits(n // 10)


# def sumOfDigits(n):
#     sum = 0
#     last_digit = n % 10     

#     while (n>=10):          
#         n = n // 10         
#         ld = n % 10         
#         sum += ld

#     return sum + last_digit


n = int(input("Enter any number: "))   # 783

ans = sumOfDigits(n)
print(ans)  # 11
