import random

def flip_coin():
    return random.choice(["Head", "Tail"])


def run_flip_a_coin(n):
    head_count = 0

    for i in range(n):
        result = flip_coin()

        if result == "Head":
            head_count += 1

    percentage = (head_count / n) * 100
    return percentage


n = int(input("Enter the number of times to flip the coin: "))

percentage = run_flip_a_coin(n)

print(f"After flipping the coin {n} times, the percentage of times head has come is: {percentage:.2f}%")