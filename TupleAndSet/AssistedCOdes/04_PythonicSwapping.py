# PROG 3.2: Swapping Variables Using Pythonic Method

# Write The Code Here
# PROG 3.2: Swapping Variables Using Pythonic Method

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("\nInitial Value of a & b are")
print(f"a = {a}")
print(f"b = {b}")

# Pythonic swapping
a, b = b, a

print("\nAfter pythonic swapping:")
print(f"a = {a}")
print(f"b = {b}")