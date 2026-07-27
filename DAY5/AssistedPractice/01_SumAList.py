# Sum of a list


# PROG 1.1: By Using Hard-Coded List

def custom_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


numbers = [29, 45, 32, 49, 37]

custom_result = custom_sum(numbers)
builtin_result = sum(numbers)

print("The Original List is", numbers)
print("The Sum of the list using Custom function is", custom_result)
print("The Sum of the list using Builtin function is", builtin_result)
print("Comparing the results of Custom function and Builtin function:", custom_result == builtin_result)




# PROG 1.2: Taking List From The User

# Write The Code Here
def custom_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


n = int(input("Enter the number of elements in the list: "))

numbers = []

for i in range (n):
  while True:
    try:
          num = int(input("Enter a number: "))
          numbers.append(num)
          break

    except ValueError:
        print("Invalid input, please enter a valid number.")


custom_result = custom_sum(numbers)
builtin_result = sum(numbers)

print("The Original List is", numbers)
print("The Sum of the list using Custom function is", custom_result)
print("The Sum of the list using Builtin function is", builtin_result)
print("Comparing the results of Custom function and Builtin function:",
      custom_result == builtin_result)