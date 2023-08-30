# Calculator
import art
# Add
def add (n1, n2):
    return n1 + n2

# Subtract
def subtract (n1, n2):
    return n1 - n2

# Multiply
def multiply (n1, n2):
    return n1 * n2

# Divide
def divide (n1, n2):
    return n1 / n2

# Create a dictionary where key is the symbols of the operator and the value is the name of the operations
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# way to the function based on the symbols
# function = operations['+'] - This will give you a addition operator function
def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))

    # looping through the dictionary

    for symbol in operations:
        print(symbol)

    # operation_symbol = input("Pick an operation from the line above: ")
    #
    # cal = operations[operation_symbol]
    # answer = cal(num1, num2)
    # print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_cal = True
    while continue_cal:
        operation_symbol = input("Pick an operation: ")
        num2 = float (input ("What's the next number: "))
        cal = operations[operation_symbol]
        first_answer = cal(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        user_input = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation.: ")

        if (user_input.lower() == 'y'):
            num1 = first_answer
        else:
            continue_cal = False
            calculator()

calculator()