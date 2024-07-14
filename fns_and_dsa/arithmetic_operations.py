def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif opereation == 'multiply':
        return num1 * num2
    elif operation == 'division':
        if num2 == 0:
            return "error division by Zero"
        result = num1 / num2
    else:
        return "error invalid operation"
