import CustomMOdule

import random

numbers = []

for i in range(10):
    numbers.append(random.uniform(1, 100))

print("Random Numbers:", numbers)
print("Mean:", CustomMOdule.mean(numbers))
print("Minimum:", CustomMOdule.minimum(numbers))
print("Maximum:", CustomMOdule.maximum(numbers))