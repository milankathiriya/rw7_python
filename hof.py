# reduce(function, collection)

from functools import reduce


def my_criteria(n1, n2):
    return n1+n2

a = [1, 2, 3, 4, 5]

ans = reduce(my_criteria, a)

print(ans)
