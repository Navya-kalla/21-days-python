print("Welcome to the calculator app!🔢")
while True:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operation=input("Enter the operation you want to perform (+, -, *, /):")
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 !=0:
            result = num1 / num2
        else:
            result = "🚫Cannot divide  by zero!!🚫"
    elif operation == "//":
        if num2 !=0:
            result = num1 // num2
        else:
            result = "🚫Cannot divide with zero!!🚫"
    elif operation == "**":
        result = num1 ** num2
    elif operation == "%":
        result = num1 % num2
    else:
        result="Invalid Operation"
    print("Result:", result)
    choice = input("Do you want the calculator to stop calculating(yeah/nahh):")
    if choice=="nahh":
        print("Peace out!!✌✌")
        break