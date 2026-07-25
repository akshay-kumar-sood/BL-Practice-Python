# Self Practice COde

# POwer OF a Number

def power(base, exponent):
    return base ** exponent


base = int(input("Enter the Base Number : "))
exponent = int(input("Enter the Exponent Number : "))

result = power(base, exponent)

print(base, "raised to the power of", exponent, "is:", result)