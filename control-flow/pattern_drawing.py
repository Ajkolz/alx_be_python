#prompt user to input size

size = int(input("Enter the size of the pattern: "))

#drawing loop pattern
row = 1
while row <= size:
    # print '*' for each column in the current row
    for column in range(size):
        print("*", end="")
    # move to the next line after printing each row
    print()
    row += 1

