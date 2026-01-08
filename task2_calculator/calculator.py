print("===== SIMPLE CALCULATOR =====")

while True:
    print("\nChoose operation:")
    print(" +  Addition")
    print(" -  Subtraction")
    print(" *  Multiplication")
    print(" /  Division")
    print(" q  Quit")

    operation = input("Enter operation (+, -, *, /, q): ")

    if operation == "q":
        print("Thank you for using the calculator!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
            continue

    else:
        print("Invalid operation")
        continue

    print("Result =", result)

