from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = int(input("What is the first number?: "))
    num2 = int(input("What is the second number?: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick operation from the line above: ")

    result = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")

    keep_going = "y" == input("Keep going? (y/n)").lower()

    while keep_going:
        next_number = int(input("What is the next number: "))
        operation_symbol = input("What is the next operation?: ")
        result = operations[operation_symbol](result, next_number)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        keep_going = "y" == input("Keep going? (y/n)").lower()
    else:
        print("Bye")

calculator()