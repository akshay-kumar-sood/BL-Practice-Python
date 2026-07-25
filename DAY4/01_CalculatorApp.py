#Self Practice Code
# Calculator App


def calculator(symbol, num1, num2):
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol == "*":
        return num1 * num2
    elif symbol == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    elif symbol == "%":
        return num1 % num2
    else:
        return "Invalid symbol"


symbol = input("Enter the symbol for the computation (+, -, *, /, %): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculator(symbol, num1, num2)

print("Result:", result)