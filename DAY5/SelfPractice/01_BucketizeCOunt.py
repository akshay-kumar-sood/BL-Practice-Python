import random

numbers = []

# Generate 1000 random float numbers between 0 and 100
for i in range(1000):
    numbers.append(random.uniform(0, 100))

buckets = [0, 0, 0, 0, 0]

# selecting based on coonditions
for num in numbers:
    if num < 20:
        buckets[0] += 1
    elif num < 40:
        buckets[1] += 1
    elif num < 60:
        buckets[2] += 1
    elif num < 80:
        buckets[3] += 1
    else:
        buckets[4] += 1


# printing the result
print("Bucket 0 to 20:", buckets[0], "numbers")
print("Bucket 20 to 40:", buckets[1], "numbers")
print("Bucket 40 to 60:", buckets[2], "numbers")
print("Bucket 60 to 80:", buckets[3], "numbers")
print("Bucket 80 to 100:", buckets[4], "numbers")