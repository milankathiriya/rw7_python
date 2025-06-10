arr = []
sum = 0

row_size = int(input("Enter row size: "))
col_size = int(input("Enter col size: "))

for i in range(row_size):
    a = []
    for j in range(col_size):
        a.append(int(input("Enter array elem: ")))
    arr.append(a)


col_num = int(input("Enter col number: "))

print("Array is: ")
for i, row in enumerate(arr):
    for j, elem in enumerate(row):
        if j==col_num:
            sum = sum + elem
    print()

print("Sum is %d" %sum)