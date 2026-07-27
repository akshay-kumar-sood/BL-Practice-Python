# PROG 4: Execution Time Calculation

# Write The Code Here
import random
import time


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def generate_list(n):
    numbers = []

    for i in range(n):
        numbers.append(random.randint(1, 100))

    return numbers


# Create prime list once
primes = []

for i in range(1, 101):
    if is_prime(i):
        primes.append(i)


sizes = [100, 10000, 100000]

for size in sizes:

    numbers = generate_list(size)

    # Normal method
    start = time.time()

    new_list = []

    for num in numbers:
        if not is_prime(num):
            new_list.append(num)

    normal_time = time.time() - start


    # Optimized method
    start = time.time()

    new_list = []

    for num in numbers:
        if num not in primes:
            new_list.append(num)

    optimized_time = time.time() - start


    print("Size:", size)
    print("Normal Time:", normal_time)
    print("Optimized Time:", optimized_time)
    print("Difference:", normal_time - optimized_time)
    print()