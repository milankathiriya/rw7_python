print("Welcome to the Pattern Generator and Number Analyzer!\n")

while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1: 
            n = int(input("Enter the number of rows for the pattern: "))

            print("Pattern: ")
            for i in range(1, n+1):
                for j in range(1, i+1):
                    print("*", end=" ")
                print()

        case 2: 
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            sum = 0

            for i in range(start, end+1):
                sum = sum + i
                if i%2==0:
                    print("Number", i, "is Even")
                else:
                    print("Number", i, "is Odd")

            print("Sum of all numbers from", start, "to", end, "is:", sum)

        case 3: 
            print("Exiting the program. Goodbye!")
            break
        case _: print("Invalid choice")
