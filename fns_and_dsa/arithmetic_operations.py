def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
           return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return f"Unknown operation: {operation}"

# Example usage:
#print(perform_operation(10, 5, 'add'))
#print(perform_operation(50, 20, 'subtract'))
#print(perform_operation(6, 7, 'multiply'))
#print(perform_operation(8, 2, 'divide'))
#print(perform_operation(10, 0, 'divide'))