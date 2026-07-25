# Self Practice Code

# Check Prime

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


print("Prime numbers between 1 and 100:")

for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")