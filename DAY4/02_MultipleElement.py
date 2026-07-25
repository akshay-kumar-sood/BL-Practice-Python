# Self Practice COde
# Multiple ELements in A List

def multiply_all(numbers):
    result = 1

    for num in numbers:
        result = result * num

    return result


numbers = [10, 2, 3]

print("Original List :", numbers)
print("Result After Multiplying Elements In The List :", multiply_all(numbers))