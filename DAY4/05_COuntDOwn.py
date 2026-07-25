#Slef Practice COde

# COunt Down using Recursion

def countdown(n):
    print(n)

    if n == 0:
        return

    countdown(n - 1)


num = int(input("Enter the number to print the count down: "))
countdown(num)