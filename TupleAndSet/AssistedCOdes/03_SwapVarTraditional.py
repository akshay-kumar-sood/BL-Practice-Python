# PROG 3.1: Swapping Variables Using Traditional Method

# Write The Code Here
# PROG 3.1: Swapping Variables Using Traditional Method

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("\nInitial Value of a & b are")
print(f"a = {a}")
print(f"b = {b}")

# Traditional swapping using third variable
temp = a
a = b
b = temp

print("\nAfter traditional swapping:")
print(f"a = {a}")
print(f"b = {b}")