#prompt user for an input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#prompt user for type of operation to be done
operation = input("Choose the operation (+, -, *, /): ")

#Perform Calculation Using Match Case
result = 0
error_message = "cannot divide by zero"

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0: 
            print(error_message)
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print(f"invalid operation '{operation}'. please choose from '+', '-', '*', '/'.")

#Printing result based on user input
if operation in {'+', '-', '*'}:
    print(f"The result is {result}.")
