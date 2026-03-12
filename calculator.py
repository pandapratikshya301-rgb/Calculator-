def calculator():
    print("<--- Simple CLI Calculator --->")
    print("Select operation: +, -, *, /")

    operation = input("Enter operation: ")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '+':
            result = num1 + num2
            print(f"Result: {result}")
            
        elif operation == '-':
            result = num1 - num2
            print(f"Result: {result}")
            
        elif operation == '*':
            result = num1 * num2
            print(f"Result: {result}")
            
        elif operation == '/':
            # Handling the division by zero edge case
            if num2 == 0:
                print("Error: You cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"Result: {result}")
        
        else:
            print("Invalid operation. Please use +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":

    calculator()
