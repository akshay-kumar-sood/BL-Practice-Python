# PROG 3.3: Swapping Variables Using Tuple Packing and Unpacking

# Write The Code Here
# PROG 3.3: Swapping Using Tuple Packing and Unpacking

def swap(a, b):
    temp = (b, a)       # Tuple packing
    x, y = temp         # Tuple unpacking
    return x, y         # Returns a tuple


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("\nInitial Value of a & b are")
print(f"a = {a}")
print(f"b = {b}")

x, y = swap(a, b)

print("\nAfter swapping (using function):")
print(f"x = {x}")
print(f"y = {y}")