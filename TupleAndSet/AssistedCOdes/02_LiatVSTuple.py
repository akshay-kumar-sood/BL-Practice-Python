# PROG 2: Comparing the Size and Creation Time of List vs. Tuple

# Write The Code Here
import sys
import timeit

# Same 10 integers
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Check memory size
print(f"Size of tuple: {sys.getsizeof(my_tuple)} bytes")
print(f"Size of list: {sys.getsizeof(my_list)} bytes")

# Check creation time
tuple_time = timeit.timeit(
    stmt=lambda: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    number=1000000
)

list_time = timeit.timeit(
    stmt=lambda: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    number=1000000
)

print(f"Creation time for tuple (in seconds): {tuple_time}")
print(f"Creation time for list (in seconds): {list_time}")