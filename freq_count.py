name = input("Enter any string: ")   # 

subjects = input("Enter subjects(separeted by comma): ")  # Maths, Science, Gujarati

freq = {}

for i in name:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1


print(freq)