# PROG 2: Fruit Store Inventory Management System

# Write The Code Here
in_stock = {'apple', 'watermelon', 'strawberry'}
out_of_stock = {'banana', 'orange', 'guava'}


def check_stock(fruit):
    fruit = fruit.lower()

    if fruit in in_stock:
        return f"{fruit.title()} is in stock."
    else:
        return f"{fruit.title()} is not in stock."


def list_items():
    all_items = in_stock | out_of_stock

    print("\nThe possible items that the store keeps are:")
    for fruit in all_items:
        print(fruit.title())


def update_stock(fruit, status):
    fruit = fruit.lower()
    status = status.lower()

    if status == "in":
        in_stock.add(fruit)
        out_of_stock.discard(fruit)
        return f"{fruit.title()} has been added to in-stock."

    elif status == "out":
        out_of_stock.add(fruit)
        in_stock.discard(fruit)
        return f"{fruit.title()} has been added to out-of-stock."

    else:
        return "Invalid status. Please enter 'in' or 'out'."


while True:

    print("\n--- Fruit Store Inventory Management ---")
    print("1. Check if a fruit is in stock")
    print("2. List all items in the store")
    print("3. Update stock (add/remove item)")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        fruit = input("Enter the name of the fruit to check: ")
        print(check_stock(fruit))

    elif choice == "2":
        list_items()

    elif choice == "3":
        fruit = input("Enter the name of the fruit: ")
        status = input(
            "Enter 'in' if the item is now in stock or 'out' if it is out of stock: "
        )

        print(update_stock(fruit, status))

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")