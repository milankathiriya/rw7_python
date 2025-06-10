x = 5

def disp():
    global x
    x += 1
    print(f"From the function: {x}")


print(f"From global area: {x}")
disp()
print(f"From global area: {x}")