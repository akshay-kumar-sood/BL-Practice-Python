import Calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum:", Calculator.add(num1, num2))
print("Difference:", Calculator.subtract(num1, num2))
print("Product:", Calculator.product(num1, num2))
print("Quotient:", Calculator.divide(num1, num2))