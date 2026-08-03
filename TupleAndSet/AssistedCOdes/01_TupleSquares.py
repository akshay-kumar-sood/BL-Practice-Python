# PROG 1: Creating a Tuple of Squares and Accessing Specific Elements


# Create squares using list comprehension
square_list = [num ** 2 for num in range(10)]

print(f"The List of Square of Numbers is {square_list}")

# Convert list into tuple
square_tuple = tuple(square_list)

print("Use of index for accessing elements in tuple")

print(f"3rd element: {square_tuple[2]}")
print(f"5th element: {square_tuple[4]}")
print(f"7th element: {square_tuple[6]}")

print(f"First 3 elements: {square_tuple[:3]}")