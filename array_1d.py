a1 = []
a2 = []
a3 = []

n = int(input("Enter array size: "))

print("Enter array a1's elements: ")
for i in range(n):
    a1.append(int(input("Enter array elem: ")))


print("Enter array a2's elements: ")
for i in range(n):
    a2.append(int(input("Enter array elem: ")))


print("Array a3's elements: ")
for i in range(n):
    a3.append(a1[i] + a2[i])
    
    
print(a3)
